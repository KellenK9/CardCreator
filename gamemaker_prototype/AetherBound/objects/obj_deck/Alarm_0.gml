/// @description Shuffle deck

if(player_deck){
	global.deck_shuffled = array_shuffle(cards_in_deck)
}
else{
	global.opponent_deck_shuffled = array_shuffle(cards_in_deck)
}