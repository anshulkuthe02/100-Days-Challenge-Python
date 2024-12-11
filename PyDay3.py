'''

#Even/Odd number
a = int(input("Enter the number:"))
if a%2==0:
    print("Even number:",a)
else:
    print("Odd number:",a)

'''

#Pizza Billing System
print("Welcome to Dominos pizza")
size = input("What size of pizza is required?(S,M,L)")
peperonni = input("Do you want extra peperonni on pizza(Y/N)?")
extra_cheese = input("Do you wanna extra cheese on pizza(Y/N)")
bill = 0
if size == "S":
    print("It costs $15")
    bill += 15
    if peperonni == "Y":
        bill += 2
elif size == "M":
    print("It costs $20")
    bill += 20
    if peperonni == "Y":
        bill += 3
elif size == "L":
    print("It costs $25")
    bill += 25
    if peperonni == "Y":
        bill += 5

if extra_cheese == "Y":
    print("It cost $1")
    bill += 1

print(f"The total bill is:${bill}")
