// Script assets have changed for v2.3.0 see
// https://help.yoyogames.com/hc/en-us/articles/360005277377 for more information
function script_am_i_activatable(_card_object){
	// Set vars
	if(global.game_over){
		return false
	}
	card_name = _card_object.card_name
	if(_card_object.object_index == obj_card){
		your_champion = obj_champion_card
	}
	else{
		your_champion = obj_champions_card_opponents
	}
	// Cases that are always activatable
	always_activatable = ["Water Dagger", "Fireball", "Spreading Flame"]
	if(array_contains(always_activatable, card_name)){
		return true
	}
	// Cases for each card
	if(card_name == "The Sacred Spring"){
		nearest_champion = instance_nearest(_card_object.x, _card_object.y, your_champion)
		if(nearest_champion.max_health > nearest_champion.current_health){
			return true
		}
		else{
			return false
		}
	}
}