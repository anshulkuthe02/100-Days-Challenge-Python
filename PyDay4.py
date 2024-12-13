import random
'''
print("Welcome to Rock Paper Scissors Game")

user = int(input("Enter 1 for Rocks 2 for Papers 3 for Scissors\n"))
trial = random.randint(1,3)
print(trial)

if user > 3 or user < 1:
    print("Invalid value. You lose")
elif user == 1 and trial == 3:
    print("User wins")
elif user == 3 and trial == 1:
    print("System wins")
elif user > trial:
    print("User wins")
elif user < trial:
    print("System wins")
elif user == trial:
    print("It's a draw")
'''
city = ["Mumbai","Pune","Nagpur","Bhandara","Kolkata","Kolhapur","Satara","Sangli","Nashik","Palghar","Thane"]
print(city)

#print the given city on the given index
print(city[1])

# print the following data onwards from given index
print(city[1:])

#replaces the data on given index
city[4] = "Dhule" #Kolkata is replaced by Dhule
print(city)


#random city picker
print(random.choice(city))

#print the given text from the given position and seperates all text from it
city[6:] = "Shimla"
print(city[0:])