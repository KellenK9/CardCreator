// Script assets have changed for v2.3.0 see
// https://help.yoyogames.com/hc/en-us/articles/360005277377 for more information
function script_activate_effect_opponent(_card_obj){
	_card_name = _card_obj.card_name
	if(_card_obj.type == "Spell"){
		_card_obj.speed = 0
		_card_obj.alarm[0] = -2
		_card_obj.in_play = true
	}
	if(_card_name == "Water Dagger"){
		// Choose a random target
		for (var _i = 0; _i < instance_number(obj_champion_card); ++_i;){
			players_champions[_i] = instance_find(obj_champion_card, _i)
		}
		_target = players_champions[irandom(array_length(players_champions) - 1)]
		_target.current_health = _target.current_health - 20
	}
	if(_card_name == "The Sacred Spring"){
		_target = instance_nearest(_card_obj.x, _card_obj.y, obj_champions_card_opponents)
		_target.current_health = _target.current_health + 10
	}
	if(_card_name == "Spreading Flame"){
		for (var _i = 0; _i < instance_number(obj_champion_card); ++_i;){
			curr_champion = instance_find(obj_champion_card, _i)
			curr_champion.current_health = curr_champion.current_health - 10
		}
		_card_obj.alarm[3] = 1
	}
	if(_card_name == "Fireball"){
		// Choose a random target
		for (var _i = 0; _i < instance_number(obj_champion_card); ++_i;){
			players_champions[_i] = instance_find(obj_champion_card, _i)
		}
		_target = players_champions[irandom(array_length(players_champions) - 1)]
		_target.current_health = _target.current_health - 20
		_card_obj.alarm[3] = 1
	}
}