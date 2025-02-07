from objects import Weapon, Item

WEAPONS = {
    'Galaxite Chakram': Weapon(
        name='Galaxite Chakram',
        min_damage=144, 
        max_damage=176, 
        attacks_per_second=2.5,
        damage_type='Range',
        consider_for='Range',
        attributes={
            '%_critical_hit_damage': 0.50
        }
    ),
    'Stormbringer': Weapon(
        name='Stormbringer',
        min_damage=84, 
        max_damage=102, 
        attacks_per_second=5,
        damage_type='Melee',
        consider_for='Melee',
        attributes={
            '+_mining_damage': 1000
        },
        has_durability=False
    ),
}

HELMS = {
    'Hivebone Helm': Item(
        name='Hivebone Helm',
        item_category='Helm',
        consider_for='Both',
        attributes={
            '%_melee_and_range_attack_speed': 0.068,
            '+_thorns_damage': 24.0,
        }
    ),
    'Slime Helm': Item(
        name='Slime Helm',
        item_category='Helm',
        consider_for='Both',
        attributes={
            '%_damage': 0.122,
        }
    ),
    'Diving Helm': Item(
        name='Diving Helm',
        item_category='Helm',
        set='fishing_set',
        consider_for='Range',
        attributes={'+_fishing': 59}
    ),
    'Scarab Visor': Item(
        name='Scarab Visor',
        item_category='Helm',
        set='scarab_set',
        consider_for='Both',
        attributes={'+_thorns_damage': 32}
    ),
    'Omoroth\'s Helm': Item(
        name='Omoroth\'s Helm',
        item_category='Helm',
        consider_for='Both',
        attributes={
            '%_damage': 0.078,
            '%_melee_and_range_attack_speed': 0.066,
        }
    ),
    'Miner\'s Protective Helm': Item(
        name='Miner\'s Protective Helm',
        item_category='Helm',
        set='mining_set',
        consider_for='Melee',
        attributes={
            '%_mining_damage': 0.17,
        }
    ),
    'Cosmos Visor Helm': Item(
        name='Cosmos Visor Helm',
        item_category='Helm',
        consider_for='Melee',
        attributes={
            '%_damage': 0.111,
            '+_mining_damage': 81.0,
        }
    ),
    'Atlantean Worm Helmet': Item(
        name='Atlantean Worm Helmet',
        item_category='Helm',
        consider_for='Both',
        attributes={
            '%_melee_and_range_attack_speed': 0.179,
            '%_critical_hit_chance': 0.06,
            '%_critical_hit_damage': 0.2
        }
    ),
    'Core Commander Helm': Item(
        name='Core Commander Helm',
        item_category='Helm',
        set='core_commander_set',
        consider_for='Both',
        attributes={
            '%_melee_and_range_attack_speed': 0.078,
            '%_damage': 0.07,
            '%_critical_hit_chance': 0.04,
        }
    ),
}

BREAST_ARMORS = {
    'Hunter Cloak': Item(
        name='Hunter Cloak',
        item_category='Breast armor',
        consider_for='Range',
        attributes={
            '%_physical_range_damage': 0.206,
        }
    ),
    'Slime Armor': Item(
        name='Slime Armor',
        item_category='Breast armor',
        consider_for='Both',
        attributes={
            '%_damage': 0.181,
        }
    ),
    'Hivebone Breastplate': Item(
        name='Hivebone Breastplate',
        item_category='Breast armor',
        consider_for='Both',
        attributes={
            '%_melee_and_range_attack_speed': 0.1,
            '+_thorns_damage': 22.0,
        }
    ),
    'Ivy\'s Thorn Harness': Item(
        name='Ivy\'s Thorn Harness',
        item_category='Breast armor',
        set='ivy\'s_set',
        consider_for='Both',
        attributes={
            '%_critical_hit_damage': 0.48,
        }
    ),
    'Miner\'s Labour Suit': Item(
        name='Miner\'s Labour Suit',
        item_category='Breast armor',
        set='mining_set',
        consider_for='Melee',
        attributes={
            '%_mining_damage': 0.23,
        }
    ),
    'Cosmos Torso': Item(
        name='Cosmos Torso',
        item_category='Breast armor',
        consider_for='Melee',
        attributes={
            '%_damage': 0.116,
            '+_mining_damage': 96.0,
        }
    ),
    'Scarab Harness': Item(
        name='Scarab Harness',
        item_category='Breast armor',
        set='scarab_set',
        consider_for='Both',
        attributes={'+_thorns_damage': 40}
    ),
    'Omoroth\'s Chestplate': Item(
        name='Omoroth\'s Chestplate',
        item_category='Breast armor',
        consider_for='Both',
        attributes={
            '%_damage': 0.101,
            '%_melee_and_range_attack_speed': 0.086
        }
    ),
    'Core Commander Brigandine': Item(
        name='Core Commander Brigandine',
        item_category='Breast armor',
        set='core_commander_set',
        consider_for='Both',
        attributes={
            '%_melee_and_range_attack_speed': 0.1,
            '%_damage': 0.073,
            '%_critical_hit_damage': 0.11,
        }
    ),
}

PANTS_ARMORS = {
    'Bronze Pants': Item(
        name='Bronze Pants',
        item_category='Pants armor',
        consider_for='Range',
        attributes={
            '%_physical_range_damage': 0.189,
        }
    ),
    'Iron Pants': Item(
        name='Iron Pants',
        item_category='Pants armor',
        consider_for='Both',
        attributes={
            '%_damage': 0.142,
        }
    ),
    'Miner\'s Worker Pants': Item(
        name='Miner\'s Worker Pants',
        item_category='Pants armor',
        set='mining_set',
        consider_for='Melee',
        attributes={
            '+_mining_damage': 120.0,
        }
    ),
    'Cosmos Legwear': Item(
        name='Cosmos Legwear',
        item_category='Pants armor',
        consider_for='Melee',
        attributes={
            '%_damage': 0.118,
            '+_mining_damage': 85.0,
        }
    ),
    'Scarab Legs': Item(
        name='Scarab Legs',
        item_category='Pants armor',
        set='scarab_set',
        consider_for='Both',
        attributes={'+_thorns_damage': 37}
    ),
    'Omoroth\'s Leg Armor': Item(
        name='Omoroth\'s Leg Armor',
        item_category='Pants armor',
        consider_for='Both',
        attributes={
            '%_damage': 0.092,
            '%_melee_and_range_attack_speed': 0.08
        }
    ),
    'Hivebone Pants': Item(
        name='Hivebone Pants',
        item_category='Pants armor',
        consider_for='Both',
        attributes={
            '%_melee_and_range_attack_speed': 0.089,
            '+_thorns_damage': 21.0,
        }
    ),
    'Ivy\'s Pants': Item(
        name='Ivy\'s Pants',
        item_category='Pants armor',
        set='ivy\'s_set',
        consider_for='Both',
        attributes={
            '%_critical_hit_damage': 0.47,
        }
    ),
    'Core Commander Greaves': Item(
        name='Core Commander Greaves',
        item_category='Pants armor',
        set='core_commander_set',
        consider_for='Both',
        attributes={
            '%_melee_and_range_attack_speed': 0.086,
            '%_critical_hit_damage': 0.11,
            '%_critical_hit_chance': 0.04,
        }
    ),
}

NECKLACES = {
    'Polished Copper Cross Necklace': Item(
        name='Polished Copper Cross Necklace',
        item_category='Necklace',
        consider_for='Both',
        attributes={
            '%_critical_hit_chance': 0.08,
            '%_critical_hit_damage': 0.25,
        }
    ),
    'Polished Octarine Necklace': Item(
        name='Polished Octarine Necklace',
        item_category='Necklace',
        consider_for='Both',
        attributes={
            '%_melee_and_range_attack_speed': 0.105,
        }
    ),
    'Neptune Necklace': Item(
        name='Neptune Necklace',
        item_category='Necklace',
        set='fishing_set',
        consider_for='Range',
        attributes={'+_fishing': 125}
    ),
    'Mold Vein Necklace': Item(
        name='Mold Vein Necklace',
        item_category='Necklace',
        consider_for='Range',
        attributes={'%_physical_range_damage': 0.389}
    ),
    'Torc Necklace': Item(
        name='Torc Necklace',
        item_category='Necklace',
        consider_for='Both',
        attributes={
            '%_damage': 0.249,
        }
    ),
    'Rusted Necklace': Item(
        name='Rusted Necklace',
        item_category='Necklace',
        consider_for='Melee',
        attributes={
            '%_mining_damage': 0.35,
        }
    ),
    'Black Necklace': Item(
        name='Black Necklace',
        item_category='Necklace',
        set='mining_set',
        consider_for='Melee',
        attributes={
            '+_mining_damage': 107.0,
        }
    ),
    'Ancient Gem Necklace': Item(
        name='Ancient Gem Necklace',
        item_category='Necklace',
        set='ancient_gem_set',
        consider_for='Melee',
        attributes={
            '%_melee_attack_speed': 0.049,
        }
    ),
    'Tower Shell Necklace': Item(
        name='Tower Shell Necklace',
        item_category='Necklace',
        consider_for='Melee',
        attributes={
            '+_mining_damage': 230.0,
        }
    ),
    'Ra-Akar\'s Necklace': Item(
        name='Ra-Akar\'s Necklace',
        item_category='Necklace',
        set='scarab_set',
        consider_for='Both',
        attributes={'+_thorns_damage': 19}
    ),
    'Glass Bead Necklace': Item(
        name='Glass Bead Necklace',
        item_category='Necklace',
        consider_for='Both',
        attributes={
            '%_critical_hit_damage': 0.82,
        }
    ),
}

RINGS = {
    'Sea Foam Ring': Item(
        name='Sea Foam Ring',
        item_category='Ring',
        consider_for='Range',
        attributes={'+_fishing': 106}
    ),
    'Gold Crystal Ring': Item(
        name='Gold Crystal Ring',
        item_category='Ring',
        consider_for='Range',
        attributes={'%_physical_range_damage': 0.416}
    ),
    'Ring of Stone': Item(
        name='Ring of Stone',
        item_category='Ring',
        consider_for='Melee',
        attributes={
            '+_mining_damage': 251.0,
        }
    ),
    'Ancient Gem Ring': Item(
        name='Ancient Gem Ring',
        item_category='Ring',
        set='ancient_gem_set',
        consider_for='Melee',
        attributes={
            '%_critical_hit_damage': 0.23,
            '+_mining_damage': 121.0,
        }
    ),
    'Topaz Ring': Item(
        name='Topaz Ring',
        item_category='Ring',
        consider_for='Melee',
        attributes={
            '%_mining_damage': 0.39,
        }
    ),
    'Black Ring': Item(
        name='Black Ring',
        item_category='Ring',
        set='mining_set',
        consider_for='Melee',
        attributes={
            '+_mining_damage': 74.0,
        }
    ),
    'Polished Gold Crystal Ring': Item(
        name='Polished Gold Crystal Ring',
        item_category='Ring',
        consider_for='Range',
        attributes={'%_physical_range_damage': 0.281,
                    '%_range_attack_speed': 0.052}
    ),
    'Polished Golden Spike Ring': Item(
        name='Polished Golden Spike Ring',
        item_category='Ring',
        consider_for='Both',
        attributes={'%_critical_hit_chance': 0.09,
                    '%_critical_hit_damage': 0.29,
                    '+_thorns_damage': 26}
    ),
    'Goldfish Ring': Item(
        name='Goldfish Ring',
        item_category='Ring',
        consider_for='Range',
        set='fishing_set'
    ),
    'Druidra\'s Ring': Item(
        name='Druidra\'s Ring',
        item_category='Ring',
        set='druidra\'s_ring',
        consider_for='Both',
        attributes={
            '%_critical_hit_damage': 0.14,
            '%_damage': 0.17,
        }
    ),
    'Ivy\'s Ring': Item(
        name='Ivy\'s Ring',
        item_category='Ring',
        set='ivy\'s_set',
        consider_for='Range',
        attributes={
            '%_range_attack_speed': 0.087,
        }
    ),
    'Glass Bead Ring': Item(
        name='Glass Bead Ring',
        item_category='Ring',
        consider_for='Both',
        attributes={
            '%_damage': 0.351
        }
    ),
    'Double Ring': Item(
        name='Double Ring',
        item_category='Ring',
        consider_for='Both',
        attributes={
            '%_damage': 0.072,
            '%_melee_and_range_attack_speed': 0.044,
            '%_critical_hit_chance': 0.04,
            '%_critical_hit_damage': 0.11,
        }
    ),
    'Morpha\'s Ring': Item(
        name='Morpha\'s Ring',
        item_category='Ring',
        consider_for='Both',
        attributes={
            '%_critical_hit_damage': 0.49,
        }
    ),
    'Wooden Thorn Ring': Item(
        name='Wooden Thorn Ring',
        item_category='Ring',
        consider_for='Both',
        attributes={
            '+_thorns_damage': 41.0,
        }
    ),
    'Skull Ring': Item(
        name='Skull Ring',
        item_category='Ring',
        consider_for='Both',
        attributes={
            '%_melee_and_range_attack_speed': 0.165,
        }
    ),
}

BAGS = {
    'Morpha\'s Bubble Bag': Item(
        name='Morpha\'s Bubble Bag',
        item_category='Bag',
        consider_for='Melee',
        attributes={
            '%_mining_damage': 0.19,
        }
    ),
}

LANTERNS = {
    'Orb Lantern': Item(
        name='Orb Lantern',
        item_category='Lantern',
        consider_for='Melee',
        attributes={
            '%_mining_damage': 0.19,
        }
    ),
}

OFFHANDS = {
    'Omoroth\'s Beak': Item(
        name='Omoroth\'s Beak',
        item_category='Offhand',
        consider_for='Melee',
        attributes={
            '%_physical_melee_damage': 0.385,
        }
    ),
    'Core Iris': Item(
        name='Core Iris',
        item_category='Offhand',
        consider_for='Melee',
        attributes={
            '+_mining_damage': 84.0,
        }
    ),
    'Octarine Shield': Item(
        name='Octarine Shield',
        item_category='Offhand',
        consider_for='Melee',
        attributes={
            '%_melee_and_range_attack_speed': 0.047,
        },
        has_durability=True
    ),
    'Concealed Blade': Item(
        name='Concealed Blade',
        item_category='Offhand',
        consider_for='Melee',
        attributes={
            '%_critical_hit_chance': 0.12,
        }
    ),
    'Crystal Meteor Chunk': Item(
        name='Crystal Meteor Chunk',
        item_category='Offhand',
        consider_for='Melee',
        attributes={
            '%_damage': 0.286,
        }
    ),
    'Hydra Tooth': Item(
        name='Hydra Tooth',
        item_category='Offhand',
        consider_for='Range',
        attributes={
            '%_triple_hit_chance': 0.05,
            '%_physical_range_damage': 0.288,
        }
    ),
}

PETS = {
    'Pheromoth': Item(
        name='Pheromoth',
        item_category='Pet',
        consider_for='Range',
        attributes={
            '%_physical_range_damage': 0.093,
            '%_triple_hit_chance': 0.1,
        }
    ),
    'Owlux': Item(
        name='Owlux',
        item_category='Pet',
        consider_for='Melee',
        attributes={
            '%_damage': 0.065,
            '%_triple_hit_chance': 0.1,
        }
    ),
}

def get_keys_for_damage_type(items_list, damage_type):
    return [[k for k, v in items.items() if v.consider_for==damage_type or v.consider_for=='Both'] for items in items_list]