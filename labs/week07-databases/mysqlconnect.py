
import mysql.connector

# Set up the connection with the database
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "")

# It is a connection object
print(mydb)

# cursor stores the responses
mycursor = mydb.cursor()
mycursor.execute("USE wsaa")

print(type(mycursor))

for x in mycursor:
    print(x)

# Get one
newsql_one = "SELECT * FROM student WHERE id = %s;"
values = (1,)
mycursor.execute(newsql_one, values)

print(mycursor)
result = mycursor.fetchall()

# x is a tuple
for x in result:
    print(x)

# Get all - looks like you don't need the ';'
newsql_all = "SELECT * FROM student"
mycursor.execute(newsql_all)

print(mycursor)
result = mycursor.fetchall()

# x is a tuple
for x in result:
    print(x)

# If you do a Create, Update or Delete...
mydb.commit()

# Close the connector, free up the connection. They should time out after an hour.
# Close the cursor first.
mycursor.close()
mydb.close()