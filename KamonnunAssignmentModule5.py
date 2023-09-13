#Kamonnun Silarat - Python Assignment Module 5

#Task 1
import random
rolls = int(input("Enter how many dices to roll?: "))
sum = 0
for i in range(rolls):
    dice = random.randint(1, 6)
    print("The number you've got from your rolls: ", dice)
    sum += dice
print("The sum of the numbers are: ", sum)
if rolls <= 0:
    print("Please try again")


#Task 2
numm = []
while True:
    num = (input("Enter the number: "))
    if num == " ":
        break
    try:
        number = int(num)
        numm.append(number)
    except ValueError:
        print("Invalid syntax")
if len(numm) >= 5:
    numm.sort(reverse=True)
    print("The five greatest numbers are: ")
    for i in range(5):
        print(numm[i])
else:
     print("You have entered  less than five numbers, so it cannot find the five greatest numbers.")


#Task 3
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, int(num//2) + 1):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print("This number is not a prime number")


#Task 4
list = []
for i in range(5):
    city = input(f"Enter the name of city {i + 1}: ")
    list.append(city)
print("The city names are:")
for city in list:
    print(city)