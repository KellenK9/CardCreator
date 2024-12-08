/// @description move to grave

grave1 = instance_find(obj_grave, 0)
grave2 = instance_find(obj_grave, 1)
if(grave1.player_grave){
	player_grave_x = grave1.x
	player_grave_y = grave1.y
}
else{
	player_grave_x = grave2.x
	player_grave_y = grave2.y
}
move_towards_point(player_grave_x, player_grave_y, 10)
moving_towards_grave = true