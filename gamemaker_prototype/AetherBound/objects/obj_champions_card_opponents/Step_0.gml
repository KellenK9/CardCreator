/// Adjust Vars

if(current_health < 100){
	gui_x = x + gui_x_offset + gui_health_shift_x
}else{
	gui_x = x + gui_x_offset
}
gui_y = y + gui_y_offset

if(mouse_check_button_released(mb_left) and position_meeting(mouse_x, mouse_y, self)){
	if(global.prompting_player_for_input and glowing){
		script_resolve_effect(self)
	}
}

if(current_health <= 0){
	for (var _i = 0; _i < instance_number(obj_card_opponents); ++_i;){
		curr_card = instance_find(obj_card_opponents, _i)
		if(curr_card.in_play and distance_to_point(curr_card.x, curr_card.y) < equipped_distance_threshold){
			curr_card.alarm[3] = 30
		}
	}
	if(num_equip_slots >= 1){
		instance_destroy(equipment_slot1)
		if(num_equip_slots >= 1){
			instance_destroy(equipment_slot2)
		}
	}
	instance_destroy(self)
}
