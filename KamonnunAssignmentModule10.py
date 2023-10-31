#Kamonnun Silarat - Python Assignment Module 10

#Task 1

class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current = bottom

    def floor_up(self):
        if self.current < self.top:
            self.current += 1
            print(f"Going up. Current floor is {self.current}")
        else:
            print("You're already at the top floor.")
    def floor_down(self):
        if self.current > self.bottom:
            self.current -= 1
            print(f"Going down. Current floor is {self.current}")
        else:
            print("You're already at the bottom floor.")

    def go_to_floor(self, floor):
        while self.current != floor:
            if self.current < floor:
                self.floor_up()
            elif self.current > floor:
                self.floor_down()

h = Elevator(1, 7)
h.go_to_floor(5)
h.go_to_floor(1)


# Task 2

class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current = bottom

    def floor_up(self):
        if self.current < self.top:
            self.current += 1
            print(f"Going up. Current floor is {self.current}")
        else:
            print("You're already at the top floor.")
    def floor_down(self):
        if self.current > self.bottom:
            self.current -= 1
            print(f"Going down. Current floor is {self.current}")
        else:
            print("You're already at the bottom floor.")

    def go_to_floor(self, floor):
        while self.current != floor:
            if self.current < floor:
                self.floor_up()
            elif self.current > floor:
                self.floor_down()

class Building:
    elevator_lists = []
    def __init__(self, bottom, top, elevator_no):
        self.bottom = bottom
        self.top = top
        self.elevator_no = elevator_no
        self.elevator_lists = [Elevator(bottom, top) for _ in range(elevator_no)]

    def moving_elevator(self, elevator_no, l_floor):
        if 0 <= elevator_no < len(self.elevator_lists):
            h = self.elevator_lists[elevator_no]
            print(f"Moving elevator no. {elevator_no + 1} to Floor {l_floor}.")
            h.go_to_floor(l_floor)

b = Building(1, 7, 4)
b.moving_elevator(0, 7)
b.moving_elevator(1, 1)
b.moving_elevator(2, 4)
b.moving_elevator(3, 2)


# Task 3

class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current = bottom

    def floor_up(self):
        if self.current < self.top:
            self.current += 1
            print(f"Going up. Current floor is {self.current}")
        else:
            print("You're already at the top floor.")
    def floor_down(self):
        if self.current > self.bottom:
            self.current -= 1
            print(f"Going down. Current floor is {self.current}")
        else:
            print("You're already at the bottom floor.")

    def go_to_floor(self, floor):
        while self.current != floor:
            if self.current < floor:
                self.floor_up()
            elif self.current > floor:
                self.floor_down()

class Building:
    elevator_lists = []
    def __init__(self, bottom, top, elevator_no):
        self.bottom = bottom
        self.top = top
        self.elevator_no = elevator_no
        self.elevator_lists = [Elevator(bottom, top) for _ in range(elevator_no)]

    def moving_elevator(self, elevator_no, l_floor):
        if 0 <= elevator_no < len(self.elevator_lists):
            h = self.elevator_lists[elevator_no]
            print(f"Moving elevator no. {elevator_no + 1} to Floor {l_floor}.")
            h.go_to_floor(l_floor)

    def fire_alarm(self):
        for h in self.elevator_lists:
            h.go_to_floor(self.bottom)
        print("Fire alarm is ringing!, all elevators will moving down to bottom floor!")

b = Building(1, 12, 4)
b.moving_elevator(0, 7)
b.moving_elevator(1, 1)
b.moving_elevator(2, 4)
b.moving_elevator(3, 11)
b.fire_alarm()

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

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

    def print_status(self):
        print(f"Race Status:")
        print(f"{'Registration number':<15} {'Maximum speed':<15} {'Current Speed':<15} {'Travelled Distance':<15}")
        for car in self.cars:
            print(f"{car.reg_no:<19} {car.max_speed:<15} {car.current_speed:<15} {car.trv_distance:<15}")

    def race_finished(self):
        return any(car.trv_distance >= self.distance for car in self.cars)

cars = [Car(f"ABC-{i+1}", random.randint(100, 200)) for i in range(1, 10)]
gdd = Race("Grand Demolition Derby", 8000, cars)

time = 0
while not gdd.race_finished():
    gdd.hour_passes()
    time += 1

    if time % 10 == 0 or gdd.race_finished():
        gdd.print_status()

print("Done Racing!!!!!")