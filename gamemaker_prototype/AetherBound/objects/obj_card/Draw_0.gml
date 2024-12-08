/// @description 

if(in_play and global.player_turn and type == "Equipment"){
	if(script_am_i_activatable(self)){
		draw_sprite(spr_glow_effect, 1, x, y)
	}
}
if(not in_play and global.player_turn){
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
