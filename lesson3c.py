# a dictionary is a data type that stores data in terms of key-value pair
# it os introduced by th use of curly braces{}
# the values stored can be of any data type
# to access the values in a dictionary we use the keys


phonebook = {
    "Benson" : "254556667",
    "Mary" : "25433377688",
    "Stephen" : "254386868"
}

# showing the entire dictionary
print(phonebook)
print(type(phonebook))

# print out benson's number
print(phonebook["Benson"])


player = {
    "name" : "Messi",
    "age" : 40,
    "teams":["PSG", "Barcelona", "Argentina"]
}
# print barcelona - the second team he played for
print(player["teams"][1])


