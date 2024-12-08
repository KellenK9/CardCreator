/// Draw

if(mouse_check_button_released(mb_left)){
	if(position_meeting(mouse_x, mouse_y, self)){
		if(deck_size > 0){
			// draw a card
			// instance_create card drawn
		}else{
			global.game_over = true
		}
	}
}