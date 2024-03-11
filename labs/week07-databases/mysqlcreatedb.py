# Lab07.02 exercise 1 - mysqlcreatedb.py
# Create a database using a python script
# Author(s): David O'Connell, Andrew Beatty

import mysql.connector

# Set up the connection with the database
connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = ""
)
# It is a connection object
print(connection)

# cursor stores the responses
mycursor = connection.cursor()
mycursor.execute("CREATE DATABASE wsaa2")

print(mycursor)

# Close the connector, free up the connection. They should time out after an hour.
# Close the cursor first.
mycursor.close()
connection.close()
