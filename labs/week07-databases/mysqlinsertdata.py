# Lab07.02 exercise 3 - mysqlinsertdata.py
# Insert a row into a database table using a python script
# Author(s): David O'Connell, Andrew Beatty

import mysql.connector

# Set up the connection with the database
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database="wsaa2"
)
# add the student
mycursor = mydb.cursor()
sql = "INSERT INTO student (name, age) values (%s, %s)"
values = ("Mary", 21)
mycursor.execute(sql, values)

# Commit the change, close the cursor, close the connector to free up the connection.
# They should time out after an hour anyway.
mydb.commit()
print("1 record inserted, ID: ", mycursor.lastrowid)
mycursor.close()
mydb.close()
