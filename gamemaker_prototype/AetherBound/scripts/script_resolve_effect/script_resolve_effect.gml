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
}