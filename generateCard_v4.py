from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import json
import numpy as np
import textwrap
from math import ceil

image_width = 2048
image_height = 2867

colors = {
    "red": (255, 0, 0),
    "pink": (255, 70, 70),
    "blue": (0, 0, 255),
    "green": (0, 255, 0),
    "yellow": (255, 240, 80),
    "white": (255, 255, 255),
    "black": (0, 0, 0),
    "teal": (60, 150, 220),
    "beige": (120, 100, 80),
    "light_beige": (200, 180, 160),
}

fonts = [
    "fonts/Pacifico.ttf",
    "fonts/Lobster_1.3.otf",
    "fonts/LeagueGothic-Regular.otf",
    "fonts/ChunkFive-Regular.otf",
    "fonts/PlayfairDisplay-Black.otf",
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
    card_width = 2048
    health_y = 1800
    name_y = 2550
    description_x = 55
    description_y = 2080
    health_font_size = 200
    name_font_size = 160
    description_font_size = 80
    color_for_font_name = list(colors[dict["color"]])
    color_for_font_description = list(colors["white"])
    longest_name_for_normal_size = 18
    max_description_width = card_width - (description_x * 2)

    current_font = fonts[4]

    # Append font color tuple
    color_for_font_name.append(255)
    color_for_font_description.append(255)
    font_color_name = tuple(color_for_font_name)
    font_color_description = tuple(color_for_font_description)

    # Import artwork and crop
    artwork = Image.open("cropped_images/" + dict["artwork"])
    artwork = artwork.crop(box=(0, 0, image_width, image_height))
    artwork = artwork.convert("RGBA")

    # Import frame
    frame = Image.open("card_frames/champion-frame.png")

    # Add slots
    if dict["slot3"] != "none" and dict["slot3"] != None:
        third_slot = Image.open("card_frames/" + dict["slot3"] + "-right.png")
    if dict["slot2"] != "none" and dict["slot2"] != None:
        second_slot = Image.open("card_frames/" + dict["slot2"] + "-middle.png")
    if dict["slot1"] != "none" and dict["slot1"] != None:
        first_slot = Image.open("card_frames/" + dict["slot1"] + "-left.png")

    # Center and size Text
    name_length = len(dict["card_name"])
    if name_length > longest_name_for_normal_size:
        name_font_size -= ceil(1.5 * (name_length - longest_name_for_normal_size + 4))
        name_y += 2 * (name_length - longest_name_for_normal_size)

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

    name_width = name_obj.textlength(dict["card_name"], font=fnt1)
    health_width = health_obj.textlength(dict["health"], font=fnt2)
    # description_width = description_obj.textlength(wrapped_text, font=fnt3)

    # Make Names smaller if necessary
    i = 0
    while name_width >= max_description_width:
        i += 1
        name_y += 1
        fnt1 = ImageFont.truetype(current_font, name_font_size - i)
        name_width = name_obj.textlength(dict["card_name"], font=fnt1)

    # Wrap Description Text
    lines = []
    current_line = ""
    for word in dict["description"].split(" "):
        test_line = f"{current_line} {word}".strip()
        line_width = description_obj.textlength(test_line, fnt3)
        if len(current_line) > 0:
            if (
                line_width <= max_description_width
                and current_line[len(current_line) - 1] != "."
            ):
                current_line = test_line
            else:
                lines.append(f"{current_line}\n")
                current_line = word
        else:
            current_line = test_line
    if current_line:
        lines.append(current_line)
    wrapped_text = "".join(lines)

    # TODO: Add logic that doesn't add newlines or shrinks description text if the text is too long to fit in the box.

    name_x = (card_width - name_width) / 2
    health_x = (card_width - health_width) / 2
    name_obj.text((name_x, name_y), dict["card_name"], font=fnt1, fill=font_color_name)
    health_obj.text(
        (health_x, health_y), dict["health"], font=fnt2, fill=font_color_name
    )
    description_obj.multiline_text(
        (description_x, description_y),
        wrapped_text,
        font=fnt3,
        fill=font_color_description,
        align="left",
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
    card_width = 2048
    name_y = 2550
    description_x = 55
    description_y = 2080
    name_font_size = 160
    description_font_size = 80
    color_for_font_name = list(colors[dict["color"]])
    if dict["type"] == "air":
        color_for_font_description = list(colors["black"])
    else:
        color_for_font_description = list(colors["white"])
    color_for_font_nums = list(colors[dict["color"]])
    longest_name_for_normal_size = 18
    max_description_width = card_width - (description_x * 2)

    current_font = fonts[4]

    # Center and size Text
    name_length = len(dict["card_name"])
    if name_length > longest_name_for_normal_size:
        name_font_size -= ceil(1.5 * (name_length - longest_name_for_normal_size + 4))
        name_y += 2 * (name_length - longest_name_for_normal_size)

    # Append font color tuple
    color_for_font_name.append(255)
    color_for_font_description.append(255)
    color_for_font_nums.append(255)
    font_color_name = tuple(color_for_font_name)
    font_color_description = tuple(color_for_font_description)
    font_color_nums = tuple(color_for_font_nums)

    # Import artwork and crop
    artwork = Image.open("cropped_images/" + dict["artwork"])
    artwork = artwork.crop(box=(0, 0, image_width, image_height))
    artwork = artwork.convert("RGBA")

    # Import and color frame
    if dict["type"] == "water":
        frame = Image.open("card_frames/water-frame.png")
        icon = Image.open("card_frames/water-icon.png")
    if dict["type"] == "fire":
        frame = Image.open("card_frames/fire-frame.png")
        icon = Image.open("card_frames/fire-icon.png")
    if dict["type"] == "earth":
        frame = Image.open("card_frames/earth-frame.png")
        icon = Image.open("card_frames/earth-icon.png")
    if dict["type"] == "air":
        frame = Image.open("card_frames/air-frame.png")
        icon = Image.open("card_frames/air-icon.png")
    if dict["type"] == "spell":
        frame = Image.open("card_frames/spell-frame.png")
        icon = None
    if dict["type"] == "speed spell":
        frame = Image.open("card_frames/spell-frame.png")
        icon = Image.open("card_frames/speed-icon.png")

    # Add text
    name_txt = Image.new("RGBA", frame.size, (255, 255, 255, 0))
    description_txt = Image.new("RGBA", frame.size, (255, 255, 255, 0))
    fnt1 = ImageFont.truetype(current_font, name_font_size)
    fnt2 = ImageFont.truetype(current_font, description_font_size)
    name_obj = ImageDraw.Draw(name_txt)
    description_obj = ImageDraw.Draw(description_txt)

    name_width = name_obj.textlength(dict["card_name"], font=fnt1)

    # Make Names smaller if necessary
    i = 0
    while name_width >= max_description_width:
        i = i - 1
        name_y += 1
        fnt1 = ImageFont.truetype(current_font, name_font_size - i)
        name_width = name_obj.textlength(dict["card_name"], font=fnt1)

    # Wrap Description Text
    lines = []
    current_line = ""
    for word in dict["description"].split(" "):
        test_line = f"{current_line} {word}".strip()
        line_width = description_obj.textlength(test_line, fnt2)
        if len(current_line) > 0:
            if (
                line_width <= max_description_width
                and current_line[len(current_line) - 1] != "."
            ):
                current_line = test_line
            else:
                lines.append(f"{current_line}\n")
                current_line = word
        else:
            current_line = test_line
    if current_line:
        lines.append(current_line)
    wrapped_text = "".join(lines)

    name_x = (card_width - name_width) / 2
    name_obj.text((name_x, name_y), dict["card_name"], font=fnt1, fill=font_color_name)
    description_obj.multiline_text(
        (description_x, description_y),
        wrapped_text,
        font=fnt2,
        fill=font_color_description,
        align="left",
    )

    # Combine images
    new_image = Image.alpha_composite(artwork, frame)
    new_image = Image.alpha_composite(new_image, name_txt)
    new_image = Image.alpha_composite(new_image, description_txt)
    if icon is not None:
        new_image = Image.alpha_composite(new_image, icon)

    return new_image


# Champions
with open("card_json/first_champions.json", "r", encoding="utf-8") as json_file:
    loaded_json = json.load(json_file)
for card in loaded_json["cards"]:
    generate_card(card).show()
    generate_card(card).save(
        "finished_cards_v3/" + card["card_name"] + "_card.png", "PNG"
    )
with open("card_json/second_champions.json", "r", encoding="utf-8") as json_file:
    loaded_json = json.load(json_file)
for card in loaded_json["cards"]:
    generate_card(card).show()
    generate_card(card).save(
        "finished_cards_v3/" + card["card_name"] + "_card.png", "PNG"
    )

# Fire
with open("card_json/first_equipment_fire.json", "r", encoding="utf-8") as json_file:
    loaded_json = json.load(json_file)
for card in loaded_json["cards"]:
    generate_equipment_card(card).show()
    generate_equipment_card(card).save(
        "finished_cards_v3/" + card["card_name"] + "_card.png", "PNG"
    )
with open("card_json/second_equipment_fire.json", "r", encoding="utf-8") as json_file:
    loaded_json = json.load(json_file)
for card in loaded_json["cards"]:
    generate_equipment_card(card).show()
    generate_equipment_card(card).save(
        "finished_cards_v3/" + card["card_name"] + "_card.png", "PNG"
    )

# Water
with open("card_json/first_equipment_water.json", "r", encoding="utf-8") as json_file:
    loaded_json = json.load(json_file)
for card in loaded_json["cards"]:
    generate_equipment_card(card).show()
    generate_equipment_card(card).save(
        "finished_cards_v3/" + card["card_name"] + "_card.png", "PNG"
    )
with open("card_json/second_equipment_water.json", "r", encoding="utf-8") as json_file:
    loaded_json = json.load(json_file)
for card in loaded_json["cards"]:
    generate_equipment_card(card).show()
    generate_equipment_card(card).save(
        "finished_cards_v3/" + card["card_name"] + "_card.png", "PNG"
    )

# Earth
with open("card_json/first_equipment_earth.json", "r", encoding="utf-8") as json_file:
    loaded_json = json.load(json_file)
for card in loaded_json["cards"]:
    generate_equipment_card(card).show()
    generate_equipment_card(card).save(
        "finished_cards_v3/" + card["card_name"] + "_card.png", "PNG"
    )
with open("card_json/second_equipment_earth.json", "r", encoding="utf-8") as json_file:
    loaded_json = json.load(json_file)
for card in loaded_json["cards"]:
    generate_equipment_card(card).show()
    generate_equipment_card(card).save(
        "finished_cards_v3/" + card["card_name"] + "_card.png", "PNG"
    )

# Air
with open("card_json/first_equipment_air.json", "r", encoding="utf-8") as json_file:
    loaded_json = json.load(json_file)
for card in loaded_json["cards"]:
    generate_equipment_card(card).show()
    generate_equipment_card(card).save(
        "finished_cards_v3/" + card["card_name"] + "_card.png", "PNG"
    )
with open("card_json/second_equipment_air.json", "r", encoding="utf-8") as json_file:
    loaded_json = json.load(json_file)
for card in loaded_json["cards"]:
    generate_equipment_card(card).show()
    generate_equipment_card(card).save(
        "finished_cards_v3/" + card["card_name"] + "_card.png", "PNG"
    )

# Spells
with open("card_json/first_spells.json", "r", encoding="utf-8") as json_file:
    loaded_json = json.load(json_file)
for card in loaded_json["cards"]:
    generate_equipment_card(card).show()
    generate_equipment_card(card).save(
        "finished_cards_v3/" + card["card_name"] + "_card.png", "PNG"
    )
with open("card_json/second_spells.json", "r", encoding="utf-8") as json_file:
    loaded_json = json.load(json_file)
for card in loaded_json["cards"]:
    generate_equipment_card(card).show()
    generate_equipment_card(card).save(
        "finished_cards_v3/" + card["card_name"] + "_card.png", "PNG"
    )


# Third Wave
with open("card_json/third_equipment.json", "r", encoding="utf-8") as json_file:
    loaded_json = json.load(json_file)
for card in loaded_json["cards"]:
    generate_equipment_card(card).show()
    generate_equipment_card(card).save(
        "finished_cards_v3/" + card["card_name"] + "_card.png", "PNG"
    )
with open("card_json/third_champions.json", "r", encoding="utf-8") as json_file:
    loaded_json = json.load(json_file)
for card in loaded_json["cards"]:
    generate_card(card).show()
    generate_card(card).save(
        "finished_cards_v3/" + card["card_name"] + "_card.png", "PNG"
    )
with open("card_json/third_spells.json", "r", encoding="utf-8") as json_file:
    loaded_json = json.load(json_file)
for card in loaded_json["cards"]:
    generate_equipment_card(card).show()
    generate_equipment_card(card).save(
        "finished_cards_v3/" + card["card_name"] + "_card.png", "PNG"
    )

# generate_card(temp_dict).show()
# generate_equipment_card(temp_dict_equipment).show()

# 19 total spells
# 15 total champions
# 7 air equipment
# 7 earth equipment
# 5 fire equipment
# 7 water equipment
# 57 total cards

# Deck Size:
# Air 62
# Water 62
# Earth 62
# Fire 62