/// 

if(mouse_check_button_released(mb_left)){
	if(showing_zoomed_card){
		if(mouse_x > zoomed_right_border_x or mouse_x < zoomed_left_border_x){
			showing_zoomed_card = false
		}
	}else{
		if((not clicking_button) and (position_meeting(mouse_x, mouse_y, obj_card_parent))){
			card_to_zoom = instance_position(mouse_x, mouse_y, obj_card_parent)
			showing_zoomed_card = true
		}
	}
}