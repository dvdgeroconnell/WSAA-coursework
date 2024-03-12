import mysql.connector

class StudentDAO:
    host =""
    user = ""
    password =""
    database =""
    connection = ""
    cursor =""

    def __init__(self):
        #these should be read from a config file
        self.host="localhost"
        self.user="root"
        self.password=""
        self.database="wsaa2"
    
    def getCursor(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()
        return self.cursor
        
    def closeAll(self):
        self.connection.close()
        self.cursor.close()

    def create(self, values):
        cursor = self.getCursor()
        sql="insert into student (name, age) values (%s,%s)"
        cursor.execute(sql, values)

        self.connection.commit()
        newid = cursor.lastrowid
        self.closeAll()
        return newid
    
    def getAll(self):
        # select all members of student table
        mycursor = self.getCursor()
        sql = "SELECT * FROM student"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        return result
        
    def findByID(self, id):
        mycursor = self.getCursor()
        sql = "SELECT * FROM student where id = %s"
        values = (id,)
        mycursor.execute(sql, values)
        result = mycursor.fetchone()
        self.closeAll()
        return result
        
    def update(self, values):
        # update the student
        mycursor = self.getCursor()
        sql = "UPDATE student SET name = %s, age = %s where id = %s"
        #values = ("Daniel", 33, 1)
        mycursor.execute(sql, values)
        # Commit the change
        self.connection.commit()
        self.closeAll()
        return
        
    def delete(self, id):
        # call the getCursor() method
        mycursor = self.getCursor()
        sql="DELETE FROM student where id = %s"
        values = (id,)
        mycursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        return

studentDAO = StudentDAO()