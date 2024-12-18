// Script assets have changed for v2.3.0 see
// https://help.yoyogames.com/hc/en-us/articles/360005277377 for more information
function script_activate_effect(_card_obj){
	_card_name = _card_obj.card_name
	global.activating_effect_name = _card_name
	global.activating_card_obj = _card_obj
	if(_card_obj.object_index == obj_card){
		if(_card_obj.type == "Spell"){
			_card_obj.speed = 0
			_card_obj.alarm[0] = -2
			_card_obj.in_play = true
		}
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
	if(_card_name == "Spring Water" or _card_name == "Holy Water Balloon"){
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
		time_between_actions = 60
		global.card_delay_card = _card_obj
		if(global.card_delay_count == 0){
			script_draw_card(1280, 930) //player_deck coords hardcoded
			obj_controller.alarm[4] = time_between_actions
			global.card_delay_count = 1
		}else{
			script_draw_card(1280, 930)
			global.player_turn = false
			global.playing_spell = false
			global.card_delay_count = 0
			_card_obj.alarm[3] = 30
		}
	}
	if(_card_name == "Verdant Codex"){
		time_between_actions = 60
		global.card_delay_card = _card_obj
		if(global.card_delay_count < 2){
			script_draw_card(1280, 930) //player_deck coords hardcoded
			obj_controller.alarm[4] = time_between_actions
			global.card_delay_count++
		}else{
			script_draw_card(1280, 930)
			global.card_delay_count = 0
			global.prompting_player_for_input = true
			for (var _i = 0; _i < instance_number(obj_card); ++_i;){
				curr_card = instance_find(obj_card, _i)
				if(not curr_card.in_play){
					curr_card.glowing = true
				}
			}
		}
	}
	if(_card_name == "Pirate Lord Jandreps"){
		time_between_actions = 60
		global.card_delay_card = _card_obj
		if(global.card_delay_count == 0){
			script_draw_card(1280, 930) //player_deck coords hardcoded
			obj_controller.alarm[4] = time_between_actions
			global.card_delay_count = 1
			_card_obj.current_health = _card_obj.current_health - 20
		}else{
			script_draw_card(1280, 930)
			global.player_turn = false
			//global.playing_spell = false
			global.card_delay_count = 0
		}
	}
	if(_card_name == "Technician Magician"){
		for (var _i = 0; _i < instance_number(obj_champions_card_opponents); ++_i;){
			curr_champion = instance_find(obj_champions_card_opponents, _i)
			curr_champion.current_health = curr_champion.current_health - 10
		}
	}
	if(_card_name == "Sirens Echo Mk. IV"){
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
}