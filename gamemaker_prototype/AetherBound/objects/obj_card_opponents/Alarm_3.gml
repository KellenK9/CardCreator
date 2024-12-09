/// @description move to grave

grave1 = instance_find(obj_grave, 0)
grave2 = instance_find(obj_grave, 1)
if(grave1.player_grave){
	cpu_grave_x = grave2.x
	cpu_grave_y = grave2.y
}
else{
	cpu_grave_x = grave1.x
	cpu_grave_y = grave1.y
}
move_towards_point(cpu_grave_x, cpu_grave_y, 10)
moving_towards_grave = true