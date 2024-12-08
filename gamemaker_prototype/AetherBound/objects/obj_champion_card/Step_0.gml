/// Adjust Vars

gui_x = x + gui_x_offset
gui_y = y + gui_y_offset

if(mouse_check_button_released(mb_left) and position_meeting(mouse_x, mouse_y, self)){
	if(global.prompting_player_for_input and glowing){
		script_resolve_equipment_effect(self)
	}
}
