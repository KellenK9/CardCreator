/// Draw Background

draw_sprite(spr_hand_and_menu_area, 0, room_width, 0)

if(global.holding_card){
	if(global.card_held.type == "Spell"){
		if(mouse_x < sprite_get_width(spr_field_border)){
			draw_sprite(spr_field_border, 1, 0, 0)
		}
		else{
			draw_sprite(spr_field_border, 0, 0, 0)
		}
	}
}