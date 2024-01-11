#COLOUR HELP
#JAn something
# Damien
from PIL import Image
redpix = []
yellow = []
navy = []
green = []
totpix = 0
totred = len(redpix)



def pixel_to_name(pixel: tuple)->str:
    red, green, blue = pixel
    if red < 70 and blue < 70 and green > 60 :
        return "green"
    elif 150 < red < 190 and blue < 60 and green < 60:
        return "red"
    elif red < 160 and blue < 230 and green < 90:
        return "navy"
    elif red < 240 and blue < 30 and 150 < green < 200 :
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
            elif pixel_to_name(pixel) == "green":
                green.append((x,y))
            elif pixel_to_name(pixel) == "yellow":
                green.append((x,y))
            else:
                im.putpixel((x, y), (0,0,0))
    im.save("./images/greenandredandyellow.jpg")
    
    
    
    totpix = height * width
totred = len(redpix)
totgrn = len(green)


print(f"red:{totred/totpix*100}%")
print(f"green:{totgrn/totpix*100}%")