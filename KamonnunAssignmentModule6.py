#Kamonnun Silarat - Python Assignment Module 6

#Task 1
import random
def dice():
    return random.randint(1, 6)

if __name__ == "__main__":
    rolls = 0
    while True:
        result = dice()
        rolls +=1
        print(f"Roll {rolls} is {result}")
        if result == 6:
            break

    print(f"You got number 6 dice, You have rolled for {rolls} rolls.")


#Task 2
import random
def dice(sides):
    return random.randint(1, sides)
rolls = 0

if rolls == 0:
    sides = int(input("Enter the number of sides of the dice: "))
    max_no = int(input("Enter the maximum number of the dice: "))


    while True:
        result = dice(max_no)
        rolls += 1
        print(f"Roll {rolls} is {result}")

        if result == max_no:
            break

    print(f"You have rolled the maximum number {max_no}. You have rolled for {rolls} roll(s).")


#Task 3
def g_to_l(gallons):
    liters = gallons * 3.785
    return liters

while True:
    gallons = float(input("Enter a volume in gallons: "))
    if gallons < 0:
        print("Cannot evaluate")
        break
    else:
        liters = g_to_l(gallons)
        print(f"{gallons} gallons is equal to {liters} liters.")


#Task 4
list = [1, 2, 3, 4, 5]
def sum(lists, n):
    if n == 0:
        return 0
    else:
        return lists[n-1] + sum(lists, n-1)

total = sum(list, len(list))
print("The total sum of all numbers in given list is: ", total)


#Task 5
def num(list):
    even = [num for num in list if num % 2 == 0]
    return even
lists = [3, 5, 7, 12, 8, 9]
print("Default lists: ", lists)
new_lists = num(lists)
print("New lists: ", new_lists)


#Task 6
import math
def unit_price(d, p):
    r = d /  2
    a_cm2 = math.pi * r**2
    a_m2 = a_cm2 * 10000
    unpr_m2 = p/a_m2
    return unpr_m2

d_pizza1 = float(input("Enter the diameter of the first pizza in cm: "))
p_pizza1 = float(input("Enter the price of the first pizza in euros: "))
d_pizza2 = float(input("Enter the diameter of the second pizza in cm: "))
p_pizza2 = float(input("Enter the price of the second pizza in euros: "))

if unit_price(d_pizza1, p_pizza1) < unit_price(d_pizza2, p_pizza2):
    print("The first pizza provides better value for money.")
elif unit_price(d_pizza1, p_pizza1) > unit_price(d_pizza2, p_pizza2):
    print("The second pizza provides better value for money.")
elif unit_price(d_pizza1, p_pizza1) == unit_price(d_pizza2, p_pizza2):
    print("Both pizzas have the same unit price.")