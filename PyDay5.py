##Prime number finder
'''

for i in range(1,101):
    if i > 1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print("Prime number:", i)

             '''

##Fizz-buzz finder
'''
for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)

'''

##Sum of natural numbers
'''            
sum = 0                
for i in range(1,101):
    sum += i
print("Sum is:", sum)
'''

##Password Generator
import random

length = int(input("Enter the length: "))

alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
nums = [0,1,2,3,4,5,6,7,8,9]
chars = [',','.','/',';',':','+','-','=','*','%','#','@','!','$']

alpha  = int(input("Enter no. of alphabets: "))
num = int(input("Enter no. of nums: "))
char = int(input("Enter no. of chars: "))

password = ''

if alpha+num+char == length:
    for j in range(0,1):
        for i in range(alpha):
            alpha1 = random.choice(alphabets)
            password += alpha1

        for i in range(num):
            num1 = random.randint(0,9)
            ##print(num1)
            password += str(num1)

        for i in range(char):
            char1 = random.choice(chars)
            ##print(char1)
            password += char1

        print("Password:",password)

else:
    print("Error! Choice out of length")