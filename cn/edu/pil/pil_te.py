# -*- coding:utf-8 -*- 
#Author: Henry

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

def ran_char():
    return chr(random.randint(65, 90))

def ran_back_color():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

def ran_font_color():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
font = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 36)
draw = ImageDraw.Draw(image)
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=ran_back_color())
for t in range(4):
    draw.text((60 * t + 10, 10), ran_char(), font=font, fill=ran_font_color())

image = image.filter(ImageFilter.BLUR)
image.save('test.jpg', 'jpeg')