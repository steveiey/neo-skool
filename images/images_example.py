# Images in pypy
# Damien Cheng
# Dec 11

from PIL import Image

def pixel_to_name(pixel: tuple)->str:
    red, green, blue = pixel
    if red < 70 and blue < 70 and green > 180:
        return "green"
    else:
        return "idk"




#open sesame
#with Image.open("./Images/kid-green.jpg") as im:
    #grab pixel info
#    pixel = im.getpixel((225,255))
#print(pixel)

#middle_cord = im.width // 2
#print(middle_cord)


with Image.open("./Images/kid-green.jpg") as im:
    height = im.height
    width = im.width
    bgim = Image.open("./images/beach.jpg")

    for y in range(height):
        for x in range(width):
            pixel = im.getpixel((x, y))
            print(pixel_to_name(pixel))
            if pixel_to_name(pixel) == "green":
                bg_pixel = bgim.getpixel((x, y))
                im.putpixel((x, y), bg_pixel)
    
    
    bgim.close()
    im.save("./images/output.jpg")

