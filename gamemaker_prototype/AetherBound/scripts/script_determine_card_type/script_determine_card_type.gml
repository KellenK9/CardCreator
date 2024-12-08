// Script assets have changed for v2.3.0 see
// https://help.yoyogames.com/hc/en-us/articles/360005277377 for more information
function script_determine_card_type(_card_name){
	_card_type = "Equipment"
	if _card_name == "Fireball"{
		_card_type = "Spell"
	}
	return _card_type
}