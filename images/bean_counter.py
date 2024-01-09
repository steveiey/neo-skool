#bean counter
#Jan somethun
# Dam Ien

from PIL import Image

def pixel_to_name(pixel: tuple)->str:
    red, green, blue = pixel
    if red > 150 and blue < 60 and green < 60:
        return "red"
    
with Image.open("./Image/Jelly Beans.jpg") as im:
    height = im.height
    width = im.width

    for y in range(height):
        for x in range(width):
            pixel = im.getpixel((x, y))
            print(pixel_to_name(pixel))