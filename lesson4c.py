# a for loop can also be used to iterate a tuple , a string or a dictionary

name = "Vanessa"

for letter in name:
    if letter == "n":
        print("this is letter n")
    else:
        print(letter)

print("====================")   
# below is a list of counties
counties = ["Nairobi", "Mombasa", "Kisumu", "Nakuru", "Eldoret", "Kajiado", "Machakos", "Meru", "Embu"]

print(counties)

for county in counties:
    print(county)

print("==========================")

# for county in counties:
#     if "":
#         print(county)
#     else:
#         print("not found")

print("==========================")

player = {
    "name" : "Mbappe",
    "age" : 25,
    "teams" : ["PSG", "Monaco", "France"],
    "nationality":"French" 

}

for key in player:
    print(key)

for value in player:
    print(player[value]) 
#     # loop through the teams
for teams in player["teams"]:
    print(teams)       


