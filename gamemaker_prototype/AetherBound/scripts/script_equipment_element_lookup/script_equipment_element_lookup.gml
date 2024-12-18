// Script assets have changed for v2.3.0 see
// https://help.yoyogames.com/hc/en-us/articles/360005277377 for more information
function script_equipment_element_lookup(_equipment_card_obj){
	curr_card_name = _equipment_card_obj.card_name
	fire_equipment = ["Fire Dagger"]
	water_equipment = ["Water Dagger", "The Sacred Spring", "Sirens Echo Mk. IV"]
	earth_equipment = []
	if(array_contains(fire_equipment,curr_card_name)){
		_equipment_card_obj.element = "Fire"
	}else{
		if(array_contains(water_equipment,curr_card_name)){
		_equipment_card_obj.element = "Water"
	}else{
		if(array_contains(earth_equipment,curr_card_name)){
		_equipment_card_obj.element = "Earth"
	}else{
		_equipment_card_obj.element = "Air"
	}
	}
	}
}