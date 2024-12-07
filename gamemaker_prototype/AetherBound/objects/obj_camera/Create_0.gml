/// @desc Initialize
total_scale = 6

y_offset = 100

view_width=1920/total_scale
view_height=1080/total_scale

window_scale=total_scale;

window_set_size(view_width*window_scale,view_height*window_scale)
alarm[0]=1

surface_resize(application_surface,view_width*window_scale,view_height*window_scale)

//scales_arr = [40, 30, 24, 20, 15, 12, 10, 8, 6, 5, 4, 3, 2, 1]
//scale_pos = 0; //can range from 0 to 13

window_set_fullscreen(true)
