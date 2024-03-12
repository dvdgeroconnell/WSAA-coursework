
from studentDAO import studentDAO

# create a student
latestid = studentDAO.create(('Anne', 25))

# find that student
result = studentDAO.findByID(latestid)
print(result)

# update that student
studentDAO.update(('Rob',21,latestid))
result = studentDAO.findByID(latestid)
print(result)

#get all
result = studentDAO.getAll()
print("**************")
for x in result:
    print(x)
print("**************")

# delete that student
studentDAO.delete(latestid)

# get all
result = studentDAO.getAll()
for x in result:
    print(x)