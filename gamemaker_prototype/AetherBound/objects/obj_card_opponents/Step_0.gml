/// @description 

sprite_index = script_convert_name_sprite(card_name)

if(moving_towards_grave){
	if(point_distance(x, y, cpu_grave_x, cpu_grave_y) <= 7){
		speed = 0
		x = cpu_grave_x
		y = cpu_grave_y
		moving_towards_grave = false
	}
}
if(moving_towards_slot){
	if(point_distance(x, y, curr_x, curr_y) <= 7){
		speed = 0
		x = curr_x
		y = curr_y
		moving_towards_slot = false
	}
}

if(mouse_check_button_released(mb_left) and position_meeting(mouse_x, mouse_y, self)){
	if(global.prompting_player_for_input and glowing){
		alarm[5] = 1
		script_resolve_effect(self)
	}
}