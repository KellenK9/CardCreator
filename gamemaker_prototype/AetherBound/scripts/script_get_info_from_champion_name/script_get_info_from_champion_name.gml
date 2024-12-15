// Script assets have changed for v2.3.0 see
// https://help.yoyogames.com/hc/en-us/articles/360005277377 for more information
function script_get_info_from_champion_name(_champion_name){
	// num_slots, element, health
	if(_champion_name == "Water Golem"){
		return [2, "Water", 100]
	}
	if(_champion_name == "Fire Golem"){
		return [2, "Fire", 100]
	}
	if(_champion_name == "Poseidon"){
		return [1, "Water", 150]
	}
	if(_champion_name == "Hades"){
		return [1, "Fire", 150]
	}
	if(_champion_name == "Technician Magician"){
		return [2, "Fire", 90]
	}
	if(_champion_name == "Pirate Lord Jandreps"){
		return [1, "Water", 110]
	}
}