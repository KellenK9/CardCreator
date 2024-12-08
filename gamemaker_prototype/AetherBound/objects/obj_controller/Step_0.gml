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
if(mouse_check_button_released(mb_left) and global.holding_card and global.player_turn){
	if(global.card_held.type == "Spell"){
		if(mouse_x < sprite_get_width(spr_field_border)){
			// Play spell
			if(script_am_i_activatable(global.card_held)){
				global.playing_spell = true
				script_activate_effect(global.card_held)
			}
		}
	}
}

// Make move for cpu
if(global.game_start and not global.player_turn and alarm[1] < 0){
	alarm[1] = 100
}

//End Game if Champions are defeated
if(instance_number(obj_champion_card) == 0){
	global.game_over = true
	global.player_won = false
}
if(instance_number(obj_champions_card_opponents) == 0){
	global.game_over = true
	global.player_won = true
}
