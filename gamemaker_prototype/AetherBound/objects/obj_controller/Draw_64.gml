/// @description 

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