import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Root@1234",
    database="iotdb"
)

name = "Xena"
query = "DELETE FROM student WHERE name = %s;"
cursor = connection.cursor()
cursor.execute(query, (name,))
connection.commit()
cursor.close()
connection.close()
