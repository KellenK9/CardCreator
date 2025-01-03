// Script assets have changed for v2.3.0 see
// https://help.yoyogames.com/hc/en-us/articles/360005277377 for more information
function script_resolve_effect(_target){
	if(global.activating_effect_name == "Water Dagger" or global.activating_effect_name == "Fire Dagger"){
		_target.current_health = _target.current_health - 10
		for (var _i = 0; _i < instance_number(obj_champion_card); ++_i;){
			curr_champion = instance_find(obj_champion_card, _i)
			curr_champion.glowing = false
		}
		for (var _i = 0; _i < instance_number(obj_champions_card_opponents); ++_i;){
			curr_champion = instance_find(obj_champions_card_opponents, _i)
			curr_champion.glowing = false
		}
		global.prompting_player_for_input = false
		global.player_turn = false
	}
	if(global.activating_effect_name == "Fireball"){
		_target.current_health = _target.current_health - 20
		for (var _i = 0; _i < instance_number(obj_champion_card); ++_i;){
			curr_champion = instance_find(obj_champion_card, _i)
			curr_champion.glowing = false
		}
		for (var _i = 0; _i < instance_number(obj_champions_card_opponents); ++_i;){
			curr_champion = instance_find(obj_champions_card_opponents, _i)
			curr_champion.glowing = false
		}
		global.prompting_player_for_input = false
		global.player_turn = false
		global.playing_spell = false
		global.activating_card_obj.alarm[3] = 30
	}
	if(global.activating_effect_name == "Spring Water"){
		_target.current_health = _target.current_health + 20
		if(_target.current_health > _target.max_health){
			_target.current_health = _target.max_health
		}
		for (var _i = 0; _i < instance_number(obj_champion_card); ++_i;){
			curr_champion = instance_find(obj_champion_card, _i)
			curr_champion.glowing = false
		}
		for (var _i = 0; _i < instance_number(obj_champions_card_opponents); ++_i;){
			curr_champion = instance_find(obj_champions_card_opponents, _i)
			curr_champion.glowing = false
		}
		global.prompting_player_for_input = false
		global.player_turn = false
		global.playing_spell = false
		global.activating_card_obj.alarm[3] = 30
	}
	if(global.activating_effect_name == "Verdant Codex"){
		if(global.card_delay_count == 0){
			_target.alarm[3] = 30
			_target.in_play = true
			_target.glowing = false
			global.card_delay_count++
		}else{
			_target.alarm[3] = 30
			_target.in_play = true
			global.card_delay_count = 0
			global.prompting_player_for_input = false
			global.player_turn = false
			global.playing_spell = false
			global.activating_card_obj.alarm[3] = 40
			for (var _i = 0; _i < instance_number(obj_card); ++_i;){
				curr_card = instance_find(obj_card, _i)
				curr_card.glowing = false
			}
		}
	}
	if(global.activating_effect_name == "Sirens Echo Mk. IV"){
		_target.current_health = _target.current_health - 20
		for (var _i = 0; _i < instance_number(obj_champion_card); ++_i;){
			curr_champion = instance_find(obj_champion_card, _i)
			curr_champion.glowing = false
		}
		for (var _i = 0; _i < instance_number(obj_champions_card_opponents); ++_i;){
			curr_champion = instance_find(obj_champions_card_opponents, _i)
			curr_champion.glowing = false
		}
		global.prompting_player_for_input = false
		global.player_turn = false
		global.activating_card_obj.alarm[0] = 30
		global.activating_card_obj.in_play = false
		equip_slot = instance_position(global.activating_card_obj.x, global.activating_card_obj.y, obj_equipment_slot)
		equip_slot.slot_filled = false
	}
	if(global.activating_effect_name == "Holy Water Balloon"){
		_target.current_health = _target.current_health + 30
		if(_target.current_health > _target.max_health){
			_target.current_health = _target.max_health
		}
		for (var _i = 0; _i < instance_number(obj_champion_card); ++_i;){
			curr_champion = instance_find(obj_champion_card, _i)
			curr_champion.glowing = false
		}
		for (var _i = 0; _i < instance_number(obj_champions_card_opponents); ++_i;){
			curr_champion = instance_find(obj_champions_card_opponents, _i)
			curr_champion.glowing = false
		}
		global.prompting_player_for_input = false
		global.player_turn = false
		global.activating_card_obj.alarm[3] = 30
		global.activating_card_obj.destroyed = true
		equip_slot = instance_position(global.activating_card_obj.x, global.activating_card_obj.y, obj_equipment_slot)
		equip_slot.slot_filled = false
	}
	if(global.activating_effect_name == "Tidal Wave"){
		_target.current_health = _target.current_health - 40
		for (var _i = 0; _i < instance_number(obj_champion_card); ++_i;){
			curr_champion = instance_find(obj_champion_card, _i)
			curr_champion.glowing = false
		}
		for (var _i = 0; _i < instance_number(obj_champions_card_opponents); ++_i;){
			curr_champion = instance_find(obj_champions_card_opponents, _i)
			curr_champion.glowing = false
		}
		global.prompting_player_for_input = false
		global.player_turn = false
		global.activating_card_obj.alarm[3] = 30
		global.activating_card_obj.destroyed = true
		equip_slot = instance_position(global.activating_card_obj.x, global.activating_card_obj.y, obj_equipment_slot)
		equip_slot.slot_filled = false
	}
	if(global.activating_effect_name == "Love Potion of Calming Mind"){
		if(global.card_delay_count == 0){
			_target.alarm[3] = 30
			_target.in_play = true
			for (var _i = 0; _i < instance_number(obj_card); ++_i;){
				curr_card = instance_find(obj_card, _i)
				curr_card.glowing = false
			}
			for (var _i = 0; _i < instance_number(obj_champion_card); ++_i;){
				curr_champion = instance_find(obj_champion_card, _i)
				if(curr_champion.current_health < curr_champion.max_health){
					curr_champion.glowing = true
				}
			}
			for (var _i = 0; _i < instance_number(obj_champions_card_opponents); ++_i;){
				curr_champion = instance_find(obj_champions_card_opponents, _i)
				if(curr_champion.current_health < curr_champion.max_health){
					curr_champion.glowing = true
				}
			}
			global.card_delay_count++
		}else{
			if(_target.object_index == obj_champion_card or _target.object_index == obj_champions_card_opponents){
				_target.current_health += 40
				if(_target.current_health > _target.max_health){
					_target.current_health = _target.max_health
				}
				global.card_delay_count = 0
				global.prompting_player_for_input = false
				global.player_turn = false
				global.playing_spell = false
				global.activating_card_obj.alarm[3] = 40
				for (var _i = 0; _i < instance_number(obj_champion_card); ++_i;){
					curr_card = instance_find(obj_champion_card, _i)
					curr_card.glowing = false
				}
				for (var _i = 0; _i < instance_number(obj_champions_card_opponents); ++_i;){
					curr_card = instance_find(obj_champions_card_opponents, _i)
					curr_card.glowing = false
				}
			}
		}
	}
	if(global.activating_effect_name == "Love Potion of Fiery Heart"){
		if(global.card_delay_count == 0){
			_target.alarm[3] = 30
			_target.in_play = true
			for (var _i = 0; _i < instance_number(obj_card); ++_i;){
				curr_card = instance_find(obj_card, _i)
				curr_card.glowing = false
			}
			for (var _i = 0; _i < instance_number(obj_champion_card); ++_i;){
				curr_champion = instance_find(obj_champion_card, _i)
				if(curr_champion.current_health < curr_champion.max_health){
					curr_champion.glowing = true
				}
			}
			for (var _i = 0; _i < instance_number(obj_champions_card_opponents); ++_i;){
				curr_champion = instance_find(obj_champions_card_opponents, _i)
				if(curr_champion.current_health < curr_champion.max_health){
					curr_champion.glowing = true
				}
			}
			global.card_delay_count++
		}else{
			if(_target.object_index == obj_champion_card or _target.object_index == obj_champions_card_opponents){
				_target.current_health = _target.current_health - 30
				global.card_delay_count = 0
				global.prompting_player_for_input = false
				global.player_turn = false
				global.playing_spell = false
				global.activating_card_obj.alarm[3] = 40
				for (var _i = 0; _i < instance_number(obj_champion_card); ++_i;){
					curr_card = instance_find(obj_champion_card, _i)
					curr_card.glowing = false
				}
				for (var _i = 0; _i < instance_number(obj_champions_card_opponents); ++_i;){
					curr_card = instance_find(obj_champions_card_opponents, _i)
					curr_card.glowing = false
				}
			}
		}
	}
	if(global.activating_effect_name == "Pressure"){
		if(global.card_delay_count == 0){
			_target.current_health = _target.current_health - 10
			for (var _i = 0; _i < instance_number(obj_champion_card); ++_i;){
				curr_champion = instance_find(obj_champion_card, _i)
				curr_champion.glowing = false
			}
			for (var _i = 0; _i < instance_number(obj_champions_card_opponents); ++_i;){
				curr_champion = instance_find(obj_champions_card_opponents, _i)
				curr_champion.glowing = false
			}
			global.activating_card_obj.alarm[0] = 30
			global.activating_card_obj.in_play = false
			if(global.hand_size < 3){
				global.prompting_player_for_input = false
				global.player_turn = false
				global.playing_spell = false
			}else{
				for (var _i = 0; _i < instance_number(obj_card); ++_i;){
					curr_card = instance_find(obj_card, _i)
					curr_card.glowing = true
				}
				global.card_delay_count++
			}
		}else{
			_target.alarm[3] = 10
			global.prompting_player_for_input = false
			global.player_turn = false
			global.playing_spell = false
			global.card_delay_count = 0
			for (var _i = 0; _i < instance_number(obj_card); ++_i;){
				curr_card = instance_find(obj_card, _i)
				curr_card.glowing = false
			}
		}
	}
}