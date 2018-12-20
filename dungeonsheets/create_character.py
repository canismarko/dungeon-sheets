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


char_classes = {
    'Barbarian': classes.Barbarian,
    'Bard': classes.Bard,
    'Cleric': classes.Cleric,
    'Druid': classes.Druid,
    'Fighter': classes.Fighter,
    'Monk': classes.Monk,
    'Paladin': classes.Paladin,
    'Ranger': classes.Ranger,
    'Rogue': classes.Rogue,
    'Sorceror': classes.Sorceror,
    'Warlock': classes.Warlock,
    'Wizard': classes.Wizard
}

races = {
    'Hill Dwarf': race.HillDwarf,
    'Mountain Dwarf': race.MountainDwarf,
    'High Elf': race.HighElf,
    'Wood Elf': race.WoodElf,
    'Dark Elf': race.DarkElf,
    'Lightfoot Halfling': race.LightfootHalfling,
    'Stout Halfling': race.StoutHalfling,
    'Human': race.Human,
    'Dragonborn': race.Dragonborn,
    'Gnome': race.Gnome,
    'Forest Gnome': race.ForestGnome,
    'Rock Gnome': race.RockGnome,
    'Half-Elf': race.HalfElf,
    'Half-Orc': race.HalfOrc,
    'Tiefling': race.Tiefling,
    'Fallen Aasimar': race.FallenAasimar,
}


backgrounds = background.available_backgrounds
backgrounds = {bg.name: bg for bg in backgrounds}


class App(npyscreen.NPSAppManaged):
    # STARTING_FORM = 'SKILLS'
    character = None
    
    def save_character(self):
        # Save the file
        filename = self.getForm("SAVE").filename.value
        self.character.save(filename)
        # Create the PDF character sheet
        if self.getForm('SAVE').make_pdf.value:
            log.debug("Creating PDF")
            subprocess.call(['makesheets', filename])
            
    def add_class(self, NewClass):
        log.debug("Adding Class: {:s}".format(NewClass.class_name))
        # basic_info = self.getForm('MAIN')
        # self.character = NewClass(
        #     name=basic_info.name.value,
        #     player_name=basic_info.player_name.value,
        #     level=int(basic_info.level.value),
        #     strength=-1, dexterity=-1, constitution=-1,
        #     intelligence=-1, wisdom=-1, charisma=-1)
        self.character.class_list.append(NewClass)
        self.update_max_hp()
        # Reset form widgets
        log.debug("Resetting forms")
        self.getForm('ABILITIES').reset()
        
    # @property
    # def character_class(self, *args, **kwargs):
    #     return self.character_class
    
    # @character_class.setter
    # def character_class(self, NewClass):
    #     log.debug("Adding Class: {:s}".format(NewClass.class_name))
    #     # basic_info = self.getForm('MAIN')
    #     # self.character = NewClass(
    #     #     name=basic_info.name.value,
    #     #     player_name=basic_info.player_name.value,
    #     #     level=int(basic_info.level.value),
    #     #     strength=-1, dexterity=-1, constitution=-1,
    #     #     intelligence=-1, wisdom=-1, charisma=-1)
    #     self.character.class_list.append(NewClass)
    #     self.update_max_hp()
    #     # Reset form widgets
    #     log.debug("Resetting forms")
    #     self.getForm('ABILITIES').reset()
    
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
                for d in range(hd.num - 1):
                    max_hp += math.ceil(hd.faces/2) + const
            log.debug("Updating max hp: %d", max_hp)
            max_hp_fld.value = str(max_hp)
    
    def onStart(self):
        self.character = character.Character()
        self.addForm("MAIN", BasicInfoForm, name="Basic Info:")
        self.addForm("RACE", RaceForm, name="Select your character's race:")
        self.addForm("CLASS", CharacterClassForm, name="Select your character's primary class:")
        self.addForm("SUBCLASS", SubclassForm, name="Select your subclass:")
        self.addForm("BACKGROUND", BackgroundForm, name="Choose background:")
        self.addForm("ALIGNMENT", AlignmentForm, name="Select your character's alignment:")
        self.addForm("ABILITIES", AbilityScoreForm, name="Choose ability scores:")
        self.addForm("SKILLS", SkillForm, name="Choose skill proficiencies")
        self.addForm("SAVE", SaveForm, name="Save character:")


class BasicInfoForm(npyscreen.ActionForm):
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
        # Move to the next form
        self.parentApp.setNextForm('RACE')
    
    def on_cancel(self):
        raise KeyboardInterrupt

    
class RaceForm(npyscreen.ActionForm):
    def create(self):
        self.race = self.add(
            npyscreen.TitleMultiLine, name="Race:", values=tuple(races.keys()))
    
    def on_ok(self):
        if self.race.value is not None:
            selected_race = self.race.values[self.race.value]
            SelectedRace = races[selected_race]
            log.debug('Selected character race: %s', SelectedRace.name)
            self.parentApp.character.race = SelectedRace()
            self.parentApp.setNextForm('CLASS')
    
    def on_cancel(self):
        self.parentApp.setNextForm('MAIN')
        

class CharacterClassForm(npyscreen.ActionForm):
    char_options = list(char_classes.keys())
    
    def create(self):
        self.level = self.add(
            npyscreen.TitleText, name='Level:', value="1", use_two_lines=False)
        self.subclass = self.add(npyscreen.Checkbox, name="Choose a Subclass?", value=False)
        self.multiclass = self.add(npyscreen.Checkbox, name="Multiclass?", value=False)
        self.character_class = self.add(
            npyscreen.TitleMultiLine, name="Class:", values=tuple(self.char_options))

    def setup_multiclass(self):
        self.character_class.values = self.char_options
        self.name = "Select your character's class #{:d}".format(1 + self.parentApp.character.num_classes)
        self.multiclass.name = "Add another class?"
        self.level.value = '1'
        self.subclass.value = False
        self.multiclass.value = False
        self.character_class.value = None
        
    def on_ok(self):
        if self.character_class.value is not None:
            # make sure this option can't be selected again
            selected_class = self.character_class.values[self.character_class.value]
            self.char_options.remove(selected_class)
            selected_class = char_classes[selected_class]
            log.debug('Selected character class %s', selected_class.class_name)
            if self.subclass.value:
                sc = self.parentApp.getForm('SUBCLASS')
                sc.when_done = 'CLASS' if self.multiclass.value else 'BACKGROUND'
                if self.multiclass:
                    self.setup_multiclass()
                sc.prepare_for_class(selected_class, int(self.level.value))
                self.parentApp.setNextForm('SUBCLASS')
            else:
                self.parentApp.add_class(selected_class(level=int(self.level.value),
                                                        subclass=None))
                if self.multiclass.value:
                    self.setup_multiclass()
                    self.parentApp.setNextForm('CLASS')
                else:
                    self.parentApp.setNextForm('BACKGROUND')
    
    def on_cancel(self):
        if self.parentApp.character.num_classes > 1:
            self.parentApp.setNextForm('BACKGROUND')
        self.parentApp.setNextForm('RACE')


class SubclassForm(npyscreen.ActionForm):
    subclass_options = ('None',)
    parent_class = None
    level = 1
    when_done = 'BACKGROUND'
    name_formatter = "Select your {:s} subclass:"
    
    def create(self):
        self.subclass = self.add(
            npyscreen.TitleMultiLine, name="Subclass:",
            values=tuple(self.subclass_options))

    def prepare_for_class(self, parent_class, level):
        self.subclass_options = parent_class.subclasses_available or ('None',)
        self.parent_class = parent_class
        self.level = level
        self.name = self.name_formatter.format(parent_class.class_name)
        self._clear_all_widgets()
        self.create()
        
    def on_ok(self):
        if self.subclass.value in [None, '', 'None']:
            newclass = self.parent_class(level=self.level,
                                         subclass=None)
        else:
            newclass = self.parent_class(level=self.level,
                                         subclass=self.subclass.value)
        self.parentApp.add_class(newclass)
        self.parentApp.setNextForm(self.when_done)
    
    def on_cancel(self):
        self.parentApp.setNextForm('CLASS')


class BackgroundForm(npyscreen.ActionForm):

    def create(self):
        self.background = self.add(
            npyscreen.TitleMultiLine,
            name="Background:", values=tuple(backgrounds.keys()))
    
    def on_ok(self):
        if self.background.value is not None:
            selected_bg = self.background.values[self.background.value]
            Background = backgrounds[selected_bg]
            self.parentApp.character.background = Background()
            # Update the languages based on background and race
            race_languages = self.parentApp.character.race.languages
            languages = Background.languages + race_languages
            self.parentApp.character.languages = ', '.join(languages)
            log.debug("Selected character background: %s", Background.name)
            self.parentApp.setNextForm('ALIGNMENT')
    
    def on_cancel(self):
        self.parentApp.setNextForm('CLASS')


class AlignmentForm(npyscreen.ActionForm):
    """Choose your character's alignment."""
    alignments = ('Lawful good', 'Neutral good', 'Chaotic good',
                  'Lawful neutral', 'True neutral', 'Chaotic neutral',
                  'Lawful evil', 'Neutral evil', 'Chaotic evil', )
    
    def create(self):
        self.alignment = self.add(
            npyscreen.TitleMultiLine, name="Alignment:", values=self.alignments)
    
    def on_ok(self):
        if self.alignment.value is not None:
            selected_alignment = self.alignment.values[self.alignment.value]
            log.debug('Selected character alignment %s', selected_alignment)
            self.parentApp.character.alignment = selected_alignment
            self.parentApp.setNextForm('ABILITIES')
    
    def on_cancel(self):
        self.parentApp.setNextForm('BACKGROUND')


class AbilityScoreForm(npyscreen.ActionForm):
    def roll_dice(self):
        """Get six ability scores that can then be assigned to abilities.""" 
        def roll_score():
            # Roll 4 dice and add the 3 highest
            rolls = (randint(1, 6) for i in range(4))
            score = sum(sorted(rolls)[-3:])
            return score
        scores = (roll_score() for i in range(6))
        return tuple(sorted(scores, reverse=True))
    
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
                race_bonus = getattr(self.parentApp.character.race, f'{attr}_bonus')
                val = int(float(fld.value))
            except ValueError:
                # Not an integer, so clear the field
                fld.value = ''
            else:
                # Valid number, so process it
                curr_val = getattr(self.parentApp.character, attr).value
                if val != curr_val:
                    log.debug("Setting %s to %s", attr, str(val))
                    setattr(self.parentApp.character, attr, val)
                    # Update the "character" with new values
                    if attr == 'constitution':
                        self.parentApp.update_max_hp()
                        fld.value = str(val)
        # Update the form display
        self.display()
        
    def create(self):
        self.score_options = self.add(
            npyscreen.TitleFixedText, name="Rolls:", editable=False,
            value=str(self.roll_dice())[1:-1])
        self.add(npyscreen.FixedText, editable=False,
                 value="Take the six rolls and assign each one to an ability.")
        self.add(npyscreen.FixedText, editable=False,
                 value="Do not add racial bonuses, they will be added for you.")
        self.strength = self.add(npyscreen.TitleText, name="Strength:")
        self.dexterity = self.add(npyscreen.TitleText, name="Dexterity:")
        self.constitution = self.add(npyscreen.TitleText, name="Constitution:")
        self.intelligence = self.add(npyscreen.TitleText, name="Intelligence:")
        self.wisdom = self.add(npyscreen.TitleText, name="Wisdom:")
        self.charisma = self.add(npyscreen.TitleText, name="Charisma:")
        self.add(npyscreen.FixedText, editable=False,
                 value="Maximum hit points initially determined by constitution.")
        self.max_hp = self.add(npyscreen.TitleText, name="Max HP:")
    
    def on_ok(self):
        self.parentApp.setNextForm('SKILLS')
    
    def on_cancel(self):
        self.parentApp.setNextForm('ALIGNMENT')


class SkillForm(npyscreen.ActionForm):
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
        self.skill_proficiencies.set_values(tuple(choices))
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
        self.parentApp.setNextForm('SAVE')
    
    def on_cancel(self):
        self.parentApp.setNextForm('ABILITIES')


class SaveForm(npyscreen.ActionForm):
    def create(self):
        self.filename = self.add(
            npyscreen.TitleText, name='Filename:')
        self.make_pdf = self.add(npyscreen.Checkbox, name="Create PDF:", value=True)
        self.instructions = self.add(
            npyscreen.FixedText, editbale=False,
            value="After saving, edit this file to finish your personality, etc.")
    
    def on_ok(self):
        self.parentApp.setNextForm(None)
    
    def on_cancel(self):
        self.parentApp.setNextForm('SKILLS')


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
