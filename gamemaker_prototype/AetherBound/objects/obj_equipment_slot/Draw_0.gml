/// @description draw self

if(global.holding_card and not slot_filled){
	if(global.card_held.type == "Equipment"){
		if(global.card_held.element == slot_type){
			if(point_distance(mouse_x, mouse_y, x, y) < global.equip_distance_threshold or point_distance(mouse_x, mouse_y, x, y-global.equip_distance_threshold) < global.equip_distance_threshold){
				image_index = 1
			}
			else{
				image_index = 0
			}
			draw_self()
		}
	}
}