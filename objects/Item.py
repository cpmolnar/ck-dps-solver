class Item():
    def __init__(self, name, item_category, consider_for, set = None, attributes: dict = {}, reinforced = False, has_durability = False):
        self.name = name
        self.item_category = item_category
        self.consider_for = consider_for
        self.set = set
        self.attributes = {
            '%_damage': 0.,
            '%_physical_melee_damage': 0.,
            '%_physical_range_damage': 0.,
            '%_mining_damage': 0.,
            '%_melee_attack_speed': 0.,
            '%_range_attack_speed': 0.,
            '%_melee_and_range_attack_speed': 0.,
            '%_damage_against_bosses': 0.,
            '%_critical_hit_damage': 0.,
            '%_critical_hit_chance': 0.,
            '%_triple_hit_chance': 0.,
            '+_fishing': 0.,
            '+_mining_damage': 0.,
            '+_thorns_damage': 0.,
        }

        for attribute_name, value in attributes.items():
            self.attributes[attribute_name] += value
            
        self.has_durability = (has_durability | (item_category in ['Weapon', 'Helm', 'Breast armor', 'Pants armor']))
        self.reinforced = False
        if has_durability: self.reinforced = reinforced
        if reinforced and has_durability: self.reinforce()

    def reinforce(self):
        if not self.reinforced and self.has_durability:
            self.reinforced = True
            self.attributes = {k: round(v*1.15, 0 if k in ['+_fishing', '+_mining_damage', '+_thorns_damage'] else 3) for k, v in self.attributes.items()}