/// Set Variables

card_name = "Fire Golem"
alarm[0] = 1
champ_slots_arr = script_get_info_from_champion_name(card_name)
max_health = champ_slots_arr[2]
current_health = max_health
num_equip_slots = champ_slots_arr[0]
element = champ_slots_arr[1]

gui_x_offset = -14
gui_y_offset = -64

gui_x = x + gui_x_offset
gui_y = y + gui_y_offset

glowing = false

equipped_distance_threshold = 200

equip_slot_distance = 96

// Create Equipment Slots
if(num_equip_slots == 2){
	equipment_slot1 = instance_create_depth(x + equip_slot_distance, 135, 10, obj_equipment_slot_opponents)
	equipment_slot2 = instance_create_depth(x - equip_slot_distance, 135, 10, obj_equipment_slot_opponents)
	equipment_slot1.slot_type = element
	equipment_slot2.slot_type = element
}
if(num_equip_slots == 1){
	equipment_slot1 = instance_create_depth(x, 140, 10, obj_equipment_slot_opponents)
	equipment_slot1.slot_type = element
}
