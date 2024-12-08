/// Draw Background

draw_sprite(spr_hand_and_menu_area, 0, room_width, 0)

if(global.holding_card){
	if(global.card_held.type == "Equipment"){
		for(var _i = 0; _i < equip_array_length; ++_i){
			if(point_distance(mouse_x, mouse_y, equip_slot_x_values[_i], 930) < equip_distance_threshold or point_distance(mouse_x, mouse_y, equip_slot_x_values[_i], 930-equip_distance_threshold) < equip_distance_threshold){
				draw_sprite(spr_eligible_equip_slot, 1, equip_slot_x_values[_i], 930)
			}
			else{
				draw_sprite(spr_eligible_equip_slot, 0, equip_slot_x_values[_i], 930)
			}
		}
	}
	if(global.card_held.type == "Spell"){
		if(mouse_x < sprite_get_width(spr_field_border)){
			draw_sprite(spr_field_border, 1, 0, 0)
		}
		else{
			draw_sprite(spr_field_border, 0, 0, 0)
		}
	}
}