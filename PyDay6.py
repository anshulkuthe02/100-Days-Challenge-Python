'''

num = 1
while num <= 100:
    if num%2 == 0:
        print(num,end=":Even\n")
    else:
        print(num,end=":Odd\n")
    num += 1

'''

nums = 105
while nums > 1:
    if nums%7 == 0:
        print(nums,end="\n")
    nums -= 7
    
'''

def sum(a,b):
    return a + b
result = sum(12,28)
print(result)

'''
'''
#default parameters
def greet(name):
    print(f"Hello {name}")
greet("AK")
'''

'''
def nums(*ak):
    for i in ak:
        print(i)

nums(1,2,3,4,5,6,7,8,"ak","bccci")
'''
'''

#Temperature converter
temp = int(input("Enter temperature: "))
unit = input("Enter unit: ")
def temp_con(temp,unit):
    if unit == 'f' or unit == 'F':
        temp = (temp*(9/5))+32
        print(f"Celsius to Fahrenheit: {temp}")
    elif unit == 'c' or unit == 'C':
        temp = (temp - 32)*(5/9)
        print(f"Fahrenheit to Celsius: {temp}")
    else:
        print("Invalid keyword")

temp_con(temp,unit)
'''



