import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='people',
    user='dbuser',
    password='pass_word',
    autocommit=True
)
def getemployeesbylastname(last_name):
    sql = "SELECT ID, lastname, firstname, salary FROM employees"
    sql += " WHERE lastname='" + last_name + "'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"Hello! I'm {row[2]} {row[1]}. My salary is {row[3]} euros per month.")
    return

n = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='people',
    user='dbuser',
    password='pass_word',
    autocommit=True
)
def UPDATESalary(id, new_salary):
    sql = "UPDATE employees SET salary=" + str(new_salary)+ "WHERE ID=" + str(id)
    sql += " WHERE lastname='" + last_name + "'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"Hello! I'm {row[2]} {row[1]}. My salary is {row[3]} euros per month.")
    return

last_name = input("Enter last name: ")
getemployeesbylastname(last_name)
id = input("Enter id number: ")
newSalary = float(input("Enter new salary: "))

