
# COMPLEX BOOLEAN EXPRESSIONS
if 18.5 <= weight / height**2 < 25:
    print("BMI is considered 'normal'")

if is_raining and is_sunny:
    print("Is there a rainbow?")

if (not unsubscribed) and (location == "USA" or location == "CAN"):
    print("send email")
# For really complicated conditions you might need to combine some ands, ors and nots together. 
# Use parentheses if you need to make the combinations clear.

# However simple or complex, the condition in an if statement must be a boolean expression that evaluates 
# to either True or False and it is this value that decides whether the indented block in an if statement 
# executes or not.









lst_1 = ['a','b','c','d']
lst_2 = ['a','d']

for i in lst_2: 
    lst_1.remove(i)

print(lst_1)    