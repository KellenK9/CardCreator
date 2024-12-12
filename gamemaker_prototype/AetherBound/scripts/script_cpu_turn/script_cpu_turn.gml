// Script assets have changed for v2.3.0 see
// https://help.yoyogames.com/hc/en-us/articles/360005277377 for more information
function script_cpu_turn(){
	//Set Vars
	var _j = 0
	var _k = 0
	card_activated = false
	// CPU sorts its cards into equipment and spells
	if(not card_activated){
		for (var _i = 0; _i < instance_number(obj_card_opponents); ++_i;){
			curr_card = instance_find(obj_card_opponents, _i)
			if(curr_card.type == "Equipment"){
				equipment_cards[_j] = curr_card
				_j = _j + 1
			}
			else{
				spell_cards[_k] = curr_card
				_k = _k + 1
			}
		}
	}
	// CPU activates spells if possible
	for (var _i = 0; _i < array_length(spell_cards); ++_i;){
		if(not spell_cards[_i].in_play){
			if(script_am_i_activatable(spell_cards[_i]) and not card_activated){
				// CPU first checks to activate Pot of Greed first
				if(spell_cards[_i].card_name == "Pot of Greed"){
					if(script_am_i_activatable(spell_cards[_i])){
						obj_controller.alarm[4] = 2 //setting this alarm activates effects with a delay
						global.card_delay_card = spell_cards[_i]
						card_activated = true
						spell_cards[_i].in_play = true
					}
				}
				// CPU first checks to activate Spring Water and heal
				if(spell_cards[_i].card_name == "Spring Water"){
					for (var _j = 0; _j < instance_number(obj_champions_card_opponents); ++_j;){
						curr_champion = instance_find(obj_champions_card_opponents, _j)
						if(curr_champion.max_health - curr_champion.current_health >= 20 and not card_activated){ //Need to have a check for not card_activated for every nested for loop
							script_activate_effect_opponent(spell_cards[_i])
							card_activated = true
							spell_cards[_i].in_play = true
						}
					}
				}
				else{
					script_activate_effect_opponent(spell_cards[_i])
					card_activated = true
					spell_cards[_i].in_play = true
				}
			}
		}
	}
	// CPU draws if there are any cards left in deck
	if(array_length(global.opponent_deck_shuffled) > 0 and not card_activated){
		script_draw_card_opponent()
		card_activated = true
	}
	// CPU activates equipped equipment if possible
	for (var _i = 0; _i < array_length(equipment_cards); ++_i;){
		if(equipment_cards[_i].in_play){
			if(script_am_i_activatable(equipment_cards[_i]) and not card_activated){
				script_activate_effect_opponent(equipment_cards[_i])
				card_activated = true
			}
		}
	}
	// CPU equips equipment if possible
	for (var _i = 0; _i < array_length(equipment_cards); ++_i;){
		if(not equipment_cards[_i].in_play){
			for (var _j = 0; _j < instance_number(obj_equipment_slot_opponents); ++_j;){
				curr_slot = instance_find(obj_equipment_slot_opponents, _j)
				if(curr_slot.slot_type == equipment_cards[_i].element and not curr_slot.slot_filled and not card_activated){
					curr_slot.slot_filled = true
					equipment_cards[_i].alarm[0] = 1
					global.recent_cpu_equip_slot_coord = [curr_slot.x, curr_slot.y]
					card_activated = true
					equipment_cards[_i].in_play = true
				}
			}
		}
	}
	// Draws to lose if cannot do anything
	if(not card_activated){
		script_draw_card_opponent()
	}

	global.player_turn = true
}