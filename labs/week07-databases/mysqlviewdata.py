# Lab07.02 exercise 4 - mysqlviewdata.py
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
# add the student
mycursor = mydb.cursor()
sql = "SELECT * FROM student"
mycursor.execute(sql)
#sql = "SELECT * FROM student where id = %s"
#values = (1,)
#mycursor.execute(sql, values)
result = mycursor.fetchall()

# print all the rows fetched
for row in result:
    print(row)

# Close the cursor, close the connector to free up the connection.
# They should time out after an hour anyway.
mycursor.close()
mydb.close()
