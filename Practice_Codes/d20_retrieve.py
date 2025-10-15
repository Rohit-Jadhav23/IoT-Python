import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Root@1234",
    database="iotdb"
)

# form a query
query = "select * from student;"

# get a cursor to execute a query
cursor = connection.cursor()

# execute  the query with cursor
cursor.execute(query)

# fetch data from cursor and print it
student = cursor.fetchall()         # list of tuples
# print(persons)

for p in student:
    print(p)

# close the cursor
cursor.close()

# close the connection with mysql server
connection.close()