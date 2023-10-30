#bubb tea pop algo
# Damien Cheng
# Oct 27

#ask 5 users what their fave tea place is
#opps coco chatime suntea xing fu tang bubble queen

# if say one of these opps, increase counter for opp by one

coconum = 0
chatimenum = 0
sunteanum = 0
xingfunum = 0
bubbleqnum = 0
no_resp = 0
NUM_RESP = 5

list = [coconum, chatimenum, sunteanum, xingfunum, bubbleqnum]

for _ in range (NUM_RESP):
    shp = input("GIMMIE").strip(".,?! ").lower()

    if shp == "coco":
        coconum = coconum + 1
    elif shp == "chatime":
        chatimenum = chatimenum + 1
    elif shp == "suntea":
      sunteanum = sunteanum + 1
    elif shp == "xingfutang":
        xingfunum = xingfunum + 1
    elif shp == "bubblequeen":
        bubbleqnum = bubbleqnum + 1
    else:
        print("I guess you don't like bubbbbbbbbbbbbbbbb")
        no_resp = no_resp + 1

print(f"coco:{coconum}")
print(f"Chatime:{chatimenum}")
print(f"suntea:{sunteanum}")
print(f"xing fu tang:{xingfunum}")
print(f"bubble queen:{bubbleqnum}")


print(f"{coconum/NUM_RESP*100}%")
print(f"{chatimenum/NUM_RESP*100}%")
print(f"{sunteanum/NUM_RESP*100}%")
print(f"{xingfunum/NUM_RESP*100}%")
print(f"{bubbleqnum/NUM_RESP*100}%")
