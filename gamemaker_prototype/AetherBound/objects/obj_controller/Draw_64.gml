/// @description 

draw_set_color(c_black)

if(global.player_turn and not global.game_over){
	draw_text(1400, 1000, "Your Turn")
}

if(global.game_over){
	draw_text(1400, 1000, "Game Over")
	if(global.player_won){
		draw_text(1400, 1020, "You win!")
	}
	else{
		draw_text(1400, 1020, "You lose.")
	}
}
else{
	if(global.game_start){
		draw_text(1400, 20, string_concat("Opponents hand size: ", opponent_hand_size))
	}
	draw_text(1400,1020, global.timer)
}

draw_set_color(c_white)
