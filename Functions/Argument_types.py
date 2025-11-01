# Default  Arguments - assumes  default values if  not  provided in  fucntion call

print("-----------Default  arguement ------------")
def myFun(x, y = 20):
    print("X : ", x)
    print("Y : ", y)
myFun(15)


# Keyword Argument = values passed Explicitly and Order  dosen't matter  
print("-----------Keyword  arguement ------------")

def student(fname, lname):
    print(fname, lname)
student(fname = 'Shubham', lname='Chaudhari')
student(lname = 'Chaudhari', fname='Shubham')

#Positional Arguments

print("-----------Positional  arguement ------------")

def nameAge(name, age):
    print("Hi, My Name IS : ", name)
    print("And , My Age IS : ", age)
    
print("Case - 1: ")
nameAge("Dadu", 22)

print("Case - 2: ")
nameAge(23, "Parya")

#Arbitrary Arguments

print("-----------Arbitrary  arguement ------------")

def myArb(*args, **kwargs):
    print("Non Keyword Based Arguments : (*args)")
    for arg in args:
        print(arg)
        
    print("Keyword Based Arguments : (**kwargs)")
    for key in kwargs.items():
        print(f"{key}== {value}")
        
myArb('INS Vikrant', 'INS Virat', first = 'INS Arihant', mid = 'HMS Herculas', last = 'INS Rajput') 

       