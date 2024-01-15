# mid ball
# Jan 12
# Damien Cheng

from PIL import Image

redpix = []
currentlongest = 0
longest = 0
longpix = []
longestxycords = []
yval = []

def pixel_to_name(pixel: tuple)->str:
    red, green, blue = pixel
    if red > 130 and blue < 110 and green < 110:
        return "red"
    
with Image.open("./images/ball.jpeg") as im:
    height = im.height
    width = im.width
#see which pixels are red
#save the (x,y) and (y) value of the 
    for y in range(height):
        for x in range(width):
            pixel = im.getpixel((x, y))
            print(pixel_to_name(pixel))
            if pixel_to_name(pixel) == "red":
                redpix.append((x,y))
                longpix.append(y)
                im.putpixel((x, y), (255,255,255))
im.save("./images/ballcheck.jpg")



for pix in longpix:
    for i in longpix:
        if longpix[i] == longpix[i+1]:
            currentlongest += 1
            longestxycords.append((x,y))
        else:
            if currentlongest > longest:
                longest = currentlongest
                currentlongest = longest
            else:
                currentlongest = 0
                longpix.clear()
                longestxycords.clear()
totalyvalue = 0
for cord in longestxycords:
    totalyvalue += cord
print(totalyvalue)
#print(currentlongest)

midpointy = totalyvalue/currentlongest
midpointx = x in longestxycords
#use x value to find row of midpoint
#use average of y values to find y value of midpoint
