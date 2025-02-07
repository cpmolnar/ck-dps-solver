from . import Item, Weapon

ACTIVE_EFFECTS_DICT = {
    '%_damage': {},
    '%_physical_melee_damage': {},
    '%_physical_range_damage': {},
    '%_mining_damage': {},
    '%_melee_attack_speed': {},
    '%_range_attack_speed': {},
    '%_melee_and_range_attack_speed': {},
    '%_damage_against_bosses': {},
    '%_critical_hit_damage': {},
    '%_critical_hit_chance': {},
    '%_triple_hit_chance': {},
    '+_fishing': {},
    '+_mining_damage': {},
    '+_thorns_damage': {},
}
class Character():
    def __init__(self, skill_levels: dict, perks: dict, items: dict = None, food_effects = None, potion_effects = None, settings: dict = None):
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
    
        self.items = {
            'Weapon': None, 'Helm': None, 'Breast armor': None, 'Pants armor': None, 'Necklace': None,
            'Ring1': None, 'Ring2': None, 'Offhand': None, 'Lantern': None, 'Bag': None, 'Pet': None,
        }

        self.settings = settings if settings is not None else {
            'Well fed': True,
            'Max health': True,
            'Low health': False,
            'Running stacks': True,
            'Range stacks': True,
            'Standing still': False,
            'Melee stacks': True,
            'Consumables active': True,
            'Ate fish-derived food': True,
            'Pyrdra soul': True
        }

        if items is not None:
            for item_category, item in items.items():
                self.items[item_category] = item

        self.food_effects = food_effects
        self.potion_effects = potion_effects

    def equip(self, item):
        if item.item_category=='Ring':
            self.items[item.item_category + ('1' if self.items['Ring1'] is None else '2')] = item
        else: 
            self.items[item.item_category] = item

    def unequip_items(self, except_categories=[]):
        for item_category in [ic for ic in self.items.keys() if ic not in except_categories]:
            self.items[item_category] = None

    def reinforce_items(self): [item.reinforce() for item in self.items.values() if item is not None]

    def printable_loadout(self): return ', '.join([item_name for item_name in self.items.keys() if item_name is not None])

    def get_consumables_active_effects(self):
        active_effects = ACTIVE_EFFECTS_DICT.copy()
        if self.settings['Consumables active']:
            if self.food_effects is not None:
                [self.update_effect(active_effects[k], *item) for k in self.food_effects.keys() for item in self.food_effects[k].items()]
            if self.potion_effects is not None:
                [self.update_effect(active_effects[k], *item) for k in self.potion_effects.keys() for item in self.potion_effects[k].items()]

        return active_effects

    def get_item_active_effects(self, return_set=True):
        active_effects = ACTIVE_EFFECTS_DICT.copy()
        set_keywords = {}
        for item in self.items.values():
            if item is not None:
                set_keywords.update({item.name: item.set})
                for attribute_name, value in item.attributes.items():
                    self.update_effect(active_effects[attribute_name], f'(Item Effect) {item.name}', value)
        self.update_effect(active_effects['%_damage'], '(Item Effect) Druidra\'s Ring', self.perks['Gardening']['Potent poison'] * 0.05 if sum([item_set=='druidra\'s_ring' for item_set in set_keywords.values()])>=1 else 0)
        self.update_effect(active_effects['%_damage'], '(Set Effect) Core Commander Set', 0.25 if sum([item_set=='core_commander_set' for item_set in set_keywords.values()])>=2 else 0)
        self.update_effect(active_effects['%_critical_hit_chance'], '(Set Effect) Ivy\'s Set', 0.25 if (sum([item_set=='ivy\'s_set' for item_set in set_keywords.values()])>=2) & (sum([item_set=='druidra\'s_ring' for item_set in set_keywords.values()])>=1) else 0)
        
        if return_set: return active_effects, set_keywords
        return active_effects
    
    def get_character_active_effects(self):
        active_effects = ACTIVE_EFFECTS_DICT.copy()

        self.update_effect(active_effects['%_damage'], '(Cooking Perk) The smell of food', self.perks['Cooking']['The smell of food'] * 0.04)
        self.update_effect(active_effects['%_damage'], '(Setting) Pyrdra soul', self.settings['Pyrdra soul'] * 0.1)
        self.update_effect(active_effects['%_damage'], '(Vitality Perk) Strong and healthy', self.perks['Vitality']['Strong and healthy'] * 0.02 if self.settings['Max health'] else 0)
        self.update_effect(active_effects['%_damage'], '(Vitality Perk) Desperate fighter', self.perks['Vitality']['Desperate fighter'] * 0.04 if self.settings['Low health'] else 0)
        self.update_effect(active_effects['%_damage'], '(Cooking Perk) Healthy diet', (1 + (self.perks['Cooking']['Healthy diet']) * 0.2) * 0.05 if self.settings['Well fed'] else 0)
        self.update_effect(active_effects['%_damage'], '(Running Perk) Keeping tempo', self.perks['Running']['Keeping tempo'] * 0.03 if self.settings['Running stacks'] else 0)
        self.update_effect(active_effects['%_critical_hit_chance'], '(Magic Perk) True sight', self.perks['Magic']['True sight'] * 0.01)
        self.update_effect(active_effects['%_critical_hit_damage'], '(Base Effect) Base', 0.5)
        self.update_effect(active_effects['%_critical_hit_damage'], '(Gardening Perk) Thorny weapons', self.perks['Gardening']['Thorny weapons'] * 0.05)
        self.update_effect(active_effects['%_critical_hit_damage'], '(Range Perk) Amplified precision', self.perks['Range']['Amplified precision'] * 0.08)
        self.update_effect(active_effects['%_damage_against_bosses'], '(Melee Perk) Strength of the Ancients', self.perks['Melee']['Strength of the Ancients'] * 0.05)
        self.update_effect(active_effects['%_damage_against_bosses'], '(Fishing Perk) Power of Omega-3!', self.perks['Fishing']['Power of Omega-3!'] * 0.03 if self.settings['Ate fish-derived food'] else 0)
        self.update_effect(active_effects['+_thorns_damage'], '(Gardening Perk) Thorny skin', self.perks['Gardening']['Thorny skin'] * 10)

        if self.items['Weapon'].damage_type=='Range':
            self.update_effect(active_effects['%_physical_range_damage'], '(Range Skill) Skill level bonus', self.skill_levels['Range']/200)
            self.update_effect(active_effects['%_physical_range_damage'], '(Range Perk) Keeping momentum', self.perks['Range']['Keeping momentum'] * 2 * 0.02 if self.settings['Range stacks'] else 0)
            self.update_effect(active_effects['%_physical_range_damage'], '(Range Perk) Focused accuracy', self.perks['Range']['Focused accuracy'] * 0.05 if self.settings['Standing still'] else 0)
            self.update_effect(active_effects['%_range_attack_speed'], '(Range Perk) Rapid shots', self.perks['Range']['Rapid shots'] * 0.02)
            self.update_effect(active_effects['%_range_attack_speed'], '(Summoning Perk) Power in numbers', self.perks['Summoning']['Power in numbers'] * 0.02 if self.settings['Summon active'] else 0)
            self.update_effect(active_effects['+_fishing'], '(Fishing Skill) Skill level bonus', self.skill_levels['Fishing'])
        if self.items['Weapon'].damage_type=='Melee':
            self.update_effect(active_effects['%_physical_melee_damage'], '(Melee Skill) Skill level bonus', self.skill_levels['Melee']/200)
            self.update_effect(active_effects['%_physical_melee_damage'], '(Melee Perk) Building anger', self.perks['Melee']['Building anger'] * 2 * 0.02 if self.settings['Melee stacks'] else 0)
            self.update_effect(active_effects['%_physical_melee_damage'], '(Melee Perk) Stubborn fighter', self.perks['Melee']['Stubborn fighter'] * 0.03 if self.settings['Melee stacks'] else 0)
            self.update_effect(active_effects['%_melee_attack_speed'], '(Melee Perk) Quick strikes', self.perks['Melee']['Quick strikes'] * 0.02)
            self.update_effect(active_effects['+_mining_damage'], '(Mining Skill) Skill level bonus', self.skill_levels['Mining'])
            self.update_effect(active_effects['+_mining_damage'], '(Base Effect) Base', 20)
            self.update_effect(active_effects['%_mining_damage'], '(Mining Perk) Efficient excavation', self.perks['Mining']['Efficient excavation'] * 0.02)

        return active_effects
    

    def update_effect(self, effect: dict, key: str, value): 
        if value != 0: effect.update({key: value})


    def get_active_effects(self):
        active_effects = ACTIVE_EFFECTS_DICT.copy()

        item_effects, set_keywords = self.get_item_active_effects()
        character_effects = self.get_character_active_effects()
        consumables_effects = self.get_consumables_active_effects()

        [[self.update_effect(active_effects[k], *item) for k in effects.keys() for item in effects[k].items()] for effects in [item_effects, character_effects, consumables_effects]]

        return active_effects, set_keywords