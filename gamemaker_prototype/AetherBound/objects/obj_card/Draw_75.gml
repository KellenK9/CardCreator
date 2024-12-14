/// @description Draw self over health

if(being_held or speed > 0 or alarm[0] > 0 or alarm[3] > 0){
	if(in_play and global.player_turn and type == "Equipment" and not global.prompting_player_for_input and not global.game_over and not global.holding_card){
		if(script_am_i_activatable(self)){
			draw_sprite(spr_glow_effect, 1, x, y)
		}
	}
	if(not in_play and global.player_turn and not global.prompting_player_for_input and not global.game_over and not global.holding_card){
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
	draw_self()
}