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
uid = 6

query = f"delete from persons where uid = {uid};"

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