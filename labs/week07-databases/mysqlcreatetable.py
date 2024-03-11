# Lab07.02 exercise 2 - mysqlcreatetable.py
# Create a database table using a python script
# Author(s): David O'Connell, Andrew Beatty

import mysql.connector

# Set up the connection with the database
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database="wsaa2"
)

# cursor stores the responses
mycursor = mydb.cursor()
sql = "CREATE TABLE student (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), age INT)"
mycursor.execute(sql)

# Close the connector, free up the connection. They should time out after an hour.
# Close the cursor first.
mycursor.close()
mydb.close()
