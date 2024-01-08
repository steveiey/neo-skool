# is light maybe
# Damien Cheng
# Dec 18
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



with Image.open("./Images/MR.I.jpg") as im:
    height = im.height
    width = im.width
    for y in range(height):
        for x in range(width):
            pixel = im.getpixel((x, y))
            if is_light(pixel):
                im.putpixel((x, y), (255,255,255))
            else:
                im.putpixel((x, y), (0,0,0))
    im.save("./images/Incredible.pdf")




print(is_light(light_pixel))  # True
print(is_light(light_gray))  # True
print(is_light(dark_gray))  # False
print(is_light(dark_pixel))  # False