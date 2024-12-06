from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import json
from math import ceil


class CardCreator:
    def __init__(self):
        self.image_width = 2048
        self.image_height = 2867
        self.name_y = 2550
        self.description_x = 55
        self.description_y = 2080
        self.name_font_size = 160
        self.description_font_size = 80
        self.longest_name_for_normal_size = 18
        self.max_description_width = self.image_width - (self.description_x * 2)

        self.colors = {
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

        self.fonts = [
            "fonts/Pacifico.ttf",
            "fonts/Lobster_1.3.otf",
            "fonts/LeagueGothic-Regular.otf",
            "fonts/ChunkFive-Regular.otf",
            "fonts/PlayfairDisplay-Black.otf",
        ]

        self.current_font = self.fonts[4]

    def generate_champion_card(self, dict):
        # Set Champion specific Vars
        health_y = 1800
        health_font_size = 200
        color_for_font_name = list(self.colors[dict["color"]])
        color_for_font_description = list(self.colors["white"])

        # Append font color tuple
        color_for_font_name.append(255)
        color_for_font_description.append(255)
        font_color_name = tuple(color_for_font_name)
        font_color_description = tuple(color_for_font_description)

        # Import artwork and crop
        artwork = Image.open("cropped_images/" + dict["artwork"])
        artwork = artwork.crop(box=(0, 0, self.image_width, self.image_height))
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
        if name_length > self.longest_name_for_normal_size:
            self.name_font_size -= ceil(
                1.5 * (name_length - self.longest_name_for_normal_size + 4)
            )
            self.name_y += 2 * (name_length - self.longest_name_for_normal_size)

        # Add Text
        name_txt = Image.new("RGBA", frame.size, (255, 255, 255, 0))
        health_txt = Image.new("RGBA", frame.size, (255, 255, 255, 0))
        description_txt = Image.new("RGBA", frame.size, (255, 255, 255, 0))
        fnt1 = ImageFont.truetype(self.current_font, self.name_font_size)
        fnt2 = ImageFont.truetype(self.current_font, health_font_size)
        fnt3 = ImageFont.truetype(self.current_font, self.description_font_size)
        name_obj = ImageDraw.Draw(name_txt)
        health_obj = ImageDraw.Draw(health_txt)
        description_obj = ImageDraw.Draw(description_txt)

        name_width = name_obj.textlength(dict["card_name"], font=fnt1)
        health_width = health_obj.textlength(dict["health"], font=fnt2)
        # description_width = description_obj.textlength(wrapped_text, font=fnt3)

        # Make Names smaller if necessary
        i = 0
        while name_width >= self.max_description_width:
            i += 1
            self.name_y += 1
            fnt1 = ImageFont.truetype(self.current_font, self.name_font_size - i)
            name_width = name_obj.textlength(dict["card_name"], font=fnt1)

        # Wrap Description Text
        lines = []
        current_line = ""
        for word in dict["description"].split(" "):
            test_line = f"{current_line} {word}".strip()
            line_width = description_obj.textlength(test_line, fnt3)
            if len(current_line) > 0:
                if (
                    line_width <= self.max_description_width
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

        name_x = (self.image_width - name_width) / 2
        health_x = (self.image_width - health_width) / 2
        name_obj.text(
            (name_x, self.name_y), dict["card_name"], font=fnt1, fill=font_color_name
        )
        health_obj.text(
            (health_x, health_y), dict["health"], font=fnt2, fill=font_color_name
        )
        description_obj.multiline_text(
            (self.description_x, self.description_y),
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

    def generate_equipment_or_spell_card(self, dict):
        color_for_font_name = list(self.colors[dict["color"]])
        if dict["type"] == "air":
            color_for_font_description = list(self.colors["black"])
        else:
            color_for_font_description = list(self.colors["white"])
        color_for_font_nums = list(self.colors[dict["color"]])

        # Center and size Text
        name_length = len(dict["card_name"])
        if name_length > self.longest_name_for_normal_size:
            self.name_font_size -= ceil(
                1.5 * (name_length - self.longest_name_for_normal_size + 4)
            )
            self.name_y += 2 * (name_length - self.longest_name_for_normal_size)

        # Append font color tuple
        color_for_font_name.append(255)
        color_for_font_description.append(255)
        color_for_font_nums.append(255)
        font_color_name = tuple(color_for_font_name)
        font_color_description = tuple(color_for_font_description)
        font_color_nums = tuple(color_for_font_nums)

        # Import artwork and crop
        artwork = Image.open("cropped_images/" + dict["artwork"])
        artwork = artwork.crop(box=(0, 0, self.image_width, self.image_height))
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
        fnt1 = ImageFont.truetype(self.current_font, self.name_font_size)
        fnt2 = ImageFont.truetype(self.current_font, self.description_font_size)
        name_obj = ImageDraw.Draw(name_txt)
        description_obj = ImageDraw.Draw(description_txt)

        name_width = name_obj.textlength(dict["card_name"], font=fnt1)

        # Make Names smaller if necessary
        i = 0
        while name_width >= self.max_description_width:
            i = i - 1
            self.name_y += 1
            fnt1 = ImageFont.truetype(self.current_font, self.name_font_size - i)
            name_width = name_obj.textlength(dict["card_name"], font=fnt1)

        # Wrap Description Text
        lines = []
        current_line = ""
        for word in dict["description"].split(" "):
            test_line = f"{current_line} {word}".strip()
            line_width = description_obj.textlength(test_line, fnt2)
            if len(current_line) > 0:
                if (
                    line_width <= self.max_description_width
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

        name_x = (self.image_width - name_width) / 2
        name_obj.text(
            (name_x, self.name_y), dict["card_name"], font=fnt1, fill=font_color_name
        )
        description_obj.multiline_text(
            (self.description_x, self.description_y),
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


# Create Cards
Creator = CardCreator()
champion_json_paths = ["first_champions", "second_champions", "third_champions"]
spell_json_paths = ["first_spells", "second_spells", "third_spells"]
equipment_json_paths = [
    "first_equipment_air",
    "first_equipment_earth",
    "first_equipment_fire",
    "first_equipment_water",
    "second_equipment_air",
    "second_equipment_earth",
    "second_equipment_fire",
    "second_equipment_water",
    "third_equipment",
]

for path in champion_json_paths:
    with open(f"card_json/{path}.json", "r", encoding="utf-8") as json_file:
        loaded_json = json.load(json_file)
    for card in loaded_json["cards"]:
        Creator.generate_champion_card(card).show()
        Creator.generate_champion_card(card).save(
            "finished_cards/Champions/" + card["card_name"] + "_card.png", "PNG"
        )
for path in spell_json_paths:
    with open(f"card_json/{path}.json", "r", encoding="utf-8") as json_file:
        loaded_json = json.load(json_file)
    for card in loaded_json["cards"]:
        Creator.generate_equipment_or_spell_card(card).show()
        Creator.generate_equipment_or_spell_card(card).save(
            "finished_cards/Spells/" + card["card_name"] + "_card.png", "PNG"
        )
for path in equipment_json_paths:
    with open(f"card_json/{path}.json", "r", encoding="utf-8") as json_file:
        loaded_json = json.load(json_file)
    for card in loaded_json["cards"]:
        Creator.generate_equipment_or_spell_card(card).show()
        Creator.generate_equipment_or_spell_card(card).save(
            f"finished_cards/{card["type"]}/{card["card_name"]}_card.png", "PNG"
        )
