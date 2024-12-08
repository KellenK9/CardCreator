/// Draw cards at start of game

script_draw_card(player_deck.x, player_deck.y)

if(global.hand_size < global.starting_hand_size){
	alarm[0] = 90
}else{
	global.player_turn = true
	global.game_start = true
}