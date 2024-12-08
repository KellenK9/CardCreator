/// Draw

if(mouse_check_button_released(mb_left)){
	if(position_meeting(mouse_x, mouse_y, self) and player_deck and global.player_turn){
		if(deck_size > 0){
			script_draw_card(x, y)
			global.player_turn = false
		}else{
			global.player_turn = false
			global.game_over = true
		}
	}
}

if(global.game_start){
	if(player_deck){
		if(array_length(global.deck_shuffled) == 0){
			sprite_index = spr_grave
		}
		else{
			sprite_index = spr_deck
		}
	}
	else{
		if(array_length(global.opponent_deck_shuffled) == 0){
			sprite_index = spr_grave
		}
		else{
			sprite_index = spr_deck
		}
	}
}
