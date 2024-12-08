// Script assets have changed for v2.3.0 see
// https://help.yoyogames.com/hc/en-us/articles/360005277377 for more information
function script_draw_card(starting_x, starting_y){
	global.hand_size = global.hand_size + 1
	card_drawn_name = string(array_pop(global.deck_shuffled))
	sprite_instance = script_convert_name_sprite(card_drawn_name)
	card_drawn = instance_create_depth(starting_x, starting_y, -1, obj_card)
	card_drawn.card_name = card_drawn_name
	card_drawn.sprite_index = sprite_instance
}