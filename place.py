WIDTH_OF_PIXEL = 100 # how many real pixels represent a pixel-art pixel in the input image
HEIGHT_OF_PIXEL = 100 # this should be ~100 so that the text fits inside the pixels
TOP_LEFT_X = 0 # whats the coordinate of the top left pixel
TOP_LEFT_Y = 0
OFFSET_LEFT = 0
OFFSET_TOP = 0
IGNORE_COLORS = [] # ignore pixels with these colors (useful for background)

from PIL import Image
from PIL import ImageFont, ImageDraw
im = Image.open("pxArt.png") # input image
width, height = im.size

draw = ImageDraw.Draw(im)
font = ImageFont.truetype("DejaVuSans.ttf", 24) # download + place a font next to the script, put the name in here

num = 0

for i in range(OFFSET_LEFT, width, WIDTH_OF_PIXEL):
    for j in range(OFFSET_TOP, height, HEIGHT_OF_PIXEL):
        pixelColor = im.getpixel((i + WIDTH_OF_PIXEL//2, j + HEIGHT_OF_PIXEL//2))
        if pixelColor not in IGNORE_COLORS:
            num += 1
            draw.line(((i, j), (i + WIDTH_OF_PIXEL, j)), fill="black", width=1)
            draw.line(((i, j), (i, j + HEIGHT_OF_PIXEL)), fill="black", width=1)
            draw.text((i+3, j+3), f"Nr. {num}\nx{TOP_LEFT_X + (i//WIDTH_OF_PIXEL)}\ny{(TOP_LEFT_Y + j//HEIGHT_OF_PIXEL)}", font=font, fill=(0, 0, 0)) # fill=(0,0,0) is the color of the text

im.save("output.png")