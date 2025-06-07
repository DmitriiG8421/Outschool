#Step-1: function objects

def greet():
    print("Hello")

hello = greet #if you save a function 
#in a variable without using the parentheses it is called a function object. 
# it is an object that holds your function's code

hello()
#This is function object
#It holds the function's code
#So 'hello' holds the code of 'greet'



#Step-2: functions inside functions

def outer():
    def inner():
        print("I am the inner function")

    inner()
outer()



#Step-3: functions returning functions

def outside():
    def inside():
        print("Hello from inner function!")
    return inside
       
my_function = outside()
my_function()


#Step-4: passing functions to other functions 

def greetings(func):
    print("Doing something first...")
    func()


def say_hello():
    print("Hello there!")


greetings(say_hello)