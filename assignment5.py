#  create a function without parameters
def message():
    print("The delivery is ready.")

message()

# a fuction that uses arithmetic operaters to calculate area os a rectangle
def area():
    num1 = 2
    num2 = 3
    product = num1 * num2
    print("The area of rectangle is:",product)
    
area()
print("=================")   
# a function with parameters that accepts two numbers
def numbers(num1 , num2):
    num1 = 5
    num2 = 3
    sum = num1 + num2
    print(sum)
    num1 = 5
    num2 = 3
    difference = num1 - num2
    print(difference)
    num1 = 5
    num2 = 3
    product = num1 * num2
    print(product)
    num1 = 5
    num2 = 3
    division = num1 / num2
    print(division)


numbers(5,3) 
print("=================")   
#Q3
number = int(input("Enter number: "))

if number == 0:
    print("zero")
elif number > 0:
    print("positive") 
else:
    print("negative")

print("=================")   
# Q4
def sum_of_numbers(n):
    sum=0
    for i in range(1, n+1):
        sum+=i
        print("The sum of numbers from 1 to", n,"is:", sum )

    





   






   












 