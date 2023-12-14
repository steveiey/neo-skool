# Functions_practice
# Damien Cheng
# Nov 24


def area_of_square(sidelength: float) -> float:
	"""
	Input a number and it will square the number.
	(multiplied by itself)
	
	Params:

	sidelength - length of one side of the square
	"""
	area = sidelength ** 2
	return area
    

#sus = int(input("wat numba"))
#for i in range(sus):
	#print(f"*" + "*"*i)

def stars(stary: int) -> str:
	nite = "*"*stary
	return nite
print(stars(5))

def biggest_of_three(number1, number2, number3: float) -> str:
	biggg = 0
	if number1 > biggg:
			biggg = number1
	if number2 > biggg:
			biggg = number2
	if number3 > biggg:
			biggg = number3
	return biggg
print(biggest_of_three(542,777,1))

def pyramid(layers: int) ->None:
	for i in range(layers+1):
		print(stars(i))





print(pyramid(6))

def pyramid_mirror(layers: int) -> None:
	for i in range(layers+1):
		spaces = " "*(layers-i)
		print( spaces + stars(i))

pyramid_mirror(10)


def linear_search(l:list, item:  any) -> int:
	"""Search through a list and gives location of item.
will return -1 if nothing found"""

	counter = 0

#search
	for thing in l:
		if thing == item:
			return counter
		counter += 1


		
	return -1
pockets = ["sus","amogus", "eat", "consume", "keys"]
results = linear_search(pockets, "keys")
print(f"THEY ARE {results}")