# class 
# object 
# function 
# function object 
# parameter 
# argument
# return 

def recipe():
    print("This is my recipe!")

recipe() #it will just execute the function right away!

my_recipe = recipe #function object it means you are passing the function but not the execute the function

# you cannot print a function object!

my_recipe() # now it will execute the recipe() function so basically recipe() function becomes my_recipe() function 

def outer():
    def inner():
        print("This is the inner function")

    inner() 

outer()



def outside():
    def inside():
        print("This is the inside function")
    return inside #you are returning the function object inside



#outside() = inside

my_function = outside()

#my_function() = inside()

my_function()


def greet(func):
    print("Doing something now...")
    func() #the parameter func is a function object!


def hello():
    print("Hi there!")


greet(hello)


def my_first_decorator(func):
    def wrapper():
        print("This line works first...")
        func()
        print("This is the last line...")
    return wrapper


# def my_regular_function():
#     print("I am in the middle...")


# my_wrapper = my_first_decorator(my_regular_function) #it just returns wrapper!

# my_wrapper()

@my_first_decorator
def my_regular_function():
    print("I am in the middle")
my_regular_function()