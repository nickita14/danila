from PIL import Image, ImageDraw, ImageFont
import random
#(110, 61, 255)

def get_position(digit, image_size, bounding_box):
    image_width, image_height = image_size
    left, top, right, bottom = bounding_box
    if 0 <= digit < 25:
        return (0, -top)
    elif 25 <= digit < 50:
        return (image_width - right, -top)
    elif 50 <= digit < 75:
        return (0, image_height - bottom)
    else:
        return (image_width - right, image_height - bottom)


with Image.open('cow.png') as background:
    digit = random.randint(0, 100)
    draw = ImageDraw.Draw(background)
    font = ImageFont.truetype("Roboto-Bold.ttf", 100)
    position = get_position(digit, background.size, font.getbbox(str(digit)))
    draw.text(position, str(digit),tuple([random.randint(0,256) for i in range(3)]) , font=font)
    background.save('cow_edit.png')

with Image.open('cow_edit.png') as image:
    image.show()
