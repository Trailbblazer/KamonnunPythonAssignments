#Kamonnun Silarat - Python Assignment Module 4

#Task 1
i = 1
while i in range(1, 1000):
    if i%3==0:
        print(i,end="\n")
    i=i+1


#Task 2
num_inch = int(input("Enter the number in inch: "))
while int(num_inch) >= 0:
    num_cm = num_inch * 2.54
    print(f"{num_inch} inch is equal to {num_cm:.2f} cm")
    num_inch = int(input("Enter the number in inch: "))
if int(num_inch) < 0:
    print("Cannot evaluate")


#Task 3
count = 0
list = []
while True:
    num = input("Enter a number: ")
    if num.isdigit():
        list.append(int(num))
        count += 1
    elif num == " ":
        max_num = max(list)
        min_num = min(list)
        print("The smallest number is: " + str(min_num))
        print("The largest number is: " + str(max_num))
        break
    else:
        print("Try Again")
        break


#Task 4
import random
random_no = random.randint(1, 10)
guess_no = 0
while not guess_no == random_no:
    guess_no = int(input("Enter the number between 1-10: "))
    if guess_no > random_no:
        print("Too high")
    elif guess_no < random_no:
        print("Too low")
    elif guess_no == random_no:
        print("Correct")
else:
    print("End of the guess")
print("Goodbye")


#Task 5
user = input("Enter the username: ")
password = input("Enter your password: ")
attempt = 0
if user != "python" and password != "rules":
    attempt = attempt + 1
while attempt < 5:
    if user != "python" and password != "rules":
        user = input("Enter the username: ")
        password = input("Enter your password: ")
        attempt = attempt + 1
    elif user == "python" and password == "rules":
        print("Welcome")
        break
if attempt >= 5:
    print("Access denied")


#Task 6
import random
n = 0
N = int(input("Enter how many points you want to generate?: "))

for i in range(N):
    A = random.uniform(-1, 1)
    B = random.uniform(-1, 1)
    if A**2+B**2 <1:
        n=n+1
pi = 4*n/N
print("Approximate value of pi is: ", pi)