#Kamonnun Silarat - Python Assignment Module 3

#Task1
l_zander = float(input("Enter the length of a zander in centimeters: "))
if l_zander >= 42:
    print("A zander is meet the size limit. ")
else:
    print("A zander is not meet the size limit. ")

#Task 2
cabin_class = str(input("Enter the cabin class of a cruise ship: "))
if cabin_class == "LUX":
    print("upper-deck cabin with a balcony")
elif cabin_class == "A":
    print("above the car deck, equipped with a window")
elif cabin_class == "B":
    print("windowless cabin above the car deck")
elif cabin_class == "C":
    print("windowless cabin below the car deck")
else:
    print("Invalid cabin class")

#Task 3
bio_gender = str(input("Enter your biological gender: "  ))
if bio_gender == 'male':
    hemo_value_m = int(input("Enter your hemoglobin value in g/l: "))
    if (hemo_value_m >= 134 and hemo_value_m <= 167):
        print("Your hemoglobin value is normal.")
    elif hemo_value_m > 167:
        print("Your hemoglobin value is high.")
    elif hemo_value_m < 134:
        print("Your hemoglobin value is low.")
    else:
        print("Try again")
if bio_gender == 'female':
    hemo_value_f = int(input("Enter your hemoglobin value in g/l: "))
    if (hemo_value_f >= 117 and hemo_value_f <= 155):
        print("Your hemoglobin value is normal.")
    elif hemo_value_f > 155:
        print("Your hemoglobin value is high.")
    elif hemo_value_f < 117:
        print("Your hemoglobin value is low.")
    else:
        print("Try again")

#Task 4
year = int(input("Please enter the year: "))
year01 = year%4
year02 = year%100
year03 = year%400
if year01 == 0:
    print("the year is on leap year")
elif year02 == 0:
    print("the year is on leap year")
elif year03 == 0:
    print("the year is on leap year")
else:
    print("the year is not on leap year")