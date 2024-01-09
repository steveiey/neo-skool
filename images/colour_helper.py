#COLOUR HELP
#JAn something
# Damien
from PIL import Image
redpix = []
totpix = 0
totred = len(redpix)



def pixel_to_name(pixel: tuple)->str:
    red, green, blue = pixel
    if red < 140 and blue < 140 and green > 100:
        return "green"
    elif red > 150 and blue < 60 and green < 60:
        return "red"
    elif red < 80 and blue < 150 and green < 90:
        return "navy"
    elif red < 200 and blue > 30 and green < 130:
        return "yellow"
    else:
        return "idk"
    
with Image.open("./images/AH.jpg") as im:
    height = im.height
    width = im.width

    for y in range(height):
        for x in range(width):
            pixel = im.getpixel((x, y))
            print(pixel_to_name(pixel))
            if pixel_to_name(pixel) == "red":
                redpix.append((x,y))
    totpix = height * width
print(len(redpix))
print(totpix)

print(f"{totred/totpix*100}%")