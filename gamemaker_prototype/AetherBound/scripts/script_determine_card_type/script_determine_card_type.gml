// Script assets have changed for v2.3.0 see
// https://help.yoyogames.com/hc/en-us/articles/360005277377 for more information
function script_determine_card_type(_card_name){
	_card_type = "Equipment"
	list_of_spells = [
	"Fireball",
	"Spreading Flame",
	"Spring Water",
	"Pot of Greed",
	"Verdant Codex",
	"Celestial Shower",
	"Pressure",
	"Love Potion of Calming Mind",
	"Love Potion of Fiery Heart"
	]
	if(array_contains(list_of_spells, _card_name)){
		_card_type = "Spell"
	}
	return _card_type
}