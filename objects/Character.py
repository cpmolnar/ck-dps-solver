from . import Item, Weapon

class Character():
    def __init__(self, skill_levels: dict, perks: dict, items: dict = None, settings: dict = None, food_attributes = None):
        self.skill_levels = skill_levels
        
        perk_to_label = {
            'Mining':    ['Efficient excavation', 'Meticulous miner', 'Self-mending alloy', 'Miner\'s strength', 'Mine, mine, mine!', 'Explosives engineer', 'Pick and run!', 'Archaeologist'],
            'Running':   ['Endurance runner', 'Balanced stance', 'Gotta go fast!', 'On your toes', 'Escape artist', 'Keeping tempo', 'Encumbering presence', 'Breaking barriers'],
            'Melee':     ['Quick strikes', 'Building anger', 'Fast and furious', 'Heavy swings', 'Stubborn fighter', 'Taking a step back', 'Seething blade', 'Strength of the Ancients'],
            'Vitality':  ['Maxed out!', 'Strong and healthy', 'Desperate fighter', 'Stayin\' alive', 'Healing potency', 'Lingering potions', 'Protection of the Ancients', 'Cheat death'],
            'Crafting':  ['Base builder', 'The right tools in the right hands', 'High quality equipment', 'Alchemist', 'Industry specialist', 'Blacksmith', 'Jewelry crafter', 'Unbreakable'],
            'Range':     ['Rapid shots', 'Keeping momentum', 'Weakness detection', 'Slimy bullets', 'Charging in', 'Stun shot', 'Focused accuracy', 'Amplified precision'],
            'Gardening': ['Grateful gardener', 'Eat your vegetables!', 'Feast for the eyes', 'Thorny weapons', 'Thorny skin', 'Poison coated weapons', 'Expert gardener', 'Potent poison'],
            'Fishing':   ['Improved bait', 'Fisherman\'s luck', 'Angler\'s advantage', 'Studied patterns', 'Steady feet', 'Chewy bait', 'Well-trained aim', 'Power of Omega-3!'],
            'Cooking':   ['Utilizing every nutrient', 'Not so picky', 'Healthy diet', 'Fast food', 'Long-lasting food', 'The smell of food', 'Master chef', 'Sharing is caring'],
            'Magic':     ['True sight', 'Mana channeling', 'Firmly grounded', 'The best offense', 'Arcane frenzy', 'Arcane transfusion', 'Fully charged', 'Deep pool'],
            'Summoning': ['Ferocious creatures', 'Critical command', 'Power in numbers', 'Trickle down arcana', 'Tough gang', 'Group effort', 'Longing for this world', 'Proxy parasites'],
        }

        self.perks = {}
        for skill, tier_choices in perks.items():
            self.perks[skill] = {perk_to_label[skill][i]: v for i, v in enumerate(tier_choices)}
    
        self.reset_items()

        self.settings = {
            'Well fed': True,
            'Max health': True,
            'Low health': False,
            'Running stacks': True,
            'Range stacks': True,
            'Standing still': False,
            'Melee stacks': True,
            'Consumables active': True,
            'Ate fish-derived food': True,
            'Pyrdra defeated': True
        }

        if items is not None:
            for item_category, item in items:
                items[item_category] = item

        self.food_attributes = food_attributes

    def equip(self, item):
        if item.item_category=='Ring':
            self.items[item.item_category + ('1' if self.items['Ring1'] is None else '2')] = item
        else: 
            self.items[item.item_category] = item

    def reset_items(self): 
        self.items = {
            'Weapon': None, 'Helm': None, 'Breast armor': None, 'Pants armor': None, 'Necklace': None,
            'Ring1': None, 'Ring2': None, 'Offhand': None, 'Lantern': None, 'Bag': None, 'Pet': None,
        }

    def reinforce_items(self): [item.reinforce() for item in self.items.values() if item is not None]

    def printable_loadout(self): return ', '.join([item_name for item_name in self.items.keys() if item_name is not None])

    def get_item_stats(self):
        item_stats = {
            'attributes': {},
            'set': {},
        }

        for item in self.items.values():
            if item is not None:
                item_stats['set'][item.name] = item.set
                for attribute_name, value in item.attributes.items():
                    if attribute_name not in item_stats['attributes']: item_stats['attributes'][attribute_name] = 0.
                    item_stats['attributes'][attribute_name] += value

        item_stats['attributes']['%_damage'] += (0.25 if sum([item_set=='core_commander_set' for item_set in item_stats['set'].values()])>=2 else 0)
        item_stats['attributes']['%_damage'] += ((self.perks['Gardening']['Potent poison'] * 0.05) if (sum([item_set=='druidra\'s_ring' for item_set in item_stats['set'].values()])>=1) else 0)
        item_stats['attributes']['%_critical_hit_chance'] += (0.25 if (sum([item_set=='ivy\'s_set' for item_set in item_stats['set'].values()])>=2) & (sum([item_set=='druidra\'s_ring' for item_set in item_stats['set'].values()])>=1) else 0)
        
        return item_stats
    
    def get_character_attributes(self):
        character_attributes = {
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
        }

        character_attributes['%_damage'] += self.perks['Cooking']['The smell of food'] * 0.04
        character_attributes['%_damage'] += self.settings['Pyrdra defeated'] * 0.1
        if self.settings['Max health']:     character_attributes['%_damage'] += self.perks['Vitality']['Strong and healthy'] * 0.02
        if self.settings['Low health']:     character_attributes['%_damage'] += self.perks['Vitality']['Desperate fighter'] * 0.04
        if self.settings['Well fed']:       character_attributes['%_damage'] += (1 + (self.perks['Cooking']['Healthy diet']) * 0.2) * 0.05
        if self.settings['Running stacks']: character_attributes['%_damage'] += self.perks['Running']['Keeping tempo'] * 0.03

        character_attributes['%_critical_hit_chance'] += self.perks['Magic']['True sight'] * 0.01
        character_attributes['%_critical_hit_damage'] += self.perks['Gardening']['Thorny weapons'] * 0.05
        character_attributes['%_critical_hit_damage'] += self.perks['Range']['Amplified precision'] * 0.08

        character_attributes['%_damage_against_bosses'] += self.perks['Melee']['Strength of the Ancients'] * 0.05
        if self.settings['Ate fish-derived food']: character_attributes['%_damage_against_bosses'] += self.perks['Fishing']['Power of Omega-3!'] * 0.03

        character_attributes['+_thorns_damage'] += self.perks['Gardening']['Thorny skin'] * 10

        if self.items['Weapon'].damage_type=='Range':
            character_attributes['%_physical_range_damage'] += self.skill_levels['Range']/200
            if self.settings['Range stacks']:           character_attributes['%_physical_range_damage'] += self.perks['Range']['Keeping momentum'] * 2 * 0.02
            if self.settings['Standing still']:         character_attributes['%_physical_range_damage'] += self.perks['Range']['Focused accuracy'] * 0.05
            character_attributes['%_range_attack_speed'] += self.perks['Range']['Rapid shots'] * 0.02
            character_attributes['%_range_attack_speed'] += self.perks['Summoning']['Power in numbers'] * 0.02
            character_attributes['+_fishing'] += self.skill_levels['Fishing']
        if self.items['Weapon'].damage_type=='Melee':
            character_attributes['%_physical_melee_damage'] += self.skill_levels['Melee']/200
            if self.settings['Melee stacks']:           character_attributes['%_physical_melee_damage'] += self.perks['Melee']['Building anger'] * 2 * 0.02
            if self.settings['Melee stacks']:           character_attributes['%_physical_melee_damage'] += self.perks['Melee']['Stubborn fighter'] * 0.03
            character_attributes['%_melee_attack_speed'] += self.perks['Melee']['Quick strikes'] * 0.02
            character_attributes['+_mining_damage'] += self.skill_levels['Mining']


        return character_attributes

    def get_attributes(self):
        item_attributes = self.get_item_stats()['attributes']
        character_attributes = self.get_character_attributes()
        food_attributes = self.food_attributes if self.food_attributes is not None and self.settings['Consumables active'] else {k: 0. for k in character_attributes.keys()}

        attributes = {attribute_name: item_attributes[attribute_name] + character_attributes[attribute_name] + food_attributes[attribute_name] for attribute_name in character_attributes.keys()}

        return attributes