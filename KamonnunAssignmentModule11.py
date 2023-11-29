# Kamonnun Silarat - Python Assignment Module 11

# Task 1

class Publication:
    def __init__(self, name):
       self.name = name

class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print("Book Information:")
        print(f"Name: {self.name}\nAuthor: {self.author}\nPage Count: {self.page_count}\n")

class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print("Magazine Information:")
        print(f"Name: {self.name}\nChief Editor: {self.chief_editor}")

book_info = Book(name="Compartment No. 6", author="Rosa Liksom", page_count=192)
magazine_info = Magazine(name="Donald Duck", chief_editor="Aki Hyyppä")

book_info. print_information()
magazine_info. print_information()


# Task 2

class Car:
    def __init__(self, reg_no, max_speed):
        self.reg_no = reg_no
        self.max_speed = max_speed
        self.current_speed = 0
        self.trv_distance = 0

    def accelerate(self, change_speed):
        self.current_speed = min(max(self.current_speed + change_speed, 0), self.max_speed)

    def drive(self, time):
        self.trv_distance += self.current_speed * time

class ElectricCar(Car):
    def __init__(self, reg_no, max_speed, battery_capacity):
        super().__init__(reg_no, max_speed)
        self.battery_capacity = battery_capacity

class GasolineCar(Car):
    def __init__(self, reg_no, max_speed, tank_volume):
        super().__init__(reg_no, max_speed)
        self.tank_volume = tank_volume

car01 = ElectricCar(reg_no="ABC-15", max_speed=180, battery_capacity=52.5)
car02 = GasolineCar(reg_no="ACD-123", max_speed=165, tank_volume=32.3)

car01.accelerate(change_speed=45)
car02.accelerate(change_speed=30)

car01.drive(time=3)
car02.drive(time=3)

print("The Values for the cars' kilometer counters (Already driven for 3 hours):")
print(f"The electric car ({car01.reg_no}) has travelled {car01.trv_distance} km.")
print(f"The gasoline car ({car02.reg_no}) has travelled {car02.trv_distance} km.")
