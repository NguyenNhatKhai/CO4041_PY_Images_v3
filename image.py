#

from constant import *
from PIL import Image

def convert_to_text(image_path):
    with Image.open(f"{image_path}.png") as image_file:
        image_file = image_file.convert('RGB')
    with open(f"{image_path}.txt", 'w') as text_file:
        for i in range(IMAGE_HEIGHT):
            for j in range(IMAGE_WIDTH):
                red, green, blue = image_file.getpixel((j, i))
                text_file.write(f"{format(red, '08b')}{format(green, '08b')}{format(blue, '08b')}")

def convert_to_image(image_path):
    image_file = Image.new('RGB', (IMAGE_WIDTH, IMAGE_HEIGHT))
    pixels = []
    with open(f"{image_path}.txt", 'r') as text_file:
        content = text_file.read()
        for i in range(0, len(content), 24):
            red = int(content[i : i + 8], 2)
            green = int(content[i + 8 : i + 16], 2)
            blue = int(content[i + 16 : i + 24], 2)
            pixels.append((red, green, blue))
    image_file.putdata(pixels)
    image_file.save(f"{image_path}.png")

def reformat_decoder(decoder_path, image_path):
    with open(f"{decoder_path}.txt", 'r') as source_file:
        source_content = source_file.read(IMAGE_BITS)
    with open(f"{image_path}.txt", 'w') as destination_file:
        destination_file.write(source_content)