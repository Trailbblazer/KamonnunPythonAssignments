#Kamonnun Silarat - Python Assignment Module 7

#Task 1
seasons = ("spring", "summer", "autumn", "winter")
month_num = int(input("Enter a number of month: "))
if 1 <= month_num <= 12:
    season = seasons[(month_num - 3)//3]
    print(f"Month {month_num} is {season}.")
else:
    print("Invalid input")


#Task 2
set_name = set()
while True:
    name = input("Enter the name: ")
    if name == "":
        break
    if name in set_name:
        print("Existing name")
    else:
        print("New name")
    set_name.add(name)
print("The name in the lists are: ")
for name in set_name:
    print(name)


#Task 3
airport = {}
while True:
    print("Choose an option:\n")
    print("1. Enter new airport")
    print("2. Fetch airport information")
    print("3. Quit")
    choice = input("Enter your choice 1-3: ")

    if choice == "1":
        icao = input("Enter ICAO code: ").strip().upper()
        airport_name = input("Enter the name of airport: ")
        airport[icao] = airport_name
        print(f"Airport '{airport_name}' with ICAO code '{icao}' is added.")

    elif choice == "2":
        icao = input("Enter ICAO code: ").strip().upper()
        if icao in airport:
            print(f"Airport Name: {airport[icao]}")
        else:
            print("Airport not found")

    elif choice == "3":
        print("Quit")
        break
    else:
        print("Invalid choice")