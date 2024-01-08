#light maybe dark
# Damien Cheng
# some day
from PIL import Image

light_pixel = (255, 255, 255)
light_gray = (128, 128, 128)
dark_gray = (127, 127, 127)
dark_pixel = (0, 0, 0)

def is_light(pixel: tuple) -> bool:

    tot_points = pixel[0] + pixel[1] + pixel[2]
    if tot_points > 765/2:
        return True
    elif tot_points < 765/2:
        return False
    
with Image.open("./Images/SUS.webp") as im:
    height = im.height
    width = im.width
    for y in range(height):
        for x in range(width):
            pixel = im.getpixel((x, y))
            avg = pixel[0] + pixel[1] + pixel[2] // 3
            im.putpixel((x, y), (avg,avg,avg))
    im.save("./images/amongthem.jpg")