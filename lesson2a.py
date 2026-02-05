# a python list is a collection of items orderd in a certain way
# a list is introduced by the use of the square brackets[]
# the items of a list are stored inside of indices NOTE: in programing we start cunting from index 0
# a lis is mutablr i.e its content can change

cars = ["BMW", "Benze", "Hiance", "Bugatti", "Probox", "Mercedes","Porche"]
print(cars)

# accesing items of a list
print(cars[2])
print("The car on index four is :", cars[4])


# list slicing - this is creating a list from a given bigger list
print(cars[4:])
print(cars[:4])
# printing from hiance to probox
print(cars[2:5])

# list mutability
# we use the function append to add an item at the end of a list
cars.append("Cadillac")
print(cars)

cars.append("Subaru")
print(cars)

# we use the pop function to remove an item at th end of list
cars.pop()
print(cars)

# we can use an index to add an item to a list
cars[5] = "Pajero"
print(cars)

# we can use the sort fuction to sort out items in alphabetical order
cars.sort()
print(cars)


