# 1) Using Condition Checking 

n = lambda x: "positive" if x > 0 else "Negative" if x < 0 else "Zero"
print(n(5))
print(n(-4))
print(n(0))

#Lambda  function takes input as x 

# It uses  Nested  if else  statement to return  positive , negative and  Zero 

#2) using with  List Comprehensions 
  
  #  It Will creates the   list of lambda   functions   where  each multiplying its input by 10 amd
  # Executes them one by  one 
  
li = [lambda arg=x: arg * 10 for x in range(1, 5)]
for i in li:
    print(i())
    
  # lambda  function  multiply  each  element  by  10 
  # lsit comprehension  iterates throgh li and applies lambda to  each  element
  # This is  ideal for  applying  transformations to datasets in the data preprocessinng and manipulation   tasks  
  
#3) Using  Returning the Multiple Results 

# Lambda  fucntionscreates  2  almbda  fucntions  and  then  call other  lambda  fucntion as an parameter to  first one 

calc = lambda x, y: (x + y, x * y)
res = calc(3, 4)
print(res)
   #  The lambda function performs both addition and multiplication and returns a tuple with both results.
#This is useful for scenarios where multiple calculations need to be performed and returned together.


#4) using the  filter()
#filter   function takes an function and list as argument and  which  offers  to  filterout the all elements of  sequence  for  which 
#  fucntions returns  true

m= [1,2,3,4,5,6]
even = filter(lambda x: x % 2 ==0, m)
print(list(even))

# 5) Using  with map()  functions
""" lambda  functions takes  function nd  list as arugenmet 
new  reduced  modified   list is  returned  


"""

#  code

#  doubles each  element in list and  returns the  new  lists

list_map = [1, 2, 3, 4]
b = map(lambda x: x * 2, list_map)
print(list(b))

#6) using  With  Reduce()
'''
Python takes in a function and a list as an argument.
 The function is called with a lambda function and an iterable and a new reduced result is returned
 
''' 

#CODDE 

#lambda multiplies two numbers at a time and reduce() applies this across the whole list to calculate the product.

from functools import reduce
an = [1, 2, 3, 4, 5]
b = reduce(lambda x, y: x * y, an)
print(b)

# Diff  Between  def and lambda  fucntions

#using  Lambda  functions
sq = lambda x: x ** 2
print(sq(3))

def def_sq(x):
    return x ** 2
print(def_sq(3))


 