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
	// check if card in grave
	for(var _i = 0; _i < instance_number(obj_grave); ++_i;){
		curr_grave = instance_find(obj_grave, _i)
		if(_card_object.x == curr_grave.x and _card_object.y == curr_grave.y){
			return false
		}
	}
	// Cases that are always activatable
	always_activatable = [
	"Water Dagger",
	"Fire Dagger",
	"Fireball",
	"Spreading Flame",
	"Sirens Echo Mk. IV",
	"Tidal Wave",
	"Pressure"]
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
	if(card_name == "Spring Water" or card_name == "Holy Water Balloon"){
		for (var _i = 0; _i < instance_number(obj_champion_card); ++_i;){
			curr_champion = instance_find(obj_champion_card, _i)
			if(curr_champion.max_health > curr_champion.current_health){
				return true
			}
		}
		for (var _i = 0; _i < instance_number(obj_champions_card_opponents); ++_i;){
			curr_champion = instance_find(obj_champions_card_opponents, _i)
			if(curr_champion.max_health > curr_champion.current_health){
				return true
			}
		}
		return false
	}
	if(card_name == "Pot of Greed"){
		if(_card_object.object_index == obj_card){
			if(array_length(global.deck_shuffled) >= 2){
				return true
			}else{
				return false
			}
		}else{
			if(array_length(global.opponent_deck_shuffled) >= 2){
				return true
			}else{
				return false
			}
		}
	}
	if(card_name == "Verdant Codex"){
		if(_card_object.object_index == obj_card){
			if(array_length(global.deck_shuffled) >= 3){
				return true
			}else{
				return false
			}
		}else{
			if(array_length(global.opponent_deck_shuffled) >= 3){
				return true
			}else{
				return false
			}
		}
	}
	if(card_name == "Pirate Lord Jandreps"){
		if(_card_object.object_index == obj_champion_card){
			if(array_length(global.deck_shuffled) >= 2){
				return true
			}else{
				return false
			}
		}else{
			if(array_length(global.opponent_deck_shuffled) >= 2){
				return true
			}else{
				return false
			}
		}
	}
	if(card_name == "Celestial Shower"){
		cpu_has_equipment = false
		player_has_equipment = false
		for (var _i = 0; _i < instance_number(obj_card_opponents); ++_i;){
			curr_card = instance_find(obj_card_opponents, _i)
			if(curr_card.in_play and curr_card.type == "Equipment"){
				cpu_has_equipment = true
			}
		}
		for (var _i = 0; _i < instance_number(obj_card); ++_i;){
			curr_card = instance_find(obj_card, _i)
			if(curr_card.in_play and curr_card.type == "Equipment"){
				player_has_equipment = true
			}
		}
		if(player_has_equipment and cpu_has_equipment){
			return true
		}else{
			return false
		}
	}
	if(card_name == "Love Potion of Calming Mind"){
		have_equipment_for_discard = false
		have_target = false
		if(_card_object.object_index == obj_card){
			for (var _i = 0; _i < instance_number(obj_card); ++_i;){
				curr_card = instance_find(obj_card, _i)
				if(not curr_card.in_play and curr_card.type == "Equipment" and curr_card.element == "Water"){
					have_equipment_for_discard =  true
				}
			}
		}else{
			for (var _i = 0; _i < instance_number(obj_card_opponents); ++_i;){
				curr_card = instance_find(obj_card_opponents, _i)
				if(not curr_card.in_play and curr_card.type == "Equipment" and curr_card.element == "Water"){
					have_equipment_for_discard =  true
				}
			}
		}
		for (var _i = 0; _i < instance_number(obj_champion_card); ++_i;){
			curr_champion = instance_find(obj_champion_card, _i)
			if(curr_champion.max_health > curr_champion.current_health){
				have_target = true
			}
		}
		for (var _i = 0; _i < instance_number(obj_champions_card_opponents); ++_i;){
			curr_champion = instance_find(obj_champions_card_opponents, _i)
			if(curr_champion.max_health > curr_champion.current_health){
				have_target = true
			}
		}
		if(have_equipment_for_discard and have_target){
			return true
		}else{
			return false
		}
	}
	if(card_name == "Love Potion of Fiery Heart"){
		if(_card_object.object_index == obj_card){
			for (var _i = 0; _i < instance_number(obj_card); ++_i;){
				curr_card = instance_find(obj_card, _i)
				if(not curr_card.in_play and curr_card.type == "Equipment" and curr_card.element == "Fire"){
					return true
				}
			}
		}else{
			for (var _i = 0; _i < instance_number(obj_card_opponents); ++_i;){
				curr_card = instance_find(obj_card_opponents, _i)
				if(not curr_card.in_play and curr_card.type == "Equipment" and curr_card.element == "Fire"){
					return true
				}
			}
		}
		return false
	}
}