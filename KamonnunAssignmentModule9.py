#Kamonnun Silarat - Python Assignment Module 9

#Task 1:

class Car:
    def __init__(self, reg_no, max_speed):
        self.reg_no = reg_no
        self.max_speed = max_speed
        self.current_speed = 0
        self.trv_distance = 0

car01 = Car("ABC-123", 142)
print(f"Car Details:\nRegistration number is {car01.reg_no}\nMaximum Speed is {car01.max_speed} km/h")
print(f"Current Speed is {car01.current_speed} km/h\nTravelled Distance is {car01.trv_distance} km")


# Task 2

class Car:
    def __init__(self, reg_no, max_speed):
        self.reg_no = reg_no
        self.max_speed = max_speed
        self.current_speed = 0
        self.trv_distance = 0

    def accelerate(self, changespeed):
        self.current_speed = min(max(self.current_speed + changespeed, 0), self.max_speed)

car01 = Car("ABC-123", 142)
car01.accelerate(30)
car01.accelerate(70)
car01.accelerate(50)
print(f"Current Speed is {car01.current_speed} km/h")
car01.accelerate(-200)
print(f"Final Speed is {car01.current_speed} km/h")

#Task 3

class Car:
    def __init__(self, reg_no, max_speed):
        self.reg_no = reg_no
        self.max_speed = max_speed
        self.current_speed = 0
        self.trv_distance = 0

    def accelerate(self, changespeed):
        self.current_speed = min(max(self.current_speed + changespeed, 0), self.max_speed)

    def drive(self, time):
        self.trv_distance += self.current_speed * time

car01 = Car("ABC-123", 142)
car01.accelerate(30)
car01.accelerate(70)
car01.accelerate(50)
print(f"Current Speed is {car01.current_speed} km/h")
car01.drive(1.5)
print(f"Travelled distance is {car01.trv_distance} km/h")

# Task 4
import random

class Car:
    def __init__(self, reg_no, max_speed):
        self.reg_no = reg_no
        self.max_speed = max_speed
        self.current_speed = 0
        self.trv_distance = 0

    def accelerate(self, changespeed):
        self.current_speed = min(max(self.current_speed + changespeed, 0), self.max_speed)

    def drive(self, time):
        self.trv_distance += self.current_speed * time

cars = [Car(f"ABC-{i+1}", random.randint(100, 200)) for i in range(1, 10)]

r_distance = 10000
time = 1

while all(car.trv_distance < r_distance for car in cars):
    print(f"Race time: {time} hour(s)")

    for car in cars:
        car.accelerate(random.randint(-10, 15))
        car.drive(1)

    print(f"Race Status:")
    print(f"{'Registration number':<15} {'Maximum speed':<15} {'Current Speed':<15} {'Travelled Distance':<15}")
    for car in cars:
        print(f"{car.reg_no:<19} {car.max_speed:<15} {car.current_speed:<15} {car.trv_distance:<15}")
    time += 1

print("Done Racing!!!!!")