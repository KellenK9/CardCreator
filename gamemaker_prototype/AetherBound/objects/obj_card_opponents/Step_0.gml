/// @description 

sprite_index = script_convert_name_sprite(card_name)

if(moving_towards_grave){
	if(point_distance(x, y, cpu_grave_x, cpu_grave_y) <= 7){
		speed = 0
		x = cpu_grave_x
		y = cpu_grave_y
	}
}
