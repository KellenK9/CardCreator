/// Draw

if(mouse_check_button_released(mb_left)){
	if(position_meeting(mouse_x, mouse_y, self)){
		if(deck_size > 0){
			script_draw_card(x, y)
		}else{
			global.game_over = true
		}
	}
}