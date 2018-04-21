#!/usr/bin/env python

"""Launch a system to interactively create a character."""

import logging
logging.basicConfig(filename='character_creater.log', level=logging.DEBUG)
log = logging.getLogger(__name__)

import math

import npyscreen
from random import randint

from dungeonsheets import character, race, dice

char_classes = {
    'Barbarian': character.Barbarian,
    'Bard': character.Bard,
    'Cleric': character.Cleric,
    'Druid': character.Druid,
    'Fighter': character.Fighter,
    'Monk': character.Monk,
    'Paladin': character.Paladin,
    'Ranger': character.Ranger,
    'Rogue': character.Rogue,
    'Sorceror': character.Sorceror,
    'Warlock': character.Warlock,
    'Wizard': character.Wizard
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
}


class App(npyscreen.NPSAppManaged):
    # STARTING_FORM = 'CLASS'
    character = None
    
    def save_character(self):
        pass
    
    @property
    def character_class(self, *args, **kwargs):
        return self.character_class
    
    @character_class.setter
    def character_class(self, NewClass):
        log.debug("Replacing character")
        basic_info = self.getForm('MAIN')
        self.character = NewClass(
            name=basic_info.name.value,
            player_name=basic_info.player_name.value,
            level=int(basic_info.level.value),
            strength=-1, dexterity=-1, constitution=-1,
            intelligence=-1, wisdom=-1, charisma=-1)
        self.update_max_hp()
        # Reset form widgets
        log.debug("Resetting forms")
        self.getForm('ABILITIES').reset()
    
    def update_max_hp(self):
        # Update max HP based on the class
        max_hp_fld = self.getForm('ABILITIES').max_hp
        if max_hp_fld.value == '':
            # Calculate the new value
            hit_dice = dice.read_dice_str(self.character.hit_dice)
            const = self.character.constitution.modifier
            max_hp = hit_dice.faces + const
            for d in range(hit_dice.num - 1):
                max_hp += math.ceil(hit_dice.faces/2) + const
            log.debug("Updating max hp: %d", max_hp)
            max_hp_fld.value = str(max_hp)
    
    def onStart(self):
        self.addForm("MAIN", BasicInfoForm, name="Basic Info:")
        self.addForm("CLASS", CharacterClassForm, name="Select your character's class:")
        self.addForm("RACE", RaceForm, name="Select your character's race:")
        self.addForm("ALIGNMENT", AlignmentForm, name="Select your character's alignment:")
        self.addForm("ABILITIES", AbilityScoreForm, name="Choose ability scores:")
        self.addForm("BACKGROUND", BackgroundForm, name="Choose background:")
        self.addForm("SAVE", SaveForm, name="Save character:")


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
        self.parentApp.setNextForm('BACKGROUND')
    
    def on_cancel(self):
        self.parentApp.setNextForm('ALIGNMENT')


class CharacterClassForm(npyscreen.ActionForm):
    def create(self):
        self.character_class = self.add(
            npyscreen.TitleMultiLine, name="Class:", values=tuple(char_classes.keys()))
    
    def on_ok(self):
        if self.character_class.value is not None:
            selected_class = self.character_class.values[self.character_class.value]
            selected_class = char_classes[selected_class]
            log.debug('Selected character class %s', selected_class.class_name)
            self.parentApp.character_class = selected_class
            self.parentApp.setNextForm('RACE')
    
    def on_cancel(self):
        self.parentApp.setNextForm('MAIN')


class BackgroundForm(npyscreen.ActionForm):
    backgrounds = ('Acolyte', 'Charlatan', 'Criminal', 'Entertainer',
                   'Folk hero', 'Guild Artison', 'Hermit', 'Noble', 'Knight',
                   'Outlander', 'Pirate', 'Sage', 'Sailor', 'Soldier', 'Urchin',)
    def create(self):
        self.background = self.add(npyscreen.TitleMultiLine,
                                   name="Background:", values=self.backgrounds)
    
    def on_ok(self):
        if self.background.value is not None:
            background = self.backgrounds[self.background.value]
            self.parentApp.character.background = background
            log.debug("Selected character background: %s", background)
            self.parentApp.setNextForm('SAVE')
    
    def on_cancel(self):
        self.parentApp.setNextForm('ABILITIES')


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
            self.parentApp.setNextForm('ABILITIES')
    
    def on_cancel(self):
        self.parentApp.setNextForm('RACE')


class BasicInfoForm(npyscreen.ActionForm):
    def create(self):
        self.name = self.add(
            npyscreen.TitleText, name="Character Name:", use_two_lines=False)
        self.player_name = self.add(
            npyscreen.TitleText, name="Player Name:", use_two_lines=False)
        self.level = self.add(
            npyscreen.TitleText, name='Level:', value="1")
    
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
        self.parentApp.setNextForm('CLASS')
    
    def on_cancel(self):
        self.parentApp.setNextForm('SAVE')


class SaveForm(npyscreen.ActionForm):
    def create(self):
        self.filename = self.add(
            npyscreen.TitleText, name='Filename:')
        self.make_pdf = self.add(npyscreen.Checkbox, name="Create PDF:", value=True)
    
    def on_ok(self):
        self.parentApp.setNextForm(None)
    
    def on_cancel(self):
        self.parentApp.setNextForm('BACKGROUND')


my_app = App()

try:
    my_app.run()
except KeyboardInterrupt:
    log.error("Aborted by user request")
else:
    my_app.save_character()
