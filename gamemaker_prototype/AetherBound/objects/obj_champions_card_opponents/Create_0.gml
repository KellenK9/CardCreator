/// Set Variables

card_name = "Fire Golem"
max_health = 100
current_health = max_health
num_equip_slots = 2
element = "Water"

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
