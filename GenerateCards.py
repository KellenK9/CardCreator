from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import json
from math import ceil, floor


class CardCreator:
    def declare_vars(self):
        self.image_width = 825
        self.image_height = 1125
        self.crop_border = 35
        self.pixel_image_width = 177
        self.pixel_image_height = 248
        self.name_y = 1000
        self.name_y_champions = 950
        self.description_x = 58
        self.description_y = 860
        self.description_y_champions = 825
        self.name_font_size = 60
        self.description_font_size = 24
        self.longest_name_for_normal_size = 32
        self.max_description_width = self.image_width - (self.description_x * 2)
        self.description_line_spacing = 6
        self.y_offset_between_effects = 6
        self.stroke_width = 2
        self.corner_radius = 46
        self.slot_y = 1055
        self.slot3_x = self.image_width * 3 / 4 + 25
        self.slot2_x = self.image_width / 2
        self.slot1_x = self.image_width / 4 - 25

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
            "fonts/Lato-Bold.ttf",
        ]
        self.current_name_font = self.fonts[4]
        self.current_description_font = self.fonts[5]

    def wrap_description_text(self, dict, fnt_description, description_obj):
        lines = []
        current_line = ""
        for word in dict["description"].split(" "):
            test_line = f"{current_line} {word}".strip()
            line_width = description_obj.textlength(test_line, fnt_description)
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
        return wrapped_text, lines

    def generate_champion_card(self, dict, printed=False, full_art=False):
        # Set global vars
        CardCreator.declare_vars(self)

        # Set Champion specific Vars
        health_y = 710
        health_font_size = 80
        color_for_font_name = list(self.colors["white"])
        color_for_font_description = list(self.colors["white"])

        # Append font color tuple
        color_for_font_name.append(255)
        color_for_font_description.append(255)
        font_color_name = tuple(color_for_font_name)
        font_color_description = tuple(color_for_font_description)

        # Import artwork and crop
        if full_art:
            artwork = Image.open(
                f"cropped_images/printable_versions/full_arts/{dict["artwork"].split(".")[0]}_extended.png"
            )
        else:
            artwork = Image.open("cropped_images/printable_versions/" + dict["artwork"])
        artwork = artwork.crop(box=(0, 0, self.image_width, self.image_height))
        artwork = artwork.convert("RGBA")

        # Import frame
        if printed:
            folder = "printable"
        else:
            folder = "digital"
        if "earth" in dict["slot1"] or "earth" in dict["slot2"]:
            frame = Image.open(f"card_frames/{folder}/earth-champion-frame.png")
        if "air" in dict["slot1"] or "air" in dict["slot2"]:
            frame = Image.open(f"card_frames/{folder}/air-champion-frame.png")
        if "water" in dict["slot1"] or "water" in dict["slot2"]:
            frame = Image.open(f"card_frames/{folder}/water-champion-frame.png")
        if "fire" in dict["slot1"] or "fire" in dict["slot2"]:
            frame = Image.open(f"card_frames/{folder}/fire-champion-frame.png")

        # Add slots
        if dict["slot3"] != "none" and dict["slot3"] != None:
            third_slot = Image.open(
                f"card_frames/{folder}/equipment_slots/" + dict["slot3"] + "_slot.png"
            )
        else:
            third_slot = Image.open(
                f"card_frames/{folder}/equipment_slots/empty_slot.png"
            )
        if dict["slot2"] != "none" and dict["slot2"] != None:
            second_slot = Image.open(
                f"card_frames/{folder}/equipment_slots/" + dict["slot2"] + "_slot.png"
            )
        else:
            second_slot = Image.open(
                f"card_frames/{folder}/equipment_slots/empty_slot.png"
            )
        if dict["slot1"] != "none" and dict["slot1"] != None:
            first_slot = Image.open(
                f"card_frames/{folder}/equipment_slots/" + dict["slot1"] + "_slot.png"
            )
        else:
            first_slot = Image.open(
                f"card_frames/{folder}/equipment_slots/empty_slot.png"
            )

        # Add Text
        name_txt = Image.new("RGBA", frame.size, (255, 255, 255, 0))
        health_txt = Image.new("RGBA", frame.size, (255, 255, 255, 0))
        description_txt = Image.new("RGBA", frame.size, (255, 255, 255, 0))
        fnt_name = ImageFont.truetype(self.current_name_font, self.name_font_size)
        fnt_health = ImageFont.truetype(self.current_name_font, health_font_size)
        fnt_description = ImageFont.truetype(
            self.current_description_font, self.description_font_size
        )
        name_obj = ImageDraw.Draw(name_txt)
        health_obj = ImageDraw.Draw(health_txt)
        description_obj = ImageDraw.Draw(description_txt)

        name_width = name_obj.textlength(dict["card_name"], font=fnt_name)
        health_width = health_obj.textlength(dict["health"], font=fnt_health)

        # Make Names smaller if necessary
        i = 0
        while name_width >= self.max_description_width:
            i += 1
            self.name_y_champions += 1
            fnt_name = ImageFont.truetype(
                self.current_name_font, self.name_font_size - i
            )
            name_width = name_obj.textlength(dict["card_name"], font=fnt_name)

        # Wrap Description Text
        wrapped_text, lines = CardCreator.wrap_description_text(
            self, dict, fnt_description, description_obj
        )

        # TODO: Add logic that shrinks description text if the text is too long to fit in the box.

        # Create text objects
        name_x = (self.image_width - name_width) / 2
        health_x = (self.image_width - health_width) / 2
        name_obj.text(
            (name_x, self.name_y_champions),
            dict["card_name"],
            font=fnt_name,
            fill=font_color_name,
            stroke_width=self.stroke_width,
            stroke_fill=(0, 0, 0),
        )
        health_obj.text(
            (health_x, health_y),
            dict["health"],
            font=fnt_health,
            fill=font_color_name,
            stroke_width=self.stroke_width,
            stroke_fill=(0, 0, 0),
        )
        # Create description text object with custom spacing
        self.description_y_champions -= self.y_offset_between_effects
        for line in lines:
            # Add line to description text object
            if line[0] == "[":
                self.description_y_champions += self.y_offset_between_effects
            description_obj.text(
                (self.description_x, self.description_y_champions),
                line,
                font=fnt_description,
                fill=font_color_description,
                stroke_width=self.stroke_width,
                stroke_fill=(0, 0, 0),
            )
            # Measure the text height using textbbox
            bbox = description_obj.textbbox((0, 0), line, font=fnt_description)
            line_height = bbox[3] - bbox[1]  # Height is bottom - top
            # Move y down for next line
            self.description_y_champions += line_height + self.description_line_spacing
            if line[-1] == ".":
                self.description_y_champions += self.y_offset_between_effects

        # Combine images
        if full_art:
            new_image = artwork
        else:
            new_image = Image.alpha_composite(artwork, frame)
        slot_width, slot_height = first_slot.size
        new_image.paste(
            first_slot,
            (
                floor(self.slot1_x - (slot_width / 2)),
                floor(self.slot_y - (slot_height / 2)),
                floor(self.slot1_x + (slot_width / 2)),
                floor(self.slot_y + (slot_height / 2)),
            ),
            first_slot,
        )
        new_image.paste(
            second_slot,
            (
                floor(self.slot2_x - (slot_width / 2)),
                floor(self.slot_y - (slot_height / 2)),
                floor(self.slot2_x + (slot_width / 2)),
                floor(self.slot_y + (slot_height / 2)),
            ),
            second_slot,
        )
        new_image.paste(
            third_slot,
            (
                floor(self.slot3_x - (slot_width / 2)),
                floor(self.slot_y - (slot_height / 2)),
                floor(self.slot3_x + (slot_width / 2)),
                floor(self.slot_y + (slot_height / 2)),
            ),
            third_slot,
        )
        new_image = Image.alpha_composite(new_image, name_txt)
        new_image = Image.alpha_composite(new_image, health_txt)
        new_image = Image.alpha_composite(new_image, description_txt)

        if printed:
            return new_image
        else:
            # Crop image
            new_image = new_image.crop(
                (
                    self.crop_border,
                    self.crop_border,
                    self.image_width - self.crop_border,
                    self.image_height - self.crop_border,
                )
            )

            # Round Corners
            # Create a mask with rounded corners
            mask = Image.new("L", new_image.size, 0)
            draw = ImageDraw.Draw(mask)
            width, height = new_image.size
            draw.rounded_rectangle(
                [(0, 0), (width, height)], radius=self.corner_radius, fill=255
            )

            # Apply the mask to the original image
            rounded_image = Image.new("RGBA", new_image.size, (0, 0, 0, 0))
            rounded_image.paste(new_image, (0, 0), mask=mask)

            return rounded_image

    def generate_equipment_or_spell_card(self, dict, printed=False):
        # Set global vars
        CardCreator.declare_vars(self)

        color_for_font_name = list(self.colors["white"])
        color_for_font_description = list(self.colors["white"])

        # Append font color tuple
        color_for_font_name.append(255)
        color_for_font_description.append(255)
        font_color_name = tuple(color_for_font_name)
        font_color_description = tuple(color_for_font_description)

        # Import artwork and crop
        artwork = Image.open("cropped_images/printable_versions/" + dict["artwork"])
        artwork = artwork.crop(box=(0, 0, self.image_width, self.image_height))
        artwork = artwork.convert("RGBA")

        # Import and color frame
        if printed:
            folder = "printable"
        else:
            folder = "digital"
        if dict["type"] == "water":
            frame = Image.open(f"card_frames/{folder}/water-frame.png")
        if dict["type"] == "fire":
            frame = Image.open(f"card_frames/{folder}/fire-frame.png")
        if dict["type"] == "earth":
            frame = Image.open(f"card_frames/{folder}/earth-frame.png")
        if dict["type"] == "air":
            frame = Image.open(f"card_frames/{folder}/air-frame.png")
        if dict["type"] == "spell":
            frame = Image.open(f"card_frames/{folder}/spell-frame.png")

        # Add text
        name_txt = Image.new("RGBA", frame.size, (255, 255, 255, 0))
        description_txt = Image.new("RGBA", frame.size, (255, 255, 255, 0))
        fnt_name = ImageFont.truetype(self.current_name_font, self.name_font_size)
        fnt_description = ImageFont.truetype(
            self.current_description_font, self.description_font_size
        )
        name_obj = ImageDraw.Draw(name_txt)
        description_obj = ImageDraw.Draw(description_txt)

        name_width = name_obj.textlength(dict["card_name"], font=fnt_name)

        # Make Names smaller if necessary
        i = 0
        while name_width >= self.max_description_width:
            i = i + 1
            # self.name_y += 1
            fnt_name = ImageFont.truetype(
                self.current_name_font, self.name_font_size - i
            )
            name_width = name_obj.textlength(dict["card_name"], font=fnt_name)

        # Wrap Description Text
        wrapped_text, lines = CardCreator.wrap_description_text(
            self, dict, fnt_description, description_obj
        )

        # Create text objects
        name_x = (self.image_width - name_width) / 2
        name_obj.text(
            (name_x, self.name_y),
            dict["card_name"],
            font=fnt_name,
            fill=font_color_name,
            stroke_width=self.stroke_width,
            stroke_fill=(0, 0, 0),
        )
        # Create description text object with custom spacing
        self.description_y -= self.y_offset_between_effects
        for line in lines:
            if line[0] == "[":
                self.description_y += self.y_offset_between_effects
            # Add line to description text object
            description_obj.text(
                (self.description_x, self.description_y),
                line,
                font=fnt_description,
                fill=font_color_description,
                stroke_width=self.stroke_width,
                stroke_fill=(0, 0, 0),
            )
            # Measure the text height using textbbox
            bbox = description_obj.textbbox((0, 0), line, font=fnt_description)
            line_height = bbox[3] - bbox[1]  # Height is bottom - top
            # Move y down for next line
            self.description_y += line_height + self.description_line_spacing

        # Combine images
        new_image = Image.alpha_composite(artwork, frame)
        new_image = Image.alpha_composite(new_image, name_txt)
        new_image = Image.alpha_composite(new_image, description_txt)

        if printed:
            return new_image
        else:
            # Crop image
            new_image = new_image.crop(
                (
                    self.crop_border,
                    self.crop_border,
                    self.image_width - self.crop_border,
                    self.image_height - self.crop_border,
                )
            )

            # Round Corners
            # Create a mask with rounded corners
            mask = Image.new("L", new_image.size, 0)
            draw = ImageDraw.Draw(mask)
            width, height = new_image.size
            draw.rounded_rectangle(
                [(0, 0), (width, height)], radius=self.corner_radius, fill=255
            )

            # Apply the mask to the original image
            rounded_image = Image.new("RGBA", new_image.size, (0, 0, 0, 0))
            rounded_image.paste(new_image, (0, 0), mask=mask)

            return rounded_image

    def create_pixel_images(self, card_name, artwork_path):
        size = 177, 177
        im = Image.open("cropped_images/" + artwork_path)
        im.thumbnail(size, Image.Resampling.LANCZOS)
        im.save(
            "cropped_images/pixel_art_versions/" + card_name + "_card.png",
            "PNG",
        )

    def create_print_sized_images(self, card_name, artwork_path, full_art=False):
        size = 825, 825
        im = Image.open("cropped_images/" + artwork_path)
        if full_art:
            new_width = 825
            left = 0
            top = 0
            right = 825
            bottom = 1125
            # Scale
            new_height = int(im.height * (new_width / im.width))
            im = im.resize((new_width, new_height))
            # Crop
            im = im.crop((left, top, right, bottom))
        else:
            im = Image.open("cropped_images/" + artwork_path)
            im.thumbnail(size, Image.Resampling.LANCZOS)
        im.save(
            "cropped_images/printable_versions/" + artwork_path,
            "PNG",
        )

    def create_zoomed_cards(self, card_name, card_path):
        size = 771, 1080
        im = Image.open(card_path)
        im.thumbnail(size, Image.Resampling.LANCZOS)
        im.save(
            "finished_cards/zoomed_versions/" + card_name + "_card.png",
            "PNG",
        )

    def create_pixel_frames(self, artwork_path):
        size = 177, 248
        im = Image.open("card_frames/digital/" + artwork_path)
        im.thumbnail(size, Image.Resampling.LANCZOS)
        im.save(
            "card_frames/pixel_art_frames/" + artwork_path,
            "PNG",
        )

    def generate_champion_pixel_art_card(self, dict):
        # Set global vars
        CardCreator.declare_vars(self)

        # Import frame
        frame = Image.open("card_frames/pixel_art_frames/champion-frame.png")

        # Import artwork and crop
        artwork = Image.open(
            "cropped_images/pixel_art_versions/" + dict["card_name"] + "_card.png"
        )
        artwork = artwork.crop(
            box=(0, 0, self.pixel_image_width, self.pixel_image_height)
        )
        artwork = artwork.convert("RGBA")

        # Add slots
        if dict["slot3"] != "none" and dict["slot3"] != None:
            third_slot = Image.open(
                "card_frames/pixel_art_frames/" + dict["slot3"] + "-right.png"
            )
        if dict["slot2"] != "none" and dict["slot2"] != None:
            second_slot = Image.open(
                "card_frames/pixel_art_frames/" + dict["slot2"] + "-middle.png"
            )
        if dict["slot1"] != "none" and dict["slot1"] != None:
            first_slot = Image.open(
                "card_frames/pixel_art_frames/" + dict["slot1"] + "-left.png"
            )

        # Combine images
        new_image = Image.alpha_composite(artwork, frame)
        if dict["slot1"] != "none" and dict["slot1"] != None:
            new_image = Image.alpha_composite(new_image, first_slot)
        if dict["slot2"] != "none" and dict["slot2"] != None:
            new_image = Image.alpha_composite(new_image, second_slot)
        if dict["slot3"] != "none" and dict["slot3"] != None:
            new_image = Image.alpha_composite(new_image, third_slot)
        return new_image

    def generate_equipment_or_spell_pixel_art_card(self, dict):
        # Set global vars
        CardCreator.declare_vars(self)

        # Import and color frame
        if dict["type"] == "water":
            frame = Image.open("card_frames/pixel_art_frames/water-frame.png")
        if dict["type"] == "fire":
            frame = Image.open("card_frames/pixel_art_frames/fire-frame.png")
        if dict["type"] == "earth":
            frame = Image.open("card_frames/pixel_art_frames/earth-frame.png")
        if dict["type"] == "air":
            frame = Image.open("card_frames/pixel_art_frames/air-frame.png")
        if dict["type"] == "spell":
            frame = Image.open("card_frames/pixel_art_frames/spell-frame.png")

        # Import artwork and crop
        artwork = Image.open(
            "cropped_images/pixel_art_versions/" + dict["card_name"] + "_card.png"
        )
        artwork = artwork.crop(
            box=(0, 0, self.pixel_image_width, self.pixel_image_height)
        )
        artwork = artwork.convert("RGBA")

        # Combine images
        new_image = Image.alpha_composite(artwork, frame)
        return new_image


# Set Variables for Creating Cards
Creator = CardCreator()
champion_json_paths = ["first_champions", "second_champions", "third_champions"]
spell_json_paths = ["first_spells", "second_spells", "third_spells", "fourth_spells"]
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
    "fourth_equipment",
    # "future_spells",
    # "future_equipment",
]
list_of_frames = [
    "card-back",
    "air-frame",
    "water-frame",
    "earth-frame",
    "fire-frame",
    "spell-frame",
    "air-champion-frame",
    "water-champion-frame",
    "fire-champion-frame",
    "earth-champion-frame",
    "equipment_slots/air_slot",
    "equipment_slots/fire_slot",
    "equipment_slots/water_slot",
    "equipment_slots/earth_slot",
]
full_arts = ["fire_golem", "earth_golem", "volcanic_slug"]
# Create printable versions of art
"""
for path in champion_json_paths:
    with open(f"card_json/{path}.json", "r", encoding="utf-8") as json_file:
        loaded_json = json.load(json_file)
    for card in loaded_json["cards"]:
        Creator.create_print_sized_images(card["card_name"], card["artwork"])
for path in spell_json_paths:
    with open(f"card_json/{path}.json", "r", encoding="utf-8") as json_file:
        loaded_json = json.load(json_file)
    for card in loaded_json["cards"]:
        Creator.create_print_sized_images(card["card_name"], card["artwork"])
for path in equipment_json_paths:
    with open(f"card_json/{path}.json", "r", encoding="utf-8") as json_file:
        loaded_json = json.load(json_file)
    for card in loaded_json["cards"]:
        Creator.create_print_sized_images(card["card_name"], card["artwork"])
"""
# Create printable versions of Champion full arts artwork

for path in champion_json_paths:
    with open(f"card_json/{path}.json", "r", encoding="utf-8") as json_file:
        loaded_json = json.load(json_file)
    for card in loaded_json["cards"]:
        for full_art_path in full_arts:
            if full_art_path in card["artwork"]:
                Creator.create_print_sized_images(
                    card["card_name"], f"full_arts/{full_art_path}_extended.png", True
                )

# Create Digital Cards
"""
for path in champion_json_paths:
    with open(f"card_json/{path}.json", "r", encoding="utf-8") as json_file:
        loaded_json = json.load(json_file)
    for card in loaded_json["cards"]:
        # Creator.generate_champion_card(card).show()
        Creator.generate_champion_card(card).save(
            "finished_cards/Champions/" + card["card_name"] + "_card.png", "PNG"
        )
for path in spell_json_paths:
    with open(f"card_json/{path}.json", "r", encoding="utf-8") as json_file:
        loaded_json = json.load(json_file)
    for card in loaded_json["cards"]:
        # Creator.generate_equipment_or_spell_card(card).show()
        Creator.generate_equipment_or_spell_card(card).save(
            "finished_cards/Spells/" + card["card_name"] + "_card.png", "PNG"
        )
for path in equipment_json_paths:
    with open(f"card_json/{path}.json", "r", encoding="utf-8") as json_file:
        loaded_json = json.load(json_file)
    for card in loaded_json["cards"]:
        # Creator.generate_equipment_or_spell_card(card).show()
        Creator.generate_equipment_or_spell_card(card).save(
            f"finished_cards/{card["type"]}/{card["card_name"]}_card.png", "PNG"
        )
"""
# Create Printable Cards
"""
for path in champion_json_paths:
    with open(f"card_json/{path}.json", "r", encoding="utf-8") as json_file:
        loaded_json = json.load(json_file)
    for card in loaded_json["cards"]:
        # Creator.generate_champion_card(card, True).show()
        Creator.generate_champion_card(card, True).save(
            "finished_cards/printable/Champions/" + card["card_name"] + "_card.png",
            "PNG",
        )
for path in spell_json_paths:
    with open(f"card_json/{path}.json", "r", encoding="utf-8") as json_file:
        loaded_json = json.load(json_file)
    for card in loaded_json["cards"]:
        # Creator.generate_equipment_or_spell_card(card, True).show()
        Creator.generate_equipment_or_spell_card(card, True).save(
            "finished_cards/printable/Spells/" + card["card_name"] + "_card.png", "PNG"
        )
for path in equipment_json_paths:
    with open(f"card_json/{path}.json", "r", encoding="utf-8") as json_file:
        loaded_json = json.load(json_file)
    for card in loaded_json["cards"]:
        # Creator.generate_equipment_or_spell_card(card, True).show()
        Creator.generate_equipment_or_spell_card(card, True).save(
            f"finished_cards/printable/{card["type"]}/{card["card_name"]}_card.png",
            "PNG",
        )
"""
# Create Digital Full art Champions

for path in champion_json_paths:
    with open(f"card_json/{path}.json", "r", encoding="utf-8") as json_file:
        loaded_json = json.load(json_file)
    for card in loaded_json["cards"]:
        for full_art_path in full_arts:
            if full_art_path in card["artwork"]:
                Creator.generate_champion_card(card, False, True).save(
                    f"finished_cards/full_art/{card["card_name"]}_card.png",
                    "PNG",
                )

# Create Printable Full art Champions

for path in champion_json_paths:
    with open(f"card_json/{path}.json", "r", encoding="utf-8") as json_file:
        loaded_json = json.load(json_file)
    for card in loaded_json["cards"]:
        for full_art_path in full_arts:
            if full_art_path in card["artwork"]:
                Creator.generate_champion_card(card, True, True).save(
                    f"finished_cards/printable/full_art/{card["card_name"]}_card.png",
                    "PNG",
                )

# Create pixel art versions of artwork
"""
for path in champion_json_paths:
    with open(f"card_json/{path}.json", "r", encoding="utf-8") as json_file:
        loaded_json = json.load(json_file)
    for card in loaded_json["cards"]:
        Creator.create_pixel_images(card["card_name"], card["artwork"])
for path in spell_json_paths:
    with open(f"card_json/{path}.json", "r", encoding="utf-8") as json_file:
        loaded_json = json.load(json_file)
    for card in loaded_json["cards"]:
        Creator.create_pixel_images(card["card_name"], card["artwork"])
for path in equipment_json_paths:
    with open(f"card_json/{path}.json", "r", encoding="utf-8") as json_file:
        loaded_json = json.load(json_file)
    for card in loaded_json["cards"]:
        Creator.create_pixel_images(card["card_name"], card["artwork"])
"""
# Create smaller versions of frames
"""
for artwork_path in list_of_frames:
    Creator.create_pixel_frames(f"{artwork_path}.png")
"""
# Create pixel art versions of cards
"""
for path in champion_json_paths:
    with open(f"card_json/{path}.json", "r", encoding="utf-8") as json_file:
        loaded_json = json.load(json_file)
    for card in loaded_json["cards"]:
        Creator.generate_champion_pixel_art_card(card).save(
            "finished_cards/pixel_art_cards/Champions/"
            + card["card_name"]
            + "_card.png",
            "PNG",
        )
for path in spell_json_paths:
    with open(f"card_json/{path}.json", "r", encoding="utf-8") as json_file:
        loaded_json = json.load(json_file)
    for card in loaded_json["cards"]:
        Creator.generate_equipment_or_spell_pixel_art_card(card).save(
            "finished_cards/pixel_art_cards/Spells/" + card["card_name"] + "_card.png",
            "PNG",
        )
for path in equipment_json_paths:
    with open(f"card_json/{path}.json", "r", encoding="utf-8") as json_file:
        loaded_json = json.load(json_file)
    for card in loaded_json["cards"]:
        Creator.generate_equipment_or_spell_pixel_art_card(card).save(
            f"finished_cards/pixel_art_cards/{card["type"]}/{card["card_name"]}_card.png",
            "PNG",
        )
"""
# Create zoomed versions of cards
"""
for path in champion_json_paths:
    with open(f"card_json/{path}.json", "r", encoding="utf-8") as json_file:
        loaded_json = json.load(json_file)
    for card in loaded_json["cards"]:
        Creator.create_zoomed_cards(
            card["card_name"],
            "finished_cards/Champions/" + card["card_name"] + "_card.png",
        )
for path in spell_json_paths:
    with open(f"card_json/{path}.json", "r", encoding="utf-8") as json_file:
        loaded_json = json.load(json_file)
    for card in loaded_json["cards"]:
        Creator.create_zoomed_cards(
            card["card_name"],
            "finished_cards/Spells/" + card["card_name"] + "_card.png",
        )
for path in equipment_json_paths:
    with open(f"card_json/{path}.json", "r", encoding="utf-8") as json_file:
        loaded_json = json.load(json_file)
    for card in loaded_json["cards"]:
        Creator.create_zoomed_cards(
            card["card_name"],
            f"finished_cards/{card["type"]}/{card["card_name"]}_card.png",
        )
"""
