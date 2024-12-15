/// Draw Upside down

image_angle = 180
image_blend = make_colour_rgb(red_shade, green_shade, blue_shade)

if(glowing){
	draw_sprite(spr_glow_effect, 1, x, y)
}

if(activation_effect_opacity > 0){
	draw_sprite_ext(self.sprite_index, 0, x, y, global.activation_effect_scale - (activation_effect_opacity / global.activation_effect_duration), global.activation_effect_scale - (activation_effect_opacity / global.activation_effect_duration), 180, -1, activation_effect_opacity / global.activation_effect_duration)
	activation_effect_opacity = activation_effect_opacity - 1
}

draw_self()