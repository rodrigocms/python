#Scripting With Raw Input
#We can get raw input from the user with the built-in function input, which takes in an optional string argument that you can use to specify a message to show to the user when asking for input.

name = input("Enter your name: ")
print("Hello there, {}!".format(name.title()))
# This prompts the user to enter a name and then uses the input in a greeting. The input function takes in whatever the user types and stores it as a string. If you want to interpret their input as something other than a string, like an integer, as in the example below, you need to wrap the result with the new type to convert it from a string.

num = int(input("Enter an integer"))
print("hello" * num)
# We can also interpret user input as a Python expression using the built-in function eval. This function evaluates a string as a line of Python.

result = eval(input("Enter an expression: "))
print(result)
# If the user inputs 2 * 3, this outputs 6.


# Exemple 1

names = input("Enter names separated by commas: ").title().split(",")
assignments = input("Enter assignment counts separated by commas: ").split(",")
grades = input("Enter grades separated by commas: ").split(",")

# message string to be used for each student
# HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

for names, assignments, grades in zip(names, assignments, grades):
    print( names, assignments, grades )




# write a for loop that iterates through each set of names, assignments, and grades to print each student's message

