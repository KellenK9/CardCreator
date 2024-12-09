// Script assets have changed for v2.3.0 see
// https://help.yoyogames.com/hc/en-us/articles/360005277377 for more information
function script_am_i_activatable(_card_object){
	if(global.game_over){
		return false
	}
	card_name = _card_object.card_name
	if(card_name == "Water Dagger"){
		return true
	}
	if(card_name == "The Sacred Spring"){
		nearest_champion = instance_nearest(_card_object.x, _card_object.y, obj_champion_card)
		if(nearest_champion.max_health > nearest_champion.current_health){
			return true
		}
		else{
			return false
		}
	}
	if(card_name == "Fireball"){
		return true
	}
	if(card_name == "Spreading Flame"){
		return true
	}
}