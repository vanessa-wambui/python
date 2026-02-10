# while loop-execute a block of code repeatedly as long as certain conditions are true
# Syntax of a while loop
"""
initialize of a variable
while keyword,
followed by the condition to be evaluated,
followed by a full colon(:)
code to be printed out,
increment/decrement
"""

number = 0
while number < 5:
    print("Hello Moses", number)
    number = number + 1


print("================") 

number = 50
while number < 71:
    print(number)
    number = number + 2


# below is a decrement that prints multiples of 3 from  201 - 150
number = 201
while number >= 150:
    print(number)
    number = number - 3
    # python function both with and without parameteres
    #a function-a block of reusable code
    # parameter - are variables you put inside the function so it can receive values when it's called.
    # the syntax:
    """
    def function_name(parameter 1, parameter 2)
    """
def greet(name):
    print("Hello",name)

greet("Vanessa")    
# a python function without parameters

    