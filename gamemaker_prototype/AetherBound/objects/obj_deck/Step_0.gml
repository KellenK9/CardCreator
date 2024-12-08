/// Draw

if(mouse_check_button_released(mb_left)){
	if(position_meeting(mouse_x, mouse_y, self) and player_deck){
		if(deck_size > 0){
			script_draw_card(x, y)
			global.player_turn = false
		}else{
			global.game_over = true
		}
	}
}