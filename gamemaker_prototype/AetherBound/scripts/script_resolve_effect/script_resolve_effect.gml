// Script assets have changed for v2.3.0 see
// https://help.yoyogames.com/hc/en-us/articles/360005277377 for more information
function script_resolve_effect(_target){
	if(global.activating_effect_name == "Water Dagger"){
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
			_target.alarm[3] = 2
			_target.in_play = true
			_target.glowing = false
			global.card_delay_count++
		}else{
			_target.alarm[3] = 2
			_target.in_play = true
			global.card_delay_count = 0
			global.prompting_player_for_input = false
			global.player_turn = false
			global.playing_spell = false
			global.activating_card_obj.alarm[3] = 30
			for (var _i = 0; _i < instance_number(obj_card); ++_i;){
				curr_card = instance_find(obj_card, _i)
				curr_card.glowing = false
			}
		}
	}
}