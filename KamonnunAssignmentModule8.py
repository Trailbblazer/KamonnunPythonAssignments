#Kamonnun Silarat - Python Assignment Module 8

#Task 1
import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='airport',
         user='newuser',
         password='user_password',
         autocommit=True
)

def getairportdata(icao):
    sql = "select ident, airport.name, country.name from airport, country "
    sql += "where airport.iso_country = country.iso_country and ident ='" + icao + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for index, row in enumerate(result, start=1):
            print(f"Airport info: {row[0]}, {row[1]} \nLocation: {row[2]}")
    else:
        print(f"No airport data")
icao = input("Enter ICAO code of the airport: ")
getairportdata(icao)


#Task 2
def getairportdatafromccode(country):
    sql = "select name, type from airport where iso_country ='" + country + "'" + " order by type "
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"The airport is {row[0]}, {row[1]}")
    return

country = input("Enter country code: ")
getairportdatafromccode(country)


#Task 3
from geopy.distance import geodesic

def distance1(ident1):
    sql = "select latitude_deg, longitude_deg from airport where ident ='" + ident1 + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    location1 = result
    if cursor.rowcount > 0:
        for row in result:
            print(f"The latitude is: {row[0]}, the longitude is: {row[1]}")
    return location1

ident1 = input("Enter first ICAO code: ")
distance1(ident1)


def distance2(ident2):
    sql = "select latitude_deg, longitude_deg from airport where ident ='" + ident2 + "'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    location2 = result
    if cursor.rowcount > 0:
        for row in result:
            print(f"The latitude is: {row[0]}, the longitude is: {row[1]}")
    return location2

ident2 = input("Enter second ICAO code: ")
distance2(ident2)

airport01 = distance1(ident1)
airport02 = distance2(ident2)

print("The distance between two airports is: ", geodesic(airport01, airport02))