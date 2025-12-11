#problem-1

a = float(input('Input the First Number: '))

b = float(input('Input the Second Number: '))

if a > b : 
    print(f'{a} is greater than {b}.')

elif b > a : 
    print(f'{b} is greater than {a}.')

else:
    print(f"{a} is equal to {b}.")

#problem-2

gen = input('Input Your Gender: ')
if gen == 'm' or gen =="M":
    print("Hello Sir, How are you")
elif gen == 'f' or gen =="F":
    print("Hello Mam, How are you")
else:
    print("Wrong input ! please enter valid inputs only : m or f.")

#problem-3

num = int(input("Input Number: "))

if num % 2 == 0 :
    print(f"{num} is an Even number.")
else:
    print(f"{num} is an Odd number.")

#problem-4

age = int(input('Input your age: '))

if age >= 18:
    print("You are eligible to vote.")
else:
    print(f"you have {18-age} years more left to be eligible.")

#problem-5

num = int(input("Tell number: "))

if num == 1 :
    print("Monday")
elif num == 2 :
    print("Tuesday")
elif num == 3 :
    print("Wednesday")
elif num == 4:
    print("Thursday")
elif num == 5 :
    print("Friday")
elif num == 6 :
    print("Saurday")
elif num == 7 :
    print("Sunday")
else:
    print('Please enter a valid number between "1-7".')

#problem-6

a = int(input('input a: '))
b = int(input('input b: '))
c = int(input('input c: '))

if a==b and b==c and c==a:
    print("All 3 of them are equal.")

elif a==b or b==c or c==a:
    print("Any 2 are equal")

elif a > b and a > c :
    print(f"{a} is the greatest number.")

elif c > b and c > a :
    print(f"{c} is the greatest number.")

else:
    print(f"{b} is the greatest number.")

#problem-7

year = int(input("Year: "))

if year % 100 == 0 and year % 400 == 0:
    print("Its a leap year and century year too.")

elif year % 100 != 0 and year % 4 == 0 :
    print("Its a leap year.")

else:
    print('Its not a leap year.')

#problem-8

# long method

total = float(input('Total: '))
disc1 = (total/10)
disc2 = (total/5)

bill1 = total - disc1
bill2 = total - disc2

if total >=1000 and total <5000:
    print(f"Your discount is {disc1} and your bill is : {bill1} ")

elif total >= 5000  :
    print(f"Your discount is {disc2} and your bill is : {bill2} ")

else:
    print(f"Your discount is 00 and your bill is : {total} ")

#short 

total = float(input('Total: '))

if total >= 1000 and total < 5000:
    print(f"You got 10% off.Your bill is : {((total)*90/100)}.")
elif total>= 5000:
    print(f"You got 20% off.Your bill is : {((total)*80/100)}.")
else:
    print(f"Your bill is : {total}.")

#problem - 9 :

char = input("Input Alphabet: ")

if char in "aeiouAEIOU":
    print(f"{char} is a vowel.")
else:
    print(f"{char} is a constant.")