#!/usr/bin/env python

"""Launch a system to interactively create a character."""

import logging
# logging.basicConfig(filename='character_creater.log', level=logging.DEBUG)
log = logging.getLogger(__name__)

import math
import os
from random import randint
import subprocess

import npyscreen
import jinja2

from dungeonsheets import character, race, dice, background, classes


def read_version():
    version = open(os.path.join(os.path.dirname(__file__), '../VERSION')).read()
    version = version.replace('\n', '')
    return version


char_classes = {c.name: c for c in classes.available_classes}

races = {r.name: r for r in race.available_races}

backgrounds = {b.name: b for b in background.available_backgrounds}


class LinkedListForm(npyscreen.ActionForm):
    prev_page = None
    this_page = None
    next_page = None

    def __init__(self, formid, *args, **kwargs):
        self.this_page = formid
        super().__init__(*args, **kwargs)

    def to_next(self):
        self.parentApp.setNextForm(self.next_page)

    def to_prev(self):
        self.parentApp.setNextForm(self.prev_page)

    def add_next(self, next_name):
        new_next = self.parentApp.getForm(next_name)
        if self.next_page:
            current_next = self.parentApp.getForm(self.next_page)
            current_next.prev_page = next_name
        new_next.next_page = self.next_page
        new_next.prev_page = self.this_page
        self.next_page = next_name

    def add_prev(self, prev_name):
        new_prev = self.parentApp.getForm(prev_name)
        if self.prev_page:
            current_prev = self.parentApp.getForm(self.prev_page)
            current_prev.next_page = prev_name
        new_prev.prev_page = self.prev_page
        new_prev.next_page = self.this_page
        self.prev_page = prev_name

    def prune(self):
        if self.next_page:
            next_form = self.parentApp.getForm(self.next_page)
            next_form.prev_page = self.prev_page
        if self.prev_page:
            prev_form = self.parentApp.getForm(self.prev_page)
            prev_form.next_page = self.next_page
        self.parentApp.removeForm(self.this_page)


class App(npyscreen.NPSAppManaged):
    # STARTING_FORM = 'SKILLS'
    character = None
    n_classes = 1
    
    def save_character(self):
        # Save the file
        filename = self.getForm("SAVE").filename.value
        self.character.save(filename, template_file='empty_template.txt')
        # Create the PDF character sheet
        if self.getForm('SAVE').make_pdf.value:
            log.debug("Creating PDF")
            self.character.to_pdf(filename, template_file='empty_template.txt')
            subprocess.call(['makesheets', filename])
    
    def update_max_hp(self):
        # Update max HP based on the class
        max_hp_fld = self.getForm('ABILITIES').max_hp
        if max_hp_fld.value == '':
            # Calculate the new value
            hit_dice = [dice.read_dice_str(d)
                        for d in self.character.hit_dice.split(' + ')]
            const = self.character.constitution.modifier
            # Assume first hd given is from primary class
            max_hp = math.floor(hit_dice[0].faces/2) + const
            for hd in hit_dice:
                for d in range(hd.num):
                    max_hp += math.ceil(hd.faces/2) + const
            log.debug("Updating max hp: %d", max_hp)
            max_hp_fld.value = str(max_hp)
    
    def onStart(self):
        self.character = character.Character()
        self.addForm("MAIN", BasicInfoForm, name="Basic Info:", formid='MAIN')
        self.addForm("RACE", RaceForm, name="Select your character's race:",
                     formid='RACE')
        self.addForm("CLASS1", CharacterClassForm, name="Select your character's primary class:",
                     formid='CLASS1')
        self.addForm("BACKGROUND", BackgroundForm, name="Choose background:",
                     formid='BACKGROUND')
        self.addForm("ALIGNMENT", AlignmentForm,
                     name="Select your character's alignment:",
                     formid='ALIGNMENT')
        self.addForm("ABILITIES", AbilityScoreForm,
                     name="Choose ability scores:", formid='ABILITIES')
        self.addForm("SKILLS", SkillForm, name="Choose skill proficiencies",
                     formid='SKILLS')
        self.addForm("SAVE", SaveForm, name="Save character:", formid='SAVE')

        # Initialized the DoublyLinkedList
        forms = ['MAIN', 'RACE', 'CLASS1', 'BACKGROUND',
                 'ALIGNMENT', 'ABILITIES', 'SKILLS', 'SAVE']
        for i in range(len(forms)-1):
            form = self.getForm(forms[i])
            form.add_next(forms[i+1])


class BasicInfoForm(LinkedListForm):
    def create(self):
        self.name = self.add(
            npyscreen.TitleText, name="Character Name:", use_two_lines=False)
        self.player_name = self.add(
            npyscreen.TitleText, name="Player Name:", use_two_lines=False)
    
    def on_ok(self):
        # Update the default filename
        name = self.name.value
        if name == '':
            filename = 'new_character.py'
        else:
            filename = f'{name.split(" ")[0].lower()}.py'
        save_form = self.parentApp.getForm('SAVE')
        save_form.filename.value = filename
        self.parentApp.character.name = self.name.value
        self.parentApp.character.player_name = self.player_name.value
        super().to_next()
    
    def on_cancel(self):
        raise KeyboardInterrupt

    
class RaceForm(LinkedListForm):
    def create(self):
        self.race = self.add(
            npyscreen.TitleSelectOne, name="Race:", values=tuple(races.keys()))
    
    def on_ok(self):
        if self.race.value is not None:
            selected_race = self.race.get_selected_objects()[0]
            SelectedRace = races[selected_race]
            log.debug('Selected character race: %s', SelectedRace.name)
            self.parentApp.character.race = SelectedRace
            super().to_next()

    def on_cancel(self):
        super().to_prev()
        

class CharacterClassForm(LinkedListForm):
    class_num = 1

    def __init__(self, num=1, **kwargs):
        self.class_num = num
        self.class_options = list(char_classes.keys())
        super().__init__(**kwargs)

    @property
    def subclass_page(self):
        key = "SUBCLASS{:d}".format(self.class_num)
        if key in self.parentApp._Forms:
            return self.parentApp.getForm(key)
        else:
            return None

    @property
    def next_multiclass_page(self):
        key = "CLASS{:d}".format(self.class_num+1)
        if key in self.parentApp._Forms:
            return self.parentApp.getForm(key)
        else:
            return None

    def update_options(self):
        if len(self.parentApp.character.class_list) == 0:
            return
        else:
            self.class_options = list(char_classes.keys())
            for c in self.parentApp.character.class_list[:self.class_num-1]:
                self.class_options.remove(c.name)
            self.character_class.values = sorted(tuple(self.class_options))
            self.character_class.update()
        
    def create(self):
        if self.class_num > 1:
            self.add(npyscreen.FixedText, editable=False,
                     value="Current Classes: {}".format(
                         self.parentApp.character.name))
        if self.class_num == 1:
            t = 'Primary Class:'
        else:
            t = 'Class #{:d}:'.format(self.class_num)
        for c in self.parentApp.character.class_list:
            self.class_options.remove(c.name)
        if self.class_num == 1:
            self.multiclass = self.add(npyscreen.Checkbox, name="Add Multiclass?".format(self.class_num + 1), value=False)
        else:
            self.multiclass = self.add(npyscreen.Checkbox, name="Add Class #{:d}?".format(self.class_num + 1), value=False)
        self.level = self.add(
            npyscreen.TitleText, name='Level:', value="1", use_two_lines=False)
        self.character_class = self.add(
            npyscreen.TitleSelectOne, name=t, values=tuple(self.class_options))

    def add_multiclass_page(self):
        new_name = "CLASS{:d}".format(self.class_num + 1)
        new_form = self.parentApp.addForm(new_name,
                                          CharacterClassForm,
                                          name="Select your character's Class #{:d}:".format(self.class_num + 1),
                                          num=self.class_num+1,
                                          formid=new_name)
        self.add_next(new_name)
        return new_form

    def add_subclass_page(self, newclass, level):
        new_name = 'SUBCLASS{:d}'.format(self.class_num)
        new_form = self.parentApp.addForm(new_name,
                                          SubclassForm,
                                          name="Select your {:s} Subclass".format(newclass.name),
                                          newclass=newclass,
                                          level=level,
                                          num=self.class_num,
                                          formid=new_name)
        self.add_next(new_name)
        return new_form
        
    def on_ok(self):
        if self.character_class.value is not None:
            selected_class = self.character_class.get_selected_objects()[0]
            selected_class = char_classes[selected_class]
            log.debug('Selected character class %s', selected_class.name)
            # replace later classes if we've backed up
            self.parentApp.character.class_list = self.parentApp.character.class_list[:self.class_num-1]
            self.parentApp.character.add_class(cls=selected_class,
                                               level=int(self.level.value),
                                               subclass=None)
            # add multiclass page if not exists yet
            if self.multiclass.value:
                if self.next_multiclass_page is None:
                    self.add_multiclass_page()
                else:
                    self.next_multiclass_page.update_options()
            else:
                # in case returned a page, prune any future multiclasses
                while self.next_page != 'BACKGROUND':
                    f = self.parentApp.getForm(self.next_page)
                    f.prune()
            if int(self.level.value) >= selected_class.subclass_select_level:
                if not self.subclass_page:
                    self.add_subclass_page(newclass=selected_class,
                                           level=int(self.level.value))
            else:
                if self.subclass_page is not None:
                    f = self.parentApp.getForm(self.next_page)
                    f.prune()
            super().to_next()
        
    def on_cancel(self):
        super().to_prev()


class SubclassForm(LinkedListForm):
    def __init__(self, newclass, level, num=1, **kwargs):
        self.class_num = num
        self.parent_class = newclass
        if len(newclass.subclasses_available) > 0:
            self.subclass_options = [sc.name for sc in newclass.subclasses_available]
        else:
            self.subclass_options = ('None',)
        self.level = level
        super().__init__(**kwargs)
    
    def create(self):
        self.subclass = self.add(
            npyscreen.TitleSelectOne, name="Subclass:",
            values=tuple(self.subclass_options))
        
    def on_ok(self):
        if self.subclass.value is not None:
            sc = self.subclass.get_selected_objects()[0]
            if sc in [None, '', 'None']:
                sc = None
                self.parentApp.character.class_list = self.parentApp.character.class_list[:self.class_num-1]
                self.parentApp.character.add_class(cls=self.parent_class,
                                                   level=self.level,
                                                   subclass=sc)
            super().to_next()
            
    def on_cancel(self):
        super().to_prev()


class BackgroundForm(LinkedListForm):
    def create(self):
        self.background = self.add(
            npyscreen.TitleSelectOne,
            name="Background:", values=tuple(backgrounds.keys()))
    
    def on_ok(self):
        if self.background.value is not None:
            selected_bg = self.background.get_selected_objects()[0]
            Background = backgrounds[selected_bg]
            self.parentApp.character.background = Background()
            # Update the languages based on background and race
            race_languages = self.parentApp.character.race.languages
            languages = Background.languages + race_languages
            self.parentApp.character.languages = ', '.join(languages)
            log.debug("Selected character background: %s", Background.name)
            super().to_next()
    
    def on_cancel(self):
        super().to_prev()


class AlignmentForm(LinkedListForm):
    """Choose your character's alignment."""
    alignments = ('Lawful good', 'Neutral good', 'Chaotic good',
                  'Lawful neutral', 'True neutral', 'Chaotic neutral',
                  'Lawful evil', 'Neutral evil', 'Chaotic evil', )
    def create(self):
        self.alignment = self.add(
            npyscreen.TitleSelectOne, name="Alignment:", values=self.alignments)
    
    def on_ok(self):
        if self.alignment.value is not None:
            selected_alignment = self.alignment.get_selected_objects()[0]  # values[self.alignment.value]
            log.debug('Selected character alignment %s', selected_alignment)
            self.parentApp.character.alignment = selected_alignment
            # prep additions to abilities page
            abils = self.parentApp.getForm('ABILITIES')
            abils.prep()
            super().to_next()
    
    def on_cancel(self):
        super().to_prev()


class AbilityScoreForm(LinkedListForm):
    num_rolls = 0

    def roll_dice(self):
        """Get six ability scores that can then be assigned to abilities.""" 
        def roll_score():
            # Roll 4 dice and add the 3 highest
            rolls = (randint(1, 6) for i in range(4))
            score = sum(sorted(rolls)[-3:])
            return score
        scores = (roll_score() for i in range(6))
        return tuple(sorted(scores, reverse=True))

    def default_array(self):
        return (15, 14, 13, 12, 10, 8)

    def reroll(self, widget=None):
        self.num_rolls += 1
        new_scores = self.roll_dice()
        self.score_options.value = str(new_scores)[1:-1]
        self.score_options.update()
        self.reroll_button.value = False
        self.reroll_button.name = 'Reroll'
        self.reroll_button.update()
        self.default_button.value = False
        self.default_button.update()

    def set_default(self, widget=None):
        new_scores = self.default_array()
        self.score_options.value = str(new_scores)[1:-1]
        self.score_options.update()
        self.default_button.value = True
        self.default_button.update()
    
    def reset(self):
        # Update the character in real time
        attrs = ('strength', 'dexterity', 'constitution',
                 'intelligence', 'wisdom', 'charisma')
        for attr in attrs:
            getattr(self, attr).value = ''
    
    def while_editing(self):
        # Update the character in real time
        attrs = ('strength', 'dexterity', 'constitution',
                 'intelligence', 'wisdom', 'charisma')
        for attr in attrs:
            fld = getattr(self, attr)
            try:
                race_bonus = getattr(self.parentApp.character.race,
                                     f'{attr}_bonus')
                val = int(float(fld.value))
            except ValueError:
                # Not an integer, so clear the field
                fld.value = ''
            else:
                # Valid number, so process it
                val += race_bonus
                curr_val = getattr(self.parentApp.character, attr).value
                if val != curr_val:
                    log.debug("Setting %s to %s", attr, str(val))
                    # Update the "character" with new values
                    setattr(self.parentApp.character, attr, val)
                    if attr == 'constitution':
                        self.parentApp.update_max_hp()
        # Update the form display
        self.display()
        
    def create(self):
        self.roll_text = self.add(npyscreen.FixedText, editable=False,
                                  value="Take the six rolls below and assign each one to an ability.")
        self.score_options = self.add(
            npyscreen.TitleFixedText, name="Rolls:", editable=False,
            value=str(self.default_array())[1:-1])
        self.default_button = self.add(npyscreen.MiniButtonPress,
                                       name="Use Default Rolls",
                                       when_pressed_function=self.set_default)
        self.reroll_button = self.add(npyscreen.MiniButtonPress,
                                      name="Reroll",
                                      when_pressed_function=self.reroll)

    def prep(self):
        attrs = ('strength', 'dexterity', 'constitution',
                 'intelligence', 'wisdom', 'charisma')
        self.class_text = self.add(npyscreen.FixedText, editable=False,
                                  value="Key stats for your primary class {:s} are listed with **".format(self.parentApp.character.primary_class.name))
        self.race_text = self.add(npyscreen.FixedText, editable=False,
                                  value="Do not add racial bonuses, they will be added for you as listed.")
        for attr in attrs:
            if attr in self.parentApp.character.primary_class.primary_abilities:
                name = '**' + attr
            else:
                name = '' + attr
            race_bonus = getattr(self.parentApp.character.race,
                                 f'{attr}_bonus')
            if race_bonus != 0:
                name += '({:+d})'.format(race_bonus)
            name += ':'
            new_fld = self.add(npyscreen.TitleText, name=name,
                               begin_entry_at=24)
            setattr(self, attr, new_fld)
        self.add(npyscreen.FixedText, editable=False,
                 value="Maximum hit points initially determined by constitution.")
        self.max_hp = self.add(npyscreen.TitleText, name="Max HP:")

    def on_ok(self):
        super().to_next()
    
    def on_cancel(self):
        super().to_prev()


class SkillForm(LinkedListForm):
    def while_editing(self):
        # Update the static skills for race and background
        bg_skills = self.parentApp.character.background.skill_proficiencies
        self.bg_skills.value = str(bg_skills)[1:-1].replace("'", "")
        race_skills = self.parentApp.character.race.skill_proficiencies
        self.race_skills.value = str(race_skills)[1:-1].replace("'", "")
        # Now set the available discretionary choices
        choices = (self.parentApp.character.primary_class.class_skill_choices +
                   self.parentApp.character.race.skill_choices +
                   self.parentApp.character.background.skill_choices)
        static_skills = bg_skills + race_skills
        choices = set([c for c in choices if c.lower() not in static_skills])
        self.skill_proficiencies.set_values(sorted(tuple(choices)))
        self.update_remaining()
    
    def update_remaining(self, widget=None):
        num_choices = (self.parentApp.character.num_skill_choices +
                       self.parentApp.character.race.num_skill_choices +
                       self.parentApp.character.background.num_skill_choices)
        num_selected = len(self.skill_proficiencies.value)
        remaining = num_choices - num_selected
        log.debug(f'Remaining: {remaining}')
        self.remaining.value = str(remaining)
        self.display()
    
    def create(self):
        self.bg_skills = self.add(
            npyscreen.TitleText, name="Background:",
            value="", editable=False)
        self.race_skills = self.add(
            npyscreen.TitleText, name="Racial:",
            value="", editable=False)
        self.remaining = self.add(
            npyscreen.TitleText, name="Remaining:",
            value=0, editable=False)
        self.skill_proficiencies = self.add(
            npyscreen.TitleMultiSelect, name="Skill Proficiencies:",
            values=self.parentApp.character.class_skill_choices,
            value_changed_callback=self.update_remaining)
    
    def on_ok(self):
        new_skills = self.skill_proficiencies.get_selected_objects()
        if new_skills is not None:
            new_skills = tuple(s.lower() for s in new_skills)
        else:
            new_skills = ()
        bg_skills = tuple(self.parentApp.character.background.skill_proficiencies)
        race_skills = tuple(self.parentApp.character.race.skill_proficiencies)
        all_skills = new_skills + bg_skills + race_skills
        self.parentApp.character.skill_proficiencies = all_skills
        log.debug(f"Skill proficiencies: {all_skills}")
        super().to_next()
    
    def on_cancel(self):
        super().to_prev()


class SaveForm(LinkedListForm):
    def create(self):
        self.filename = self.add(
            npyscreen.TitleText, name='Filename:')
        self.make_pdf = self.add(npyscreen.Checkbox, name="Create PDF:", value=True)
        self.instructions = self.add(
            npyscreen.FixedText, editbale=False,
            value="After saving, edit this file to finish your personality, etc.")
    
    def on_ok(self):
        super().to_next()
    
    def on_cancel(self):
        super().to_prev()


def main():
    my_app = App()
    
    try:
        my_app.run()
    except KeyboardInterrupt:
        log.error("Aborted by user request")
    else:
        my_app.save_character()


if __name__ == '__main__':
    main()
