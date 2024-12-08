/// 

global.hand_x = 1500 + (global.hand_size * 16)
global.hand_y = 200 + (global.hand_size * 4)

if(mouse_check_button_released(mb_left)){
	if(showing_zoomed_card){
		showing_zoomed_card = false
	}else{
		if(not clicking_button and not global.holding_card and (position_meeting(mouse_x, mouse_y, obj_card_parent))){
			card_to_zoom = instance_position(mouse_x, mouse_y, obj_card_parent)
			card_name = string(card_to_zoom.card_name)
			showing_zoomed_card = true
			spr_to_show = script_covert_name_to_zoomed_sprite(card_name)
		}
	}
}