// Script assets have changed for v2.3.0 see
// https://help.yoyogames.com/hc/en-us/articles/360005277377 for more information
function script_activate_equipment_effect(_card_obj){
	_card_name = _card_obj.card_name
	global.activating_effect_name = _card_name
	if(_card_name == "Water Dagger"){
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
	}
}