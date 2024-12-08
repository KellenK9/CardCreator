/// @description 

if(mouse_check_button_released(mb_left) and global.holding_card and global.player_turn and not slot_filled){
	if(global.card_held.type == "Equipment"){
		if(global.card_held.element == slot_type){
			if(point_distance(mouse_x, mouse_y, x, y) < global.equip_distance_threshold or point_distance(mouse_x, mouse_y, x, y-global.equip_distance_threshold) < global.equip_distance_threshold){
				// Play Equipment
				global.playing_equipment = true
				global.equip_slot_coord_recent = [x, y]
				slot_filled = true
			}
		}
	}
}