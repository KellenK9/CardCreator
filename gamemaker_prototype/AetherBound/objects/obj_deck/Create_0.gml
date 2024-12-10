/// 

player_deck = true
alarm[1] = 1

if(player_deck){
	cards_in_deck = [
		"Water Dagger",
	]
}else{
	cards_in_deck = [
		"Fire Dagger",
	]
}
deck_size = array_length(cards_in_deck)
alarm[0] = 2