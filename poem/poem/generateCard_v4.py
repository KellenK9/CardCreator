from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import json
import numpy as np
from math import ceil

image_width = 2048
image_height = 2867

colors = {
    "red": (255, 0, 0),
    "blue": (0, 0, 255),
    "green": (0, 255, 0),
    "yellow": (255, 244, 89),
    "white": (255, 255, 255),
    "black": (0, 0, 0),
    "teal": (60, 150, 220),
    "beige": (120, 100, 80),
}

fonts = [
    "poem/poem/fonts/Pacifico.ttf",
    "poem/poem/fonts/Lobster_1.3.otf",
    "poem/poem/fonts/LeagueGothic-Regular.otf",
    "poem/poem/fonts/ChunkFive-Regular.otf",
    "poem/poem/fonts/PlayfairDisplay-Black.otf",
]

# In the final version this will be read in via json
temp_dict = {
    "card_name": "Teddy",
    "health": "80",
    "description": "",
    "slot1": "water",
    "slot2": "water",
    "slot3": "none",
    "color": "teal",
    "artwork": "fountain.png",
}

temp_dict_equipment = {
    "card_name": "Fountain of Youth",
    "description": "Heal 20 damage",
    "color": "white",
    "type": "water",
    "artwork": "fountain.png",
}


def generate_card(dict):
    # Coordiantes and font sizes for text locations on card
    # These variables must be adjusted for each font, alongside the code adjusting these variables
    # For the font: PlayfairDisplay-Black
    health_x = 900
    health_y = 1800
    name_x = 950
    name_y = 2600
    description_x = 55
    description_y = 2080
    health_font_size = 200
    name_font_size = 120
    description_font_size = 60
    color_for_font_name = list(colors[dict["color"]])
    color_for_font_description = list(colors["white"])
    description_line_length = 52  # This is the number of characters that can fit on one line, and is dependant upon the font and font size
    longest_name_for_normal_size = 18

    current_font = fonts[4]

    # Append font color tuple
    color_for_font_name.append(255)
    color_for_font_description.append(255)
    font_color_name = tuple(color_for_font_name)
    font_color_description = tuple(color_for_font_description)

    # Import artwork and crop
    artwork = Image.open("poem/poem/cropped_images/" + dict["artwork"])
    artwork = artwork.crop(box=(0, 0, image_width, image_height))
    artwork = artwork.convert("RGBA")

    # Import frame
    frame = Image.open("poem/poem/card_frames/champion-frame.png")

    # Add slots
    if dict["slot3"] != "none" and dict["slot3"] != None:
        third_slot = Image.open("poem/poem/card_frames/" + dict["slot3"] + "-right.png")
    if dict["slot2"] != "none" and dict["slot2"] != None:
        second_slot = Image.open(
            "poem/poem/card_frames/" + dict["slot2"] + "-middle.png"
        )
    if dict["slot1"] != "none" and dict["slot1"] != None:
        first_slot = Image.open("poem/poem/card_frames/" + dict["slot1"] + "-left.png")

    # Center and size Text
    char_width = 15  # This value may have to be adjusted for different fonts
    name_length = len(dict["card_name"])
    name_x -= name_length * char_width
    if name_length > longest_name_for_normal_size:
        name_font_size -= ceil(1.5 * (name_length - longest_name_for_normal_size + 4))
        name_y += 2 * (name_length - longest_name_for_normal_size)
        name_x += 30 * (name_length - longest_name_for_normal_size + 1)

    # Center Health
    health_length = len(dict["health"])
    if health_length == 3:
        health_x -= 50
    if "1" in dict["health"]:
        health_x += 10
    if "11" in dict["health"]:
        health_x += 5
    if "100" in dict["health"]:
        health_x -= 5
    if "8" in dict["health"]:
        health_y += 4

    # Add enters to descriptions
    if len(dict["description"]) > description_line_length:
        last_line_len = len(dict["description"])
        desc_string = dict["description"]
        new_desc = ""
        while len(desc_string) > description_line_length:
            last_space_locale = 0
            for char_num in range(description_line_length):
                if desc_string[char_num].isspace():
                    last_space_locale = char_num
            new_desc += str(desc_string[:last_space_locale])
            new_desc += "\n"
            desc_string = desc_string[last_space_locale + 1 :]
            # find the last space in the first x characters and change it to a line break
        new_desc += str(desc_string)
    else:
        new_desc = dict["description"]

    # Add Text
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
    health_obj.text(
        (health_x, health_y), dict["health"], font=fnt2, fill=font_color_name
    )
    description_obj.text(
        (description_x, description_y), new_desc, font=fnt3, fill=font_color_description
    )

    # Combine images
    new_image = Image.alpha_composite(artwork, frame)
    if dict["slot1"] != "none" and dict["slot1"] != None:
        new_image = Image.alpha_composite(new_image, first_slot)
    if dict["slot2"] != "none" and dict["slot2"] != None:
        new_image = Image.alpha_composite(new_image, second_slot)
    if dict["slot3"] != "none" and dict["slot3"] != None:
        new_image = Image.alpha_composite(new_image, third_slot)
    new_image = Image.alpha_composite(new_image, name_txt)
    new_image = Image.alpha_composite(new_image, health_txt)
    new_image = Image.alpha_composite(new_image, description_txt)

    return new_image


def generate_equipment_card(dict):
    # Coordiantes and font sizes for text locations on card
    # These variables must be adjusted for each font, alongside the code adjusting these variables
    # For the font: PlayfairDisplay-Black
    name_x = 950
    name_y = 2600
    description_x = 55
    description_y = 2080
    name_font_size = 120
    description_font_size = 60
    color_for_font_name = list(colors[dict["color"]])
    color_for_font_description = list(colors["white"])
    color_for_font_nums = list(colors[dict["color"]])
    description_line_length = 52  # This is the number of characters that can fit on one line, and is dependant upon the font and font size
    longest_name_for_normal_size = 18

    current_font = fonts[4]

    # Center and size Text
    char_width = 15  # This value may have to be adjusted for different fonts
    name_length = len(dict["card_name"])
    name_x -= name_length * char_width
    if name_length > longest_name_for_normal_size:
        name_font_size -= ceil(1.5 * (name_length - longest_name_for_normal_size + 4))
        name_y += 2 * (name_length - longest_name_for_normal_size)
        name_x += 30 * (name_length - longest_name_for_normal_size + 1)

    # Append font color tuple
    color_for_font_name.append(255)
    color_for_font_description.append(255)
    color_for_font_nums.append(255)
    font_color_name = tuple(color_for_font_name)
    font_color_description = tuple(color_for_font_description)
    font_color_nums = tuple(color_for_font_nums)

    # Import artwork and crop
    artwork = Image.open("poem/poem/cropped_images/" + dict["artwork"])
    artwork = artwork.crop(box=(0, 0, image_width, image_height))
    artwork = artwork.convert("RGBA")

    # Import and color frame
    if dict["type"] == "water":
        frame = Image.open("poem/poem/card_frames/water-frame.png")
        icon = Image.open("poem/poem/card_frames/water-icon.png")
    if dict["type"] == "fire":
        frame = Image.open("poem/poem/card_frames/fire-frame.png")
        icon = Image.open("poem/poem/card_frames/fire-icon.png")
    if dict["type"] == "earth":
        frame = Image.open("poem/poem/card_frames/earth-frame.png")
        icon = Image.open("poem/poem/card_frames/earth-icon.png")
    if dict["type"] == "air":
        frame = Image.open("poem/poem/card_frames/air-frame.png")
        icon = Image.open("poem/poem/card_frames/air-icon.png")
    if dict["type"] == "spell":
        frame = Image.open("poem/poem/card_frames/spell-frame.png")
        icon = None
    if dict["type"] == "speed spell":
        frame = Image.open("poem/poem/card_frames/spell-frame.png")
        icon = Image.open("poem/poem/card_frames/speed-icon.png")

    # Add enters to descriptions
    if len(dict["description"]) > description_line_length:
        last_line_len = len(dict["description"])
        desc_string = dict["description"]
        new_desc = ""
        while len(desc_string) > description_line_length:
            last_space_locale = 0
            for char_num in range(description_line_length):
                if desc_string[char_num].isspace():
                    last_space_locale = char_num
            new_desc += str(desc_string[:last_space_locale])
            new_desc += "\n"
            desc_string = desc_string[last_space_locale + 1 :]
            # find the last space in the first x characters and change it to a line break
        new_desc += str(desc_string)
    else:
        new_desc = dict["description"]

    # Move long names to the left
    if len(dict["card_name"]) > 14:
        name_x -= (len(dict["card_name"]) - 14) * 15

    # Add text
    name_txt = Image.new("RGBA", frame.size, (255, 255, 255, 0))
    description_txt = Image.new("RGBA", frame.size, (255, 255, 255, 0))
    fnt1 = ImageFont.truetype(current_font, name_font_size)
    fnt2 = ImageFont.truetype(current_font, description_font_size)
    name_obj = ImageDraw.Draw(name_txt)
    description_obj = ImageDraw.Draw(description_txt)
    name_obj.text((name_x, name_y), dict["card_name"], font=fnt1, fill=font_color_name)
    description_obj.text(
        (description_x, description_y), new_desc, font=fnt2, fill=font_color_description
    )

    # Combine images
    new_image = Image.alpha_composite(artwork, frame)
    new_image = Image.alpha_composite(new_image, name_txt)
    new_image = Image.alpha_composite(new_image, description_txt)
    if icon is not None:
        new_image = Image.alpha_composite(new_image, icon)

    return new_image


with open("poem/poem/card_json/first_champions.txt") as json_file:
    loaded_json = json.load(json_file)
for card in loaded_json["cards"]:
    generate_card(card).show()
    generate_card(card).save(
        "poem/poem/finished_cards_v3/" + card["card_name"] + "_card.png", "PNG"
    )
with open("poem/poem/card_json/second_champions.txt") as json_file:
    loaded_json = json.load(json_file)
for card in loaded_json["cards"]:
    generate_card(card).show()
    generate_card(card).save(
        "poem/poem/finished_cards_v3/" + card["card_name"] + "_card.png", "PNG"
    )

with open("poem/poem/card_json/first_equipment_fire.txt") as json_file:
    loaded_json = json.load(json_file)
for card in loaded_json["cards"]:
    generate_equipment_card(card).show()
    generate_equipment_card(card).save(
        "poem/poem/finished_cards_v3/" + card["card_name"] + "_card.png", "PNG"
    )

# generate_card(temp_dict).show()
# generate_equipment_card(temp_dict_equipment).show()

# 19 total spells
# 14 total champions   X
# 7 air equipment
# 6 earth equipment    X
# 5 fire equipment     X
# 6 water equipment    X
# 57 total cards
