# loops-sometimes we may need to do a piece of work a no of repeated tyms and in such cases we may use loops.
#  a loop is a control structure that allows us to execute a block of code repeatedly until a certain condition is met.
# there are two types i.e the for loop and the while loop.
# below is a syntax of a for loop
"""
for variable in range(n):
      # block of code to be repeated exected
"""

for greeting in range(5):
    print("Hello Moses" , greeting)

print("========================")  

for number in range(10,21):
    print(number)


print("===========================")

# find the even numberrs in range of 50 - 71
for number in range(50, 71, 2):
    print(number) 


print("============================")

# odd numbers from 100 - 150
for number in range(101, 150, 2):
    print(number)


print("============================")
# a program tha prints multiples of 3 starting from 201 - 150
for number in range(201, 151, -3):
    print(number)


print("============================")
# leap years btn 2000 and 2024
for number in range(2000, 2025):
    if number % 4 == 0:
        print(number)

    
