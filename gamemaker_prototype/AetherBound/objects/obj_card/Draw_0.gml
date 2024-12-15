/// @description 

if(in_play and global.player_turn and type == "Equipment" and not global.prompting_player_for_input and not global.game_over and not global.holding_card and global.card_delay_count == 0){
	if(script_am_i_activatable(self)){
		draw_sprite(spr_glow_effect, 1, x, y)
	}
}
if(not in_play and global.player_turn and not global.prompting_player_for_input and not global.game_over and not global.holding_card and global.card_delay_count == 0){
	if(type == "Spell"){
		if(script_am_i_activatable(self)){
			draw_sprite(spr_glow_effect, 1, x, y)
		}
	}
	if(type == "Equipment"){
		for (var _i = 0; _i < instance_number(obj_equipment_slot); ++_i;){
			curr_slot = instance_find(obj_equipment_slot, _i)
			if(not curr_slot.slot_filled and curr_slot.slot_type == element){
				draw_sprite(spr_glow_effect, 1, x, y)
			}
		}
	}
}

if(glowing){
	draw_sprite(spr_glow_effect, 1, x, y)
}

if(activation_effect_opacity > 0){
	draw_sprite_ext(self.sprite_index, 0, x, y, global.activation_effect_scale - (activation_effect_opacity / global.activation_effect_duration), global.activation_effect_scale - (activation_effect_opacity / global.activation_effect_duration), 0, -1, activation_effect_opacity / global.activation_effect_duration)
	activation_effect_opacity = activation_effect_opacity - 1
}

draw_self()
