from PIL import Image, ImageDraw, ImageFont
from constants import (
    FONT_PATH,
    NAME_Y_OSSFET,
    SPECIAL_Y_OSSFET,
    ATTACK_DEFENCE_Y_OFFSET,
    ATTACK_X_OFFSET,
    DEFENCE_X_OFFSET,
)


def resize_image(img_path, size_cm, dpi=300):
    # Convert size in cm to size in pixels
    size_pixels = (int(size_cm[0] * dpi / 2.54), int(size_cm[1] * dpi / 2.54))
    with Image.open(img_path) as img:
        img_resized = img.resize(size_pixels)
    return img_resized


def create_card(image_path,
                output_path,
                name,
                attack,
                defence,
                special,
                dpi=300):

    template_path = "/Users/pavelrastopchin/Downloads/card_template_v3.png"

    blank_size = (int(9 * dpi / 2.54), int(12 * dpi / 2.54))
    blank_img = Image.new("RGBA", blank_size, "white")

    # Resize images
    template_img = resize_image(template_path, (9, 12))
    image_img = resize_image(image_path, (8.5, 8.5))

    # Paste the image_img centered on the blank image
    x_offset_img = (blank_img.size[0] - image_img.size[0]) // 2
    y_offset_img = int(0.25 * dpi / 2.54)
    blank_img.paste(image_img, (x_offset_img, y_offset_img), image_img)

    # Paste the template_img centered on top of the image_img
    x_offset_template = (blank_img.size[0] - template_img.size[0]) // 2
    y_offset_template = (blank_img.size[1] - template_img.size[1]) // 2
    blank_img.paste(template_img, (x_offset_template, y_offset_template), template_img)

    # Special
    draw = ImageDraw.Draw(blank_img)
    font = ImageFont.truetype(FONT_PATH, 42)
    left, upper, right, lower = draw.textbbox((0, 0), special, font=font)
    text_width = right - left
    text_height = lower - upper
    x_text = (blank_img.size[0] - text_width) // 2
    y_text = blank_img.size[1] - text_height - SPECIAL_Y_OSSFET
    draw.text((x_text, y_text), special, fill="black", font=font)

    # Name
    draw = ImageDraw.Draw(blank_img)
    font = ImageFont.truetype(FONT_PATH, 72)
    left, upper, right, lower = draw.textbbox((0, 0), name, font=font)
    text_width = right - left
    text_height = lower - upper
    x_text = (blank_img.size[0] - text_width) // 2
    y_text = blank_img.size[1] - text_height - NAME_Y_OSSFET
    draw.text((x_text, y_text), name, fill="black", font=font)

    # Attack
    draw = ImageDraw.Draw(blank_img)
    font = ImageFont.truetype(FONT_PATH, 120)
    left, upper, right, lower = draw.textbbox((0, 0), str(attack), font=font)
    text_height = lower - upper
    y_text = blank_img.size[1] - text_height - ATTACK_DEFENCE_Y_OFFSET
    draw.text((ATTACK_X_OFFSET, y_text), str(attack), fill="black", font=font)

    # Defence
    draw = ImageDraw.Draw(blank_img)
    font = ImageFont.truetype(FONT_PATH, 120)
    left, upper, right, lower = draw.textbbox((0, 0), str(defence), font=font)
    text_height = lower - upper
    y_text = blank_img.size[1] - text_height - ATTACK_DEFENCE_Y_OFFSET
    draw.text((DEFENCE_X_OFFSET, y_text), str(defence), fill="black", font=font)

    # Save the combined image
    blank_img.save(output_path)


if __name__ == '__main__':
    image_path = "/Users/pavelrastopchin/Downloads/DALL·E 2023-10-18 23.13.15 - Thin black line illustration with reduced texture designed for coloring. It portrays a battle-worn medieval warrior fully clad in armor, charging with.png"
    output_path = "../temp.png"
    name = "TEST TEST TEST"
    special = "Melee\n\n+2 attack against demons"
    create_card(image_path,
                output_path,
                name,
                attack=1,
                defence=1,
                special=special,
                dpi=300)
