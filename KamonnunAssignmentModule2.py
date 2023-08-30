#Kamonnun Silarat - Python Assignment Module 2

#Task 1
print("Hello, Kamonnun")

#Task 2
import math
pi = math.pi
r =  float(input("Enter the radius of the circle: "))
area_c = pi * r**2
print(f"The area of the circle: {float(area_c):.2f} units^2")

#Task 3
l = int(input("Enter the length of a rectangle: "))
w = int(input("Enter the width of a rectangle: "))
perimeter_r = l + w + l + w
area_r = l * w
print(f"The perimeter of the rectangle is {int(perimeter_r)} units and area of the rectangle is {int(area_r)} units^2 respectively." )

#Task 4
a = int(input("Enter first value: "))
b = int(input("Enter second value: "))
c = int(input("Enter third value: "))
sum = a+b+c
product = a*b*c
average = sum/3
print(f"Sum: {sum}, Product: {product} Average: {average:.1f}" )
print()

#Task 5
t = float(input("Enter talents: "))
p = float(input("Enter pounds: "))
l = float(input("Enter lots: "))
talent = t*20*32*13.3
pound = p*32*13.3
lots = l*13.3
tpl = talent+pound+lots
kg = int(tpl/1000)
g = tpl-kg*1000
print(f"The weight in modern units: {(kg):} kg and {float(g):.2f} grams." )

#Task 6
import random
n611 = str(random.randint( 0, 9))
n612 = str(random.randint( 0, 9))
n613 = str(random.randint( 0, 9))

n621 = str(random.randint( 1, 6))
n622 = str(random.randint( 1, 6))
n623 = str(random.randint( 1, 6))
n624 = str(random.randint( 1, 6))

print(n611+n612+n613)
print(n621+n622+n623+n624)