from objects import Character
import math

def calculate_adjusted_weapon_damage(character: Character, active_effects, set_keywords, damage_type):
    adjusted_damage_multiplier = 1 + active_effects['%_damage'] + (active_effects['%_physical_range_damage'] if damage_type=='Range' else active_effects['%_physical_melee_damage'])
    
    min_damage = character.items['Weapon'].min_damage * adjusted_damage_multiplier
    max_damage = character.items['Weapon'].max_damage * adjusted_damage_multiplier

    thorns_damage =  active_effects['+_thorns_damage'] if sum([item_set=='scarab_set' for item_set in set_keywords.values()])>=3 else 0
    thorns_min_damage = thorns_damage * 0.9 * adjusted_damage_multiplier
    thorns_max_damage = thorns_damage * 1.1 * adjusted_damage_multiplier

    if damage_type=='Range':
        fishing_damage = active_effects['+_fishing'] * ((character.perks['Fishing']['Well-trained aim'] * 0.06) + (0.24 if sum([item_set=='fishing_set' for item_set in set_keywords.values()])>=3 else 0))
        fishing_min_damage = fishing_damage * 0.9 * adjusted_damage_multiplier
        fishing_max_damage = fishing_damage * 1.1 * adjusted_damage_multiplier

    elif damage_type=='Melee':
        mining_damage = active_effects['+_mining_damage'] * (1 + active_effects['%_mining_damage']) * ((character.perks['Mining']['Miner\'s strength'] * 0.02) + \
                                                         (0.08 if sum([item_set=='mining_set' for item_set in set_keywords.values()])>=5 else 0) + \
                                                         (0.13 if sum([item_set=='ancient_gem_set' for item_set in set_keywords.values()])>=2 else 0))
        mining_min_damage = mining_damage * 0.9 * adjusted_damage_multiplier
        mining_max_damage = mining_damage * 1.1 * adjusted_damage_multiplier

    adjusted_min_damage = math.ceil(min_damage + (fishing_min_damage if damage_type=='Range' else mining_min_damage) + thorns_min_damage)
    adjusted_max_damage = math.floor(max_damage + (fishing_max_damage if damage_type=='Range' else mining_max_damage) + thorns_max_damage)

    return adjusted_min_damage, adjusted_max_damage

def calculate_weakness_detection_crit(character: Character, attributes):
    attacks_per_second = character.items['Weapon'].attacks_per_second * (1 + attributes['%_range_attack_speed'] + attributes['%_melee_and_range_attack_speed'])
    expected_rolls_per_outcome = 1 / (character.perks['Range']['Weakness detection'] * 0.02)
    expected_seconds_until_outcome = expected_rolls_per_outcome / attacks_per_second
    active_likelihood = 3 / (3 + expected_seconds_until_outcome) # This is activation length / the expected length of the block of time in and out of activation
    adjusted_critical_hit_chance = active_likelihood + (attributes['%_critical_hit_chance'] * (1 - active_likelihood))
    return adjusted_critical_hit_chance

def calculate_fast_and_furious_attack_speed(character: Character, attributes):
    attacks_per_second = character.items['Weapon'].attacks_per_second * (1 + attributes['%_melee_attack_speed'] + attributes['%_melee_and_range_attack_speed'])
    expected_rolls_per_outcome = 1 / (character.perks['Melee']['Fast and furious'] * 0.02)
    expected_seconds_until_outcome = expected_rolls_per_outcome / attacks_per_second
    active_likelihood = 2 / (2 + expected_seconds_until_outcome)
    adjusted_melee_attack_speed = (1.5 * active_likelihood) + (1 - active_likelihood)
    return adjusted_melee_attack_speed


def calculate_dps(character: Character):
    damage_type = character.items['Weapon'].damage_type
    active_effects_sources, set_keywords = character.get_active_effects()
    active_effects = {k: sum(v.values()) for k, v in active_effects_sources.items()}
    min_damage, max_damage = calculate_adjusted_weapon_damage(character, active_effects, set_keywords, damage_type)

    average_damage = (min_damage + max_damage) / 2
    critical_hit_chance = calculate_weakness_detection_crit(character, active_effects) if damage_type=='Range' else active_effects['%_critical_hit_chance']
    damage_type_attack_speed = (active_effects['%_range_attack_speed'] if damage_type=='Range' else active_effects['%_melee_attack_speed'])

    crit_adjusted_damage =  average_damage * (critical_hit_chance * (1 + active_effects['%_critical_hit_damage'])) 
    crit_adjusted_damage += average_damage * (1 - critical_hit_chance)
    triple_adjusted_damage = crit_adjusted_damage * active_effects['%_triple_hit_chance'] * 3
    triple_adjusted_damage += crit_adjusted_damage * (1 - active_effects['%_triple_hit_chance'])

    attacks_per_second = character.items['Weapon'].attacks_per_second * (1 + damage_type_attack_speed + active_effects['%_melee_and_range_attack_speed']) * calculate_fast_and_furious_attack_speed(character, active_effects)
    final_dps = triple_adjusted_damage * attacks_per_second

    return math.floor(final_dps)