/// 

global.hand_x = 1500 + (global.hand_size * 16)
global.hand_y = 200 + (global.hand_size * 4)

if(mouse_check_button_released(mb_left) and showing_zoomed_card){
	showing_zoomed_card = false
}
if(mouse_check_button_released(mb_middle) or mouse_check_button_released(mb_right)){
	if(showing_zoomed_card){
		showing_zoomed_card = false
	}else{
		if(not clicking_button and not global.holding_card and (position_meeting(mouse_x, mouse_y, obj_card_parent))){
			card_to_zoom = instance_position(mouse_x, mouse_y, obj_card_parent)
			card_name = string(card_to_zoom.card_name)
			showing_zoomed_card = true
			spr_to_show = script_covert_name_to_zoomed_sprite(card_name)
		}
	}
}

// Check if card played
if(mouse_check_button_released(mb_left) and global.holding_card){
	if(global.card_held.type == "Equipment"){
		for(var _i = 0; _i < equip_array_length; ++_i){
			if(point_distance(mouse_x, mouse_y, equip_slot_x_values[_i], 930) < equip_distance_threshold or point_distance(mouse_x, mouse_y, equip_slot_x_values[_i], 930-equip_distance_threshold) < equip_distance_threshold){
				// Play Equipment
				global.playing_equipment = true
				global.equip_slot_coord_recent = [equip_slot_x_values[_i], 930]
			}
		}
	}
	if(global.card_held.type == "Spell"){
		if(mouse_x < sprite_get_width(spr_field_border)){
			// Play spell
			global.playing_spell = true
		}
	}
}

// Make move for cpu
if(global.game_start and not global.player_turn){
	alarm[1] = 100
}
