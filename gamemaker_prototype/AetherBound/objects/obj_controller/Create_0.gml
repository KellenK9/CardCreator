/// Set Vars

clicking_button = false
showing_zoomed_card = false

zoomed_card_width = 771
zoomed_x = (1920 - zoomed_card_width) / 2
zoomed_y = 0

zoomed_left_border_x = zoomed_x
zoomed_right_border_x = 1920 - zoomed_x

global.equip_distance_threshold = 95
//equip_slot_x_values = [100, 290, 500, 690, 900, 1090]
//equip_array_length = array_length(equip_slot_x_values)

// Set global vars
global.holding_card = false
global.player_turn = false
global.game_over = false
global.game_start = false
global.player_won = false
global.starting_hand_size = 7
global.hand_size = 0
global.opponent_hand_size = 0
global.hand_x = 1500 + (global.hand_size * 16)
global.hand_y = 200 + (global.hand_size * 4)
global.playing_equipment = false
global.playing_spell = false
global.prompting_player_for_input = false
alarm[0] = 10
alarm[1] = -2

// Create Graves and Decks
player_grave = instance_create_depth(1280, 660, 0, obj_grave)
player_grave.player_grave = true
cpu_grave = instance_create_depth(100, 390, 0, obj_grave)
cpu_grave.player_grave = false
player_deck = instance_create_depth(1280, 930, 0, obj_deck)
player_deck.player_deck = true
cpu_deck = instance_create_depth(100, 140, 0, obj_deck)
cpu_deck.player_deck = false
// Create player's Champions
instance_create_depth(200, 660, 0, obj_champion_card)
instance_create_depth(600, 660, 0, obj_champion_card)
instance_create_depth(1000, 660, 0, obj_champion_card)
// Create opponent's Champions
instance_create_depth(380, 390, 0, obj_champions_card_opponents)
instance_create_depth(780, 390, 0, obj_champions_card_opponents)
instance_create_depth(1180, 390, 0, obj_champions_card_opponents)
