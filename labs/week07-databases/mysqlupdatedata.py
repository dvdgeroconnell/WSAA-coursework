# Lab07.02 exercise 5 - mysqlupdatedata.py
# Update a database entry by id using a python script
# Author(s): David O'Connell, Andrew Beatty

import mysql.connector

# Set up the connection with the database
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database="wsaa2"
)
# update the student
mycursor = mydb.cursor()
sql = "UPDATE student SET name = %s, age = %s where id = %s"
values = ("Daniel", 33, 1)
mycursor.execute(sql, values)

# Commit the change
mydb.commit()

# Close the cursor, close the connector to free up the connection.
# They should time out after an hour anyway.
mycursor.close()
mydb.close()
