/// Draw Background

draw_sprite(spr_hand_and_menu_area, 0, room_width, 0)

if(global.holding_card){
	draw_sprite(spr_eligible_equip_slot, 0, 100, 930)
	draw_sprite(spr_eligible_equip_slot, 0, 290, 930)
	draw_sprite(spr_eligible_equip_slot, 0, 500, 930)
	draw_sprite(spr_eligible_equip_slot, 0, 690, 930)
	draw_sprite(spr_eligible_equip_slot, 0, 900, 930)
	draw_sprite(spr_eligible_equip_slot, 0, 1090, 930)
}