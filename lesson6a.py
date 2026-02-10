# python module - a file that contains python definitions, statement and/or function

def add():
    num1 = 20
    num2 = 30
    sum = num1 + num2
    print("The answer is :", sum)

def subtract():
    x = 6
    y = 4
    difference = x - y
    print(difference)



# these functions defined above can be called in another file

def rectangle_area():
    length = int(input("Enter the length:"))
    width = int(input("Enter the width:"))

    area = length * width
    print("The area of the rectangle is", area)