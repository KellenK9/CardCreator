/// @description 

if(point_distance(x, y, curr_x, curr_y) <= 7 and speed != 0){
	speed = 0
	x = curr_x
	y = curr_y
}

if(mouse_check_button_pressed(mb_left)){
	if(position_meeting(mouse_x, mouse_y, self)){
		if(speed == 0 and x > 1920 - sprite_get_width(spr_zoom_filter) and not global.holding_card){
			being_held = true
			global.holding_card = true
		}
	}
}

if(being_held){
	x = mouse_x
	y = mouse_y
	if(mouse_check_button_released(mb_left)){
		being_held = false
		global.holding_card = false
		// if not near open equipment slot during your turn:
		alarm[0] = 5
	}
}
