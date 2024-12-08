/// @description Move to Hand

if(curr_x == 0 and curr_y == 0){
	curr_x = global.hand_x
	curr_y = global.hand_y
}
move_towards_point(curr_x, curr_y, 10)