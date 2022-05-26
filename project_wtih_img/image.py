from PIL import Image, ImageDraw, ImageFont
import random


def get_position(digit, image_size, bounding_box):
    image_width, image_height = image_size
    left, top, right, bottom = bounding_box
    match digit:
        case num if 0 <= num <= 25:
            return (0, -top)
        case num if 25 < num <= 50:
            return (image_width - right, -top)
        case num if 50 < num <= 75:
            return (0, image_height - bottom)
        case _:
            return (image_width - right, image_height - bottom)


with Image.open('cow.png') as background:
    digit = random.randint(0, 101)
    draw = ImageDraw.Draw(background)
    font = ImageFont.truetype("Roboto-Bold.ttf", 100)
    position = get_position(digit, background.size, font.getbbox(str(digit)))
    draw.text(position, str(digit), tuple([random.randint(0, 256) for i in range(3)]), font=font)
    background.save('cow_edit.png')

with Image.open('cow_edit.png') as image:
    image.show()
#hello_world
