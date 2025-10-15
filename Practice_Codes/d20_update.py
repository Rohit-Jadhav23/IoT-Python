import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Root@1234",
    database="iotdb"
)

rollno = 100
name = "Alyonushka"

query = f"update student SET name = '{name}' where rollno={rollno};"

# get a cursor to execute a query
cursor = connection.cursor()

# execute  the query with cursor
cursor.execute(query)

# commit your changes on database server
connection.commit()

# close the cursor
cursor.close()

# close the connection with mysql server
connection.close()