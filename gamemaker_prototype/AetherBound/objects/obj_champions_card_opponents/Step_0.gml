/// Adjust Vars

if(current_health < 100){
	gui_x = x + gui_x_offset + gui_health_shift_x
}else{
	gui_x = x + gui_x_offset
}
gui_y = y + gui_y_offset

if(mouse_check_button_released(mb_left) and position_meeting(mouse_x, mouse_y, self)){
	if(global.prompting_player_for_input and glowing){
		alarm[5] = 1
		script_resolve_effect(self)
	}
}

if(current_health <= 0){
	for (var _i = 0; _i < instance_number(obj_card_opponents); ++_i;){
		curr_card = instance_find(obj_card_opponents, _i)
		if(curr_card.in_play and distance_to_point(curr_card.x, curr_card.y) < equipped_distance_threshold){
			curr_card.alarm[3] = 30
		}
	}
	if(num_equip_slots >= 1){
		instance_destroy(equipment_slot1)
		if(num_equip_slots >= 2){
			instance_destroy(equipment_slot2)
		}
	}
	instance_destroy(self)
}

//Check if health changed
if(current_health < latest_health){
	took_damage = true
	latest_health = current_health
}
if(current_health > latest_health){
	healed = true
	latest_health = current_health
}

//Glow red if took damage recently
if(took_damage){
	green_shade = green_shade - 5
	blue_shade = blue_shade - 5
	if(alarm[1] <= 0){
		alarm[1] = 40
	}
}
else{
	if(green_shade < 255){
		green_shade = green_shade + 5
		blue_shade = blue_shade + 5
	}
}
//Glow green if healed recently
if(healed){
	red_shade = red_shade - 5
	blue_shade = blue_shade - 5
	if(alarm[1] <= 0){
		alarm[1] = 40
	}
}
else{
	if(red_shade < 255){
		red_shade = red_shade + 5
		blue_shade = blue_shade + 5
	}
}

if(card_name == "Technician Magician"){
	if(current_health < max_health){
		if(not technician_activated){
			script_activate_effect_opponent(self)
			technician_activated = true
			alarm[5] = 1
		}
	}
}
