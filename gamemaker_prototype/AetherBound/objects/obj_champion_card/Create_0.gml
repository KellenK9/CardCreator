/// Set Variables

card_name = "Water Golem"
alarm[0] = 1
champ_slots_arr = script_get_info_from_champion_name(card_name)
max_health = champ_slots_arr[2]
current_health = max_health
num_equip_slots = champ_slots_arr[0]
element = champ_slots_arr[1]
sprite_index = script_convert_name_sprite(card_name)

gui_x_offset = -14
gui_y_offset = 40
gui_health_shift_x = 5

gui_x = x + gui_x_offset
gui_y = y + gui_y_offset

glowing = false

equipped_distance_threshold = 200

equip_slot_distance = 96

activation_effect_opacity = 0

red_shade = 255
green_shade = 255
blue_shade = 255
took_damage = false
healed = false
latest_health = current_health
alarm[1] = -2

//Champion specific vars (typically for trigger or passive effects)
technician_activated = false