/// 

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

if(showing_zoomed_card){
	draw_sprite(spr_zoom_filter, 0, 0, 0)
	draw_sprite(spr_to_show, 0, zoomed_x, zoomed_y)
}
