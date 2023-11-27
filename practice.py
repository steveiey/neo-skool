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

def biggest_of_three(number1, number2, number3: int) -> str:
	biggg = 0
	if number1 > biggg:
			biggg = number1
	if number2 > biggg:
			biggg = number2
	if number3 > biggg:
			biggg = number3
	return biggg
print(biggest_of_three(1, 2, 3))

def pyramid(layers: int) -> str:
	for i in range(layers):
		ok = "*" + "*"*i
		
	
		
		
		return ok
	
print(pyramid(6))