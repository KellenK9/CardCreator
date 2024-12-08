/// @description Draw self and glow

if(player_deck and global.player_turn and global.game_start and not global.game_over){
	if(array_length(global.deck_shuffled) != 0){
		draw_sprite(spr_glow_effect, 1, x, y)
	}
}

// Draw Self
if(not player_deck){
	image_angle = 180
}
draw_self()