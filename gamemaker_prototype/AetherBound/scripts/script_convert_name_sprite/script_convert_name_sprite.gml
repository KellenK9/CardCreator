// Script assets have changed for v2.3.0 see
// https://help.yoyogames.com/hc/en-us/articles/360005277377 for more information
function script_convert_name_sprite(_card_name){
	return asset_get_index(string_concat("spr_", string_lower(string_replace_all(_card_name," ","_"))))
}