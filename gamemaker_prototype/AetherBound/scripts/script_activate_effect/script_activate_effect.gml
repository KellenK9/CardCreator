// Script assets have changed for v2.3.0 see
// https://help.yoyogames.com/hc/en-us/articles/360005277377 for more information
function script_activate_effect(_card_obj){
	if(global.card_delay > 0){
		global.card_delay = global.card_delay - 1
	}
	_card_name = _card_obj.card_name
	global.activating_effect_name = _card_name
	global.activating_card_obj = _card_obj
	if(_card_obj.type == "Spell"){
		_card_obj.speed = 0
		_card_obj.alarm[0] = -2
		_card_obj.in_play = true
	}
	if(_card_name == "Water Dagger" or _card_name == "Fire Dagger"){
		//prompt player for Champion to select
		global.prompting_player_for_input = true
		for (var _i = 0; _i < instance_number(obj_champion_card); ++_i;){
			curr_champion = instance_find(obj_champion_card, _i)
			curr_champion.glowing = true
		}
		for (var _i = 0; _i < instance_number(obj_champions_card_opponents); ++_i;){
			curr_champion = instance_find(obj_champions_card_opponents, _i)
			curr_champion.glowing = true
		}
	}
	if(_card_name == "The Sacred Spring"){
		_target = instance_nearest(_card_obj.x, _card_obj.y, obj_champion_card)
		_target.current_health = _target.current_health + 10
		global.player_turn = false
	}
	if(_card_name == "Spreading Flame"){
		for (var _i = 0; _i < instance_number(obj_champions_card_opponents); ++_i;){
			curr_champion = instance_find(obj_champions_card_opponents, _i)
			curr_champion.current_health = curr_champion.current_health - 10
		}
		global.player_turn = false
		global.playing_spell = false
		_card_obj.alarm[3] = 30
	}
	if(_card_name == "Fireball"){
		global.prompting_player_for_input = true
		for (var _i = 0; _i < instance_number(obj_champion_card); ++_i;){
			curr_champion = instance_find(obj_champion_card, _i)
			curr_champion.glowing = true
		}
		for (var _i = 0; _i < instance_number(obj_champions_card_opponents); ++_i;){
			curr_champion = instance_find(obj_champions_card_opponents, _i)
			curr_champion.glowing = true
		}
	}
	if(_card_name == "Spring Water"){
		global.prompting_player_for_input = true
		for (var _i = 0; _i < instance_number(obj_champion_card); ++_i;){
			curr_champion = instance_find(obj_champion_card, _i)
			if(curr_champion.max_health > curr_champion.current_health){
				curr_champion.glowing = true
			}
		}
		for (var _i = 0; _i < instance_number(obj_champions_card_opponents); ++_i;){
			curr_champion = instance_find(obj_champions_card_opponents, _i)
			if(curr_champion.max_health > curr_champion.current_health){
				curr_champion.glowing = true
			}
		}
	}
	if(_card_name == "Pot of Greed"){
		if(global.card_delay < 0){
			script_draw_card(1280, 930) //player_deck coords hardcoded
			global.card_delay = 60
		}
		if(global.card_delay > 10){
			script_activate_effect(_card_obj)
		}else{ //global.card_delay == 0
			global.card_delay = -1
			script_draw_card(1280, 930)
			global.player_turn = false
			global.playing_spell = false
			_card_obj.alarm[3] = 30
		}
	}
}