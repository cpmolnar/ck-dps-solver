from . import Item
import math

class Weapon(Item):
    def __init__(self, name, min_damage, max_damage, attacks_per_second, damage_type, consider_for, set = None, attributes: dict = {}, reinforced = False):
        super().__init__(name, 'Weapon', consider_for, set, attributes, reinforced)
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.attacks_per_second = attacks_per_second
        self.damage_type = damage_type

    def reinforce(self):
        if not self.reinforced:
            self.reinforced = True
            self.attributes = {k: round(v*1.15, 0 if k in ['+_fishing', '+_mining_damage', '+_thorns_damage'] else 3) for k, v in self.attributes.items()}
            self.min_damage = math.ceil(self.min_damage*1.15)
            self.max_damage = math.floor(self.max_damage*1.15)