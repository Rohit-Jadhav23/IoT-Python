# import mysql connector
import mysql.connector

# create connection with mysql server
connection = mysql.connector.connect(
    host = "localhost",
    port = 3306,
    user = "root",
    password = "root",
    database = "iotdb"
)

# form a query
query = "select * from persons;"

# get a cursor to execute a query
cursor = connection.cursor()

# execute  the query with cursor
cursor.execute(query)

# fetch data from cursor and print it
persons = cursor.fetchall()         # list of tuples
# print(persons)

for p in persons:
    print(p)

# close the cursor
cursor.close()

# close the connection with mysql server
connection.close()