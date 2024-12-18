/// @description 

sprite_index = script_convert_name_sprite(card_name)

if(point_distance(x, y, curr_x, curr_y) <= 7 and speed != 0 and not moving_towards_grave){
	speed = 0
	x = curr_x
	y = curr_y
}
if(moving_towards_grave){
	if(point_distance(x, y, player_grave_x, player_grave_y) <= 7){
		speed = 0
		x = player_grave_x
		y = player_grave_y
		moving_towards_grave = false
	}
}

if(mouse_check_button_pressed(mb_left) and not in_play and global.game_start and speed == 0 and (curr_x != 0 or curr_y != 0)){
	if(position_meeting(mouse_x, mouse_y, self)){
		if(speed == 0 and x > 1920 - sprite_get_width(spr_zoom_filter) and not global.holding_card){
			being_held = true
			global.holding_card = true
			global.card_held = self
			depth = depth - 3
		}
	}
}

if(being_held){
	x = mouse_x
	y = mouse_y
	if(mouse_check_button_released(mb_left)){
		being_held = false
		alarm[1] = 1
		// if not near open equipment slot during your turn:
		if(x < 1920 - sprite_get_width(spr_hand_and_menu_area)){
			alarm[0] = 5
		}
	}
}

//Equip
if(alarm[0] > 0){
	if(global.playing_equipment){
		speed = 0
		alarm[0] = -2
		in_play = true
		x = global.equip_slot_coord_recent[0]
		y = global.equip_slot_coord_recent[1]
		global.hand_size = global.hand_size - 1
		global.playing_equipment = false
		global.player_turn = false
	}
}

//Get activated
if(mouse_check_button_pressed(mb_left)){
	if(in_play and global.player_turn and type == "Equipment" and position_meeting(mouse_x, mouse_y, self) and not global.prompting_player_for_input and global.card_delay_count == 0){
		if(script_am_i_activatable(self)){
			alarm[5] = 1
			script_activate_effect(self)
		}
	}
}

if(mouse_check_button_released(mb_left) and position_meeting(mouse_x, mouse_y, self)){
	if(global.prompting_player_for_input and glowing){
		alarm[5] = 1
		alarm[0] = -2
		script_resolve_effect(self)
	}
}
