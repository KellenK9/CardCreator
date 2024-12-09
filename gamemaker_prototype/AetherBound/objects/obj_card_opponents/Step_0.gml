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