// Script assets have changed for v2.3.0 see
// https://help.yoyogames.com/hc/en-us/articles/360005277377 for more information
function script_draw_card_opponent(){
	global.opponent_hand_size = global.opponent_hand_size + 1
	card_drawn_name = string(array_pop(global.opponent_deck_shuffled))
	sprite_instance = script_convert_name_sprite(card_drawn_name)
	card_drawn = instance_create_depth(150, -140, -1, obj_card_opponents)
	card_drawn.card_name = card_drawn_name
	card_drawn.sprite_index = sprite_instance
}