from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import json
import numpy as np

image_width = 744
image_height = 1039

colors = {
    "red": (255, 0, 0),
    "blue": (0, 0, 255),
    "green": (0, 255, 0),
    "yellow": (255, 244, 89),
    "white": (255, 255, 255),
    "black": (0, 0, 0),
    "teal": (60, 150, 220)
}

fonts = ["fonts/Pacifico.ttf",
         "fonts/Lobster_1.3.otf",
         "fonts/LeagueGothic-Regular.otf",
         "fonts/ChunkFive-Regular.otf",
         "fonts/PlayfairDisplay-Black.otf"
         ]

#In the final version this will be read in via json
temp_dict = {
    "card_name": "Teddy",
    "health": "80",
    "element": "Water",
    "description": "Ability: attacks cost 2 less stamina",
    "slot1": "helmet",
    "slot2": "sword",
    "slot3": "sword",
    "slot4": "magic",
    "color": "teal",
    "icon_color": "white",
    "artwork": "dragon.jpg"
}

temp_dict_equipment = {
    "card_name": "Poison Dagger",
    "description": "Deal 20 damage",
    "detach_cost": "2",
    "stamina_cost": "3",
    "color": "red",
    "type": "Sword", #Sword or Magic or Helmet
    "symbol_color": "red",
    "artwork": "dragon1.jpg"
}

def generate_card(dict):
    #Coordiantes and font sizes for text locations on card
    #These variables must be adjusted for each font, alongside the code adjusting these variables
    #For the font: PlayfairDisplay-Black
    health_x = 310
    health_y = 410
    name_x = 285
    name_y = 530
    description_x = 50
    description_y = 650
    health_font_size = 90
    name_font_size = 60
    description_font_size = 25
    color_for_font_name = list(colors[dict["color"]])
    color_for_font_description = list(colors["white"])
    description_line_length = 52 #This is the number of characters that can fit on one line, and is dependant upon the font and font size

    current_font = fonts[4]

    #Append font color tuple
    color_for_font_name.append(255)
    color_for_font_description.append(255)
    font_color_name = tuple(color_for_font_name)
    font_color_description = tuple(color_for_font_description)

    #Import artwork and crop
    artwork = Image.open("cropped_images/" + dict["artwork"])
    artwork = artwork.crop(box=(0, 0, 744, 1039))
    artwork = artwork.convert('RGBA')

    #Import and color frame
    frame = Image.open("card_frames/FixedChampionFrame.png")
    data = np.array(frame)
    red, green, blue, alpha = data.T
    white_areas = (red == 255) & (blue == 255) & (green == 255)
    new_color = (0, 0, 0)
    for color in colors:
        if color == dict["color"]:
            new_color = colors[color]
    data[..., :-1][white_areas.T] = new_color
    frame = Image.fromarray(data)

    #Add element
    element = Image.open("card_frames/" + dict["element"] + ".png")

    #Add slots
    first_slot = Image.open("card_frames/1_" + dict["slot1"] + ".png")
    second_slot = Image.open("card_frames/2_" + dict["slot2"] + ".png")
    third_slot = Image.open("card_frames/3_" + dict["slot3"] + ".png")
    fourth_slot = Image.open("card_frames/4_" + dict["slot4"] + ".png")

    #Color slot 1
    data = np.array(first_slot)
    red, green, blue, alpha = data.T
    black_areas = (red == 0) & (blue == 0) & (green == 0)
    new_color = (0, 0, 0)
    for color in colors:
        if color == dict["icon_color"]:
            new_color = colors[color]
    data[..., :-1][black_areas.T] = new_color
    first_slot = Image.fromarray(data)

    # Color slot 2
    data = np.array(second_slot)
    red, green, blue, alpha = data.T
    black_areas = (red == 0) & (blue == 0) & (green == 0)
    new_color = (0, 0, 0)
    for color in colors:
        if color == dict["icon_color"]:
            new_color = colors[color]
    data[..., :-1][black_areas.T] = new_color
    second_slot = Image.fromarray(data)

    # Color slot 3
    data = np.array(third_slot)
    red, green, blue, alpha = data.T
    black_areas = (red == 0) & (blue == 0) & (green == 0)
    new_color = (0, 0, 0)
    for color in colors:
        if color == dict["icon_color"]:
            new_color = colors[color]
    data[..., :-1][black_areas.T] = new_color
    third_slot = Image.fromarray(data)

    # Color slot 4
    data = np.array(fourth_slot)
    red, green, blue, alpha = data.T
    black_areas = (red == 0) & (blue == 0) & (green == 0)
    new_color = (0, 0, 0)
    for color in colors:
        if color == dict["icon_color"]:
            new_color = colors[color]
    data[..., :-1][black_areas.T] = new_color
    fourth_slot = Image.fromarray(data)

    #Center Text
    char_width = 15 #This value may have to be adjusted for different fonts
    name_length = len(dict["card_name"])
    name_x = 360 - (name_length*char_width)

    #Center Health
    health_length = len(dict["health"])
    if(health_length == 2):
        health_x = 320
    if(health_length == 3):
        health_x = 290
    if("1" in dict["health"]):
        health_x += 10
    if("11" in dict["health"]):
        health_x += 5
    if("100" in dict["health"]):
        health_x -= 5

    #Add enters to descriptions
    if(len(dict["description"]) > description_line_length):
        last_line_len = len(dict["description"])
        desc_string = dict["description"]
        new_desc = ""
        while(len(desc_string) > description_line_length):
            last_space_locale = 0
            for char_num in range(description_line_length):
                if desc_string[char_num].isspace():
                    last_space_locale = char_num
            new_desc += str(desc_string[:last_space_locale])
            new_desc += '\n'
            desc_string = desc_string[last_space_locale+1:]
            #find the last space in the first x characters and change it to a line break
        new_desc += str(desc_string)
    else:
        new_desc = dict["description"]

    #Add Text
    name_txt = Image.new("RGBA", frame.size, (255, 255, 255, 0))
    health_txt = Image.new("RGBA", frame.size, (255, 255, 255, 0))
    description_txt = Image.new("RGBA", frame.size, (255, 255, 255, 0))
    fnt1 = ImageFont.truetype(current_font, name_font_size)
    fnt2 = ImageFont.truetype(current_font, health_font_size)
    fnt3 = ImageFont.truetype(current_font, description_font_size)
    name_obj = ImageDraw.Draw(name_txt)
    health_obj = ImageDraw.Draw(health_txt)
    description_obj = ImageDraw.Draw(description_txt)
    name_obj.text((name_x, name_y), dict["card_name"], font=fnt1, fill=font_color_name)
    health_obj.text((health_x, health_y), dict["health"], font=fnt2, fill=font_color_name)
    description_obj.text((description_x, description_y), new_desc, font=fnt3, fill=font_color_description)

    #Combine images
    new_image = Image.alpha_composite(artwork, frame)
    new_image = Image.alpha_composite(new_image, element)
    new_image = Image.alpha_composite(new_image, first_slot)
    new_image = Image.alpha_composite(new_image, second_slot)
    new_image = Image.alpha_composite(new_image, third_slot)
    new_image = Image.alpha_composite(new_image, fourth_slot)
    new_image = Image.alpha_composite(new_image, name_txt)
    new_image = Image.alpha_composite(new_image, health_txt)
    new_image = Image.alpha_composite(new_image, description_txt)

    return new_image


def generate_equipment_card(dict):
    # Coordiantes and font sizes for text locations on card
    # These variables must be adjusted for each font, alongside the code adjusting these variables
    # For the font: PlayfairDisplay-Black
    name_x = 185
    name_y = 530
    description_x = 50
    description_y = 650
    stamina_x = 70
    stamina_y = 800
    detach_x = 640
    detach_y = 875
    name_font_size = 60
    description_font_size = 25
    stamina_font_size = 150
    detach_font_size = 100
    color_for_font_name = list(colors[dict["color"]])
    color_for_font_description = list(colors["white"])
    color_for_font_nums = list(colors[dict["color"]])
    description_line_length = 52  # This is the number of characters that can fit on one line, and is dependant upon the font and font size

    current_font = fonts[4]

    # Center Text
    char_width = 15  # This value may have to be adjusted for different fonts
    name_length = len(dict["card_name"])
    name_x = 360 - (name_length * char_width)

    # Append font color tuple
    color_for_font_name.append(255)
    color_for_font_description.append(255)
    color_for_font_nums.append(255)
    font_color_name = tuple(color_for_font_name)
    font_color_description = tuple(color_for_font_description)
    font_color_nums = tuple(color_for_font_nums)

    # Import artwork and crop
    artwork = Image.open("cropped_images/" + dict["artwork"])
    artwork = artwork.crop(box=(0, 0, 744, 1039))
    artwork = artwork.convert('RGBA')

    # Import and color frame
    frame = Image.open("card_frames/EquipFrame.png")
    data = np.array(frame)
    red, green, blue, alpha = data.T
    white_areas = (red != 0) & (blue != 0) & (green != 0)
    new_color = (0, 0, 0)
    for color in colors:
        if color == dict["color"]:
            new_color = colors[color]
    data[..., :-1][white_areas.T] = new_color
    frame = Image.fromarray(data)

    #Import Equipment Type symbol
    type_symbol = Image.open("card_frames/Equip" + dict["type"] + ".png")
    data = np.array(type_symbol)
    red, green, blue, alpha = data.T
    black_areas = (red == 0) & (blue == 0) & (green == 0)
    new_color = (0, 0, 0)
    for color in colors:
        if color == dict["symbol_color"]:
            new_color = colors[color]
    data[..., :-1][black_areas.T] = new_color
    type_symbol = Image.fromarray(data)

    #Adjust stamina cost location
    if("1" in dict["stamina_cost"]):
        stamina_x += 5
        stamina_y += 5
    if("*" == dict["stamina_cost"]):
        stamina_y += 42
        stamina_x += 3
    if ("0" in dict["stamina_cost"]):
        stamina_x -= 10
        stamina_y += 5
    if ("6" in dict["stamina_cost"]):
        stamina_x -= 8
        stamina_y += 15
    if("2" in dict["stamina_cost"]):
        stamina_x -= 5
        stamina_y += 5
    #Adjust detach cost location
    if("2" in dict["detach_cost"]):
        detach_y += 5
    if("0" in dict["detach_cost"]):
        detach_y += 5
        detach_x -= 5
    if("1" in dict["detach_cost"]):
        detach_x += 8
    if("8" in dict["detach_cost"]):
        detach_y += 10

    # Add enters to descriptions
    if (len(dict["description"]) > description_line_length):
        last_line_len = len(dict["description"])
        desc_string = dict["description"]
        new_desc = ""
        while (len(desc_string) > description_line_length):
            last_space_locale = 0
            for char_num in range(description_line_length):
                if desc_string[char_num].isspace():
                    last_space_locale = char_num
            new_desc += str(desc_string[:last_space_locale])
            new_desc += '\n'
            desc_string = desc_string[last_space_locale+1:]
            # find the last space in the first x characters and change it to a line break
        new_desc += str(desc_string)
    else:
        new_desc = dict["description"]

    #Move long names to the left
    if(len(dict["card_name"]) > 14):
        name_x -= ((len(dict["card_name"])-14)*15)

    #Add text
    name_txt = Image.new("RGBA", frame.size, (255, 255, 255, 0))
    description_txt = Image.new("RGBA", frame.size, (255, 255, 255, 0))
    stamina_txt = Image.new("RGBA", frame.size, (255, 255, 255, 0))
    detach_txt = Image.new("RGBA", frame.size, (255, 255, 255, 0))
    fnt1 = ImageFont.truetype(current_font, name_font_size)
    fnt2 = ImageFont.truetype(current_font, description_font_size)
    fnt3 = ImageFont.truetype(current_font, stamina_font_size)
    fnt4 = ImageFont.truetype(current_font, detach_font_size)
    name_obj = ImageDraw.Draw(name_txt)
    description_obj = ImageDraw.Draw(description_txt)
    stamina_obj = ImageDraw.Draw(stamina_txt)
    detach_obj = ImageDraw.Draw(detach_txt)
    name_obj.text((name_x, name_y), dict["card_name"], font=fnt1, fill=font_color_name)
    description_obj.text((description_x, description_y), new_desc, font=fnt2, fill=font_color_description)
    stamina_obj.text((stamina_x, stamina_y), dict["stamina_cost"], font=fnt3, fill=font_color_nums)
    detach_obj.text((detach_x, detach_y), dict["detach_cost"], font=fnt4, fill=font_color_nums)

    # Combine images
    new_image = Image.alpha_composite(artwork, frame)
    new_image = Image.alpha_composite(new_image, type_symbol)
    new_image = Image.alpha_composite(new_image, name_txt)
    new_image = Image.alpha_composite(new_image, description_txt)
    new_image = Image.alpha_composite(new_image, stamina_txt)
    new_image = Image.alpha_composite(new_image, detach_txt)

    return new_image

with open("card_json/first_fire_equipment.txt") as json_file:
    loaded_json = json.load(json_file)
    for card in loaded_json["cards"]:
        generate_equipment_card(card).show()
        #generate_equipment_card(card).save("finished_cards/" + card["card_name"] + "_card.png", "PNG")