# Default Arguments
#We can add default arguments in a function to have default values for parameters that are unspecified in a function call.

def cylinder_volume(height, radius=5):
    pi = 3.14159
    return height * pi * radius ** 2
#In the example above, radius is set to 5 if that parameter is omitted in a function call. 
# If we call cylinder_volume(10), the function will use 10 as the height and 5 as the radius. 
# However, if we call cylinder_volume(10, 7) the 7 will simply overwrite the default value of 5.

#Also notice here we are passing values to our arguments by position. It is possible to pass values 
# in two ways - by position and by name. Each of these function calls are evaluated the same way.

cylinder_volume(10, 7)  # pass in arguments by position
cylinder_volume(height=10, radius=7)  # pass in arguments by name


# VARIABLE SCOPE
#Variable scope refers to which parts of a program a variable can be referenced, or used, from.

#It's important to consider scope when using variables in functions. If a variable is created in#side 
# a function, it can only be used within that function. Accessing it outside that function is not possible.

# This will result in an error
def some_function():
    word = "hello"

print(word)
# In the example above and the example below, word is said to have scope that is only local to each function. This means you can use the same name for different variables that are used in different functions.

# This works fine
def some_function():
    word = "hello"

def another_function():
    word = "goodbye"

# Variables defined outside functions, as in the example below, can still be accessed within a function. Here, word is said to have a global scope.

# This works fine
word = "hello"

def some_function():
    print(word)

some_function()

# Good practice: It is best to define variables in the smallest scope they will be needed in. 
# While functions can refer to variables defined in a larger scope, this is very rarely a good idea 
# since you may not know what variables you have defined if your program has a lot of variables.

## Exemple

def readable_timedelta(days):
    # use integer division to get the number of weeks
    weeks = days // 7
    # use % to get the number of days that remain
    remainder = days % 7
    return "{} week(s) and {} day(s).".format(weeks, remainder)

# test your function
print(readable_timedelta(10))


## --- Test 1 # This code causes an UnboundLocalError
egg_count = 0

def buy_eggs():
    egg_count += 12 # purchase a dozen eggs

buy_eggs()
#Because the variable egg_count in the first line has global scope. 
# Note that it is not passed as an argument into the function, so the function assumes the 
# egg_count being referred to is the global variable.


### Exemple o Documentation
def readable_timedelta(days):
    ''' Split a nunmber of days in Weeks and days
    INPUT:
    days =  number of days you want to evaluate
    OUTPUT:
    week = number of weeks
    days = number of days'''
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)
readable_timedelta(27)

