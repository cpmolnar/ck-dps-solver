import re

KEYS = {
            '%_damage': 0.,
            '%_physical_melee_damage': 0.,
            '%_physical_range_damage': 0.,
            '%_mining_damage': 0.,
            '%_melee_attack_speed': 0.,
            '%_range_attack_speed': 0.,
            '%_melee_and_range_attack_speed': 0.,
            '%_damage_against_bosses': 0.,
            '%_critical_hit_damage': 0.5,
            '%_critical_hit_chance': 0.,
            '%_triple_hit_chance': 0.,
            '+_fishing': 0.,
            '+_mining_damage': 0.,
            '+_thorns_damage': 0.,
}.keys()

item_category = 'Bag'
consider_for = 'Melee'
set = None

file_path = 'wiki_item.txt'
with open(file_path, 'r') as file:
    s = file.read()
    _, item_name,  _, attributes_txt = s.split('\t')
    item_name = item_name.replace('\'', '\\\'')
    attributes_list = attributes_txt.split('\n')
    keys = [('' if re.split('\d', attr)[-1].startswith('%') else '+') + re.split('\d', attr)[-1].replace(' ', '_') for attr in attributes_list]
    types = [re.search('(%)+|(\d)+ ', attr[1:])[0] for attr in attributes_list]
    values = [round(float(re.search('(\d)+(.\d)*', attr)[0])/(100 if type=='%' else 1), 4) for type, attr in zip(types, attributes_list)]

    set_string = ('        set=' + set + '\n') if set is not None else ''
    consider_for_string = '        consider_for=\'' + consider_for + '\',\n'
    attributes_string = '        attributes={\n'
    for key, value in zip(keys, values):
        if key in KEYS:
            attributes_string += f"            '{key}': {value},\n"
    attributes_string += '        }\n'

    print_string = f"'{item_name}': Item(\n        name='{item_name}',\n        item_category='{item_category}',\n{set_string}{consider_for_string}{attributes_string}    ),"
    print(print_string)
