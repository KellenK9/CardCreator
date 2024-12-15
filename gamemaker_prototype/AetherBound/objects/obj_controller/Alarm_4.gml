/// @description Delay activation times
// alarms are our way of tracking time. Functions don't have alarms so here we are

if(global.card_delay_card.object_index == obj_card or global.card_delay_card.object_index == obj_champion_card){
	script_activate_effect(global.card_delay_card)
}else{
	script_activate_effect_opponent(global.card_delay_card)
}