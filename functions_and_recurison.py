# functions and recusion
# Damien Cheng
# Dec 7

def factorial(n:int) -> int:
    if n == 0 or n == 1:
        return 1
    elif n>1:
        return factorial(n-1) * n
    
#print(factorial(100))

def fib(x:int)-> int:
    if x in [1, 2]:
        return 1
    elif x > 2:
        return fib(x-1) + fib(x-2)
    
print(fib(9))

