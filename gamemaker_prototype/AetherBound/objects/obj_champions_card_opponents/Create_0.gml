/// Set Variables

card_name = "Fire Golem"
alarm[0] = 1
champ_slots_arr = script_get_info_from_champion_name(card_name)
max_health = champ_slots_arr[2]
current_health = max_health
num_equip_slots = champ_slots_arr[0]
element = champ_slots_arr[1]
sprite_index = script_convert_name_sprite(card_name)

gui_x_offset = -14
gui_y_offset = -64

gui_x = x + gui_x_offset
gui_y = y + gui_y_offset
gui_health_shift_x = 5

glowing = false

equipped_distance_threshold = 200

equip_slot_distance = 96

activation_effect_opacity = 0
