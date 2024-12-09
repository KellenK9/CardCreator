/// @description Set init vars

champ_slots_arr = script_get_info_from_champion_name(card_name)
num_equip_slots = champ_slots_arr[0]
element = champ_slots_arr[1]
max_health = champ_slots_arr[2]
current_health = max_health