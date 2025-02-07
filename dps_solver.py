from objects import Character
from items import *
from utils import calculate_dps, calculate_adjusted_weapon_damage

import itertools
import pandas as pd
from tqdm import tqdm

skill_levels = {
    'Mining':       95,
    'Running':      100,
    'Melee':        100,
    'Vitality':     100,
    'Crafting':     100,
    'Range':        100,
    'Gardening':    100,
    'Fishing':      100,
    'Cooking':      100,
    'Magic':        100,
    'Summoning':    100,
}

perk_trees = {
    'Mining':       [5, 5, 5, 5, 5, 0, 0, 0],
    'Running':      [5, 0, 5, 0, 0, 5, 0, 2],
    'Melee':        [5, 5, 5, 0, 5, 0, 0, 5],
    'Vitality':     [5, 5, 5, 0, 5, 0, 5, 0],
    'Crafting':     [5, 5, 5, 5, 0, 0, 5, 0],
    'Range':        [5, 5, 5, 0, 0, 5, 0, 5],
    'Gardening':    [5, 5, 0, 5, 5, 0, 0, 5],####
    'Fishing':      [5, 5, 0, 0, 5, 0, 5, 5],
    'Cooking':      [5, 5, 5, 5, 0, 5, 0, 0],
    'Magic':        [5, 0, 0, 0, 0, 0, 0, 0],
    'Summoning':    [0, 0, 5, 0, 0, 0, 0, 0],
}

food_effects = {
        '%_damage': {'(Food Effect) Food': 0.756},
        '%_physical_melee_damage': {'(Food Effect) Food': 0.579},
        '%_physical_range_damage': {'(Food Effect) Food': 0.423},
        '%_melee_attack_speed': {'(Food Effect) Food': 0.208},
        '%_range_attack_speed': {'(Food Effect) Food': 0.208},
        '%_melee_and_range_attack_speed': {'(Food Effect) Food': 0.17},
        '%_damage_against_bosses': {'(Food Effect) Food': 0.21},
        '%_critical_hit_damage': {'(Food Effect) Food': 0.62},
        '%_critical_hit_chance': {'(Food Effect) Food': 0.21},
        '+_fishing': {'(Food Effect) Food': 94.},
        '+_mining_damage': {'(Food Effect) Food': 516.},
        '+_thorns_damage': {'(Food Effect) Food': 75.},
}

potion_effects = {
        '%_damage': {'(Potion Effect) Potion': 0.4},
        '%_physical_melee_damage': {'(Potion Effect) Potion': 0.3},
        '%_physical_range_damage': {'(Potion Effect) Potion': 0.3},
        '%_critical_hit_chance': {'(Potion Effect) Potion': 0.11},
}

# display_damage_settings = {
#     'Well fed': True,
#     'Max health': True,
#     'Low health': False,
#     'Running stacks': False,
#     'Range stacks': False,
#     'Standing still': False,
#     'Melee stacks': False,
#     'Consumables active': False,
#     'Ate fish-derived food': False,
#     'Pyrdra soul': True
# }

if __name__=='__main__':
    character = Character(skill_levels, perk_trees, food_effects=food_effects, potion_effects=potion_effects, settings=None)
    damage_type = 'Melee'

    character.equip(WEAPONS['Galaxite Chakram' if damage_type=='Range' else 'Stormbringer'])
    character.equip(PETS['Pheromoth' if damage_type=='Range' else 'Owlux'])
    if damage_type=='Melee':
        character.equip(LANTERNS['None' if damage_type=='Range' else 'Orb Lantern'])
        character.equip(BAGS['None' if damage_type=='Range' else 'Morpha\'s Bubble Bag'])

    # results = pd.read_csv('outputs/melee_dps.csv')
    keys_list = get_keys_for_damage_type([HELMS, BREAST_ARMORS, PANTS_ARMORS, NECKLACES, RINGS, RINGS, OFFHANDS], damage_type)
    loadouts = list(itertools.product(*keys_list))
    results = {
                'Weapon': [], 'Helm': [], 'Breast armor': [], 'Pants armor': [], 'Necklace': [],
                'Ring1': [], 'Ring2': [], 'Offhand': [], 'Lantern': [], 'Bag': [], 'Pet': [], 'DPS': []
    }

    for loadout in tqdm(loadouts, desc='Composing loadouts...'):
        helm, breast_armor, pants_armor, necklace, ring1, ring2, offhand = loadout
        [
            results[item_category].append(item_name) for item_category, item_name in \
            [('Weapon', 'Galaxite Chakram' if damage_type=='Range' else 'Stormbringer'), 
            ('Helm', helm), 
            ('Breast armor', breast_armor), 
            ('Pants armor', pants_armor), 
            ('Necklace', necklace), 
            ('Ring1', ring1 if ring1 > ring2 else ring2), # Permutation invariance once duplicates are dropped
            ('Ring2', ring2 if ring1 > ring2 else ring1), 
            ('Offhand', offhand),
            ('Lantern', 'None' if damage_type=='Range' else 'Orb Lantern'), 
            ('Bag', 'None' if damage_type=='Range' else 'Morpha\'s Bubble Bag'), 
            ('Pet', 'Pheromoth' if damage_type=='Range' else 'Owlux'), 
            ('DPS', 'None')]
        ]
    results = pd.DataFrame.from_dict(results)
    results = results.drop_duplicates(subset=['Helm', 'Breast armor', 'Pants armor', 'Necklace', 'Ring1', 'Ring2', 'Offhand', 'Pet'])

    def calculate(row):
        character.unequip_items(except_categories=['Weapon', 'Pet', 'Lantern', 'Bag'])
        character.equip(HELMS[row['Helm']])
        character.equip(BREAST_ARMORS[row['Breast armor']])
        character.equip(PANTS_ARMORS[row['Pants armor']])
        character.equip(NECKLACES[row['Necklace']])
        character.equip(RINGS[row['Ring1']])
        character.equip(RINGS[row['Ring2']])
        character.equip(OFFHANDS[row['Offhand']])
        character.reinforce_items()
        return calculate_dps(character)

    tqdm.pandas(desc="Calculating DPS...")
    results['DPS'] = results.progress_apply(calculate, axis=1)

    results = results.sort_values(by=['DPS'], ascending=False)
    print(results.head(10))
    results.to_csv(f'outputs/{damage_type.lower()}_dps.csv')