# Anonymous Functions

def cube(x): return x * x * x   # without Lambda
cube_1 = lambda x : x * x * x    # with Lambda

print(cube(7))
print(cube_1(8))

# Return Statements in  Functions -  which used to  end the functions

def sqaure_value(num):
    """This Function Returns the  square 
     values of  enterd  number"""
    return num**2

print(sqaure_value(2))
print(sqaure_value(-4))


# Pass by Reference and Pass by Value

def myFun(x):
    x[0] = 20
lst = [10, 11, 12, 13]

myFun(lst)
print(lst)

def myFun2(x):
    x = 20
    
a = 10
myFun2(a)
print(a)


# Recursive Functions -  functions  Calls  Itself  To Solve the Problem  - used Divide nd conquer Approach

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))

# From  Here the  workk of   function is  ended 





