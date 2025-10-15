import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Root@1234",
    database="iotdb"
)

rollno = 99
name = "rohit"
age = 25
std = 17
medium = "marathi"
marks = 16.0  # float, not string

query = "INSERT INTO student (rollno, name, age, std, medium, marks) VALUES (%s, %s, %s, %s, %s, %s);"

data = (rollno, name, age, std, medium, marks)

cursor = connection.cursor()
cursor.execute(query, data)
connection.commit()
cursor.close()
connection.close()
