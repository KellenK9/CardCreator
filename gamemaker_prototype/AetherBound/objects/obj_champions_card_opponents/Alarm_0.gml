/// @description Set init vars

champ_slots_arr = script_get_info_from_champion_name(card_name)
num_equip_slots = champ_slots_arr[0]
element = champ_slots_arr[1]
max_health = champ_slots_arr[2]
current_health = max_health
sprite_index = script_convert_name_sprite(card_name)

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