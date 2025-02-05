from objects import Character
import math

def calculate_adjusted_weapon_damage(character: Character, attributes, damage_type):
    item_stats = character.get_item_stats()
    
    adjusted_damage_multiplier = 1 + attributes['%_damage'] + (attributes['%_physical_range_damage'] if damage_type=='Range' else attributes['%_physical_melee_damage'])
    
    min_damage = character.items['Weapon'].min_damage * adjusted_damage_multiplier
    max_damage = character.items['Weapon'].max_damage * adjusted_damage_multiplier

    thorns_damage =  attributes['+_thorns_damage'] if sum([item_set=='scarab_set' for item_set in item_stats['set'].values()])>=3 else 0
    thorns_min_damage = thorns_damage * 0.9 * adjusted_damage_multiplier
    thorns_max_damage = thorns_damage * 1.1 * adjusted_damage_multiplier

    if damage_type=='Range':
        fishing_damage = attributes['+_fishing'] * ((character.perks['Fishing']['Well-trained aim'] * 0.06) + (0.24 if sum([item_set=='fishing_set' for item_set in item_stats['set'].values()])>=3 else 0))
        fishing_min_damage = fishing_damage * 0.9 * adjusted_damage_multiplier
        fishing_max_damage = fishing_damage * 1.1 * adjusted_damage_multiplier

    elif damage_type=='Melee':
        mining_damage = attributes['+_mining_damage'] * (1 + attributes['%_mining_damage']) * ((character.perks['Mining']['Miner\'s strength'] * 0.02) + \
                                                         (0.08 if sum([item_set=='mining_set' for item_set in item_stats['set'].values()])>=5 else 0) + \
                                                         (0.13 if sum([item_set=='ancient_gem_set' for item_set in item_stats['set'].values()])>=2 else 0))
        mining_min_damage = mining_damage * 0.9 * adjusted_damage_multiplier
        mining_max_damage = mining_damage * 1.1 * adjusted_damage_multiplier

    adjusted_min_damage = math.ceil(min_damage + (fishing_min_damage if damage_type=='Range' else mining_min_damage) + thorns_min_damage)
    adjusted_max_damage = math.floor(max_damage + (fishing_max_damage if damage_type=='Range' else mining_max_damage) + thorns_max_damage)

    return adjusted_min_damage, adjusted_max_damage

def calculate_weakness_detection_crit(character: Character, attributes):
    attacks_per_second = character.items['Weapon'].attacks_per_second * (1 + attributes['%_range_attack_speed'] + attributes['%_melee_and_range_attack_speed'])
    critical_hit_chance = attributes['%_critical_hit_chance']
    activation_chance = (1-(character.perks['Range']['Weakness detection'] * 0.02)) ** attacks_per_second # Chance of activating the perk each second
    active_likelihood = 1 - ((1 - activation_chance) ** 3) # Approximate likelihood of having activated the perk in the past 3 seconds
    adjusted_critical_hit_chance = active_likelihood + (critical_hit_chance * (1 - active_likelihood))
    return adjusted_critical_hit_chance

def calculate_fast_and_furious_attack_speed(character: Character, attributes):
    attacks_per_second = character.items['Weapon'].attacks_per_second * (1 + attributes['%_melee_attack_speed'] + attributes['%_melee_and_range_attack_speed'])
    activation_chance = (1-(character.perks['Melee']['Fast and furious'] * 0.02)) ** attacks_per_second # Chance of activating the perk each second
    active_likelihood = 1 - ((1 - activation_chance) ** 3) # Approximate likelihood of having activated the perk in the past 3 seconds
    adjusted_melee_attack_speed = (attributes['%_melee_attack_speed'] * 1.5 * active_likelihood) + (attributes['%_melee_attack_speed'] * (1 - active_likelihood))
    return adjusted_melee_attack_speed


def calculate_dps(character: Character):
    attributes = character.get_attributes()
    damage_type = character.items['Weapon'].damage_type
    min_damage, max_damage = calculate_adjusted_weapon_damage(character, attributes, damage_type)

    average_damage = (min_damage + max_damage) / 2
    critical_hit_chance = calculate_weakness_detection_crit(character, attributes) if damage_type=='Range' else attributes['%_critical_hit_chance']
    damage_type_attack_speed = (attributes['%_range_attack_speed'] if damage_type=='Range' else calculate_fast_and_furious_attack_speed(character, attributes))

    crit_adjusted_damage =  average_damage * (critical_hit_chance * (1 + attributes['%_critical_hit_damage'])) 
    crit_adjusted_damage += average_damage * (1 - critical_hit_chance)
    triple_adjusted_damage = crit_adjusted_damage * attributes['%_triple_hit_chance'] * 3
    triple_adjusted_damage += crit_adjusted_damage * (1 - attributes['%_triple_hit_chance'])

    attacks_per_second = character.items['Weapon'].attacks_per_second * (1 + damage_type_attack_speed + attributes['%_melee_and_range_attack_speed'])
    final_dps = triple_adjusted_damage * attacks_per_second

    return math.floor(final_dps)