import json
import re

OUTFILE = 'spells_new.py'
INFILE = '/home/mwolf/Documents/dungeons_and_dragons/spells.json'

data = json.load(open(INFILE, mode='r'))

components_re = re.compile('([VSM])?[, ]*([VSM])?[, ]*([VSM])?[, ]*'
                           '(?:\(([-a-zA-Z ,.0-9;’—()]+)\))?')

def parse_components(string):
    result = components_re.match(string)
    components = tuple(r for r in result.groups()[0:3] if r is not None)
    materials = result.groups()[3]
    if 'M' in components:
        assert materials is not None
    if materials is None:
        materials = ''
    return components, materials

print(parse_components('V'))
print(parse_components('V, S'))
print(parse_components('S, V'))
print(parse_components("V, S, M (a tiny strip of white cloth)"))

with open(OUTFILE, mode='w') as out:

    for spell_name, spell in data.items():
        # Read the components list to determine which components there are
        class_name = ''.join([s.capitalize() for s in spell_name.split()])
        # Process the components
        try:
            components, materials = parse_components(spell["components"])
        except AssertionError:
            print(spell_name, spell)
        new_s = (f'class {class_name}(Spell):\n'
                 f'    """{spell["description"]}"""\n'
                 f'    name = "{spell_name}"\n'
                 f'    level = {spell["level"]}\n'
                 f'    casting_time = "{spell["casting_time"]}"\n'
                 f'    components = {components}\n'
                 f'    materials = "{materials}"\n'
                 f'    duration = "{spell["duration"]}"\n'
                 f'    magic_school = "{spell["school"].capitalize()}"\n'
                 f'    classes = ()\n'
                 '\n\n')
        # print(new_s)
        out.write(new_s)
