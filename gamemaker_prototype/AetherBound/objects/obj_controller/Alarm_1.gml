/// @description Opponent's Turn

// CPU draws if there are any cards left in deck
if(array_length(global.opponent_deck_shuffled) > 0){
	script_draw_card_opponent()
}
else{
	for (var _i = 0; _i < instance_number(obj_card_opponents); ++_i;){
		curr_card = instance_find(obj_card_opponents, _i)
		if(curr_card.type == "Equipment"){
			equipment_cards[_i] = curr_card
		}
		else{
			spell_cards[_i] = curr_card
		}
	}
	// CPU activates equipped equipment if possible
	for (var _i = 0; _i < array_length(equipment_cards); ++_i;){
		curr_card = equipment_cards[_i]
		if(curr_card.in_play){
			if(script_am_i_activatable(equipment_cards[_i])){
				script_activate_effect_opponent(equipment_cards[_i])
			}
		}
	}
	// CPU equips equipment if possible
	for (var _i = 0; _i < array_length(equipment_cards); ++_i;){
		if(not equipment_cards[_i].in_play){
			// Equip equipment here
		}
	}
	// CPU activates spells if possible
	for (var _i = 0; _i < array_length(spell_cards); ++_i;){
		if(not spell_cards[_i].in_play){
			if(script_am_i_activatable(spell_cards[_i])){
				script_activate_effect_opponent(spell_cards[_i])
			}
		}
	}
	// Draws to lose if cannot do anything
	script_draw_card_opponent()
}

global.player_turn = true
