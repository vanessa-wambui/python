# python functions
# they are a block of code/statements that perform a given task/action
# they can be reused throughout the program to perform diff tasks.
# Functions are defined using the (def) keyword
# We have two main types of functions i.e:
# 1. in-built - they come pre-installed in the intepreter eg print(), pop(), append(), etc..
# 2. User Defined Functions - they are created by a programmer to solve a given tasks.
# To define the function you need to give it a name followed by parenthesis
# For the fuction body it is usually indented and to involke a function we use the function name.

def greetings():
    print("Hello, how are you?")

# below we call the function by use of its name
greetings() 

print("==============================")
# addition function
def addition():
    num1 = 40
    num2 = 50
    sum = num1 + num2
    print("The sum of the number is", sum)

addition() 
print("==============================")
# create a funtion to multipli 3 values

def multiplication():
    num1 = 3
    num2 = 3
    num3 = 5
    multiplication = num1 * num2 * num3
    print("the product of the 3 is", multiplication) 

multiplication()
print("==============================")
#below is a division function
def divide():
    number1 = int(input("Enter the first nuumber: "))
    number2 = int(input("Enter the 2nd number: "))
    quotient = number1 / number2
    print("The answer is: ", quotient)
    print("-------")

for function in range(3):
    divide()          


