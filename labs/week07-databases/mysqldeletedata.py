# Lab07.02 exercise 6 - mysqldeletedata.py
# View a database entry by id using a python script
# Author(s): David O'Connell, Andrew Beatty

import mysql.connector

# Set up the connection with the database
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database="wsaa2"
)
# delete the student
mycursor = mydb.cursor()
sql = "DELETE FROM student where id = %s"
values = (1,)
mycursor.execute(sql, values)

# Commit the change
mydb.commit()
print("Deleted")

# Close the cursor, close the connector to free up the connection.
# They should time out after an hour anyway.
mycursor.close()
mydb.close()
