#BMI calculator + f-string
height = 1.85; weight = 84
bmi_cal = weight/(height ** 2)
print(f"The bmi comes to be: {bmi_cal}")


#Bill calculator + f-string
print("welcome to tip calculator")
bill = float(input("enter the bill:"))
tip = float(input("Enter the tip:"))
total = bill * (bill/100) + tip
print(f"The total is: ${total}")
no = int(input(("enter number of people:")))
print(f"The total for each is: ${float(round((tip+bill)/no,2))}")