# irish trains.py
# File to try out Andrew's code for parsing the employee XML file
# and printing the first name from each employee element
# author: David O'Connell

# parse() function reads the XML file and returns an ElementTree object. We then
# get the root element of the XML document using the getroot() method. Finally, we
# iterate over each child element in the root of the XML file and print the tag and
# attributes. This is a simple and effective way to parse XML files in Python.

from xml.dom.minidom import parse, parseString

import requests

page = requests.get("http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML")
print(page)
print("------------")
print(page.content)
doc = parseString(page.content)
print(doc.toprettyxml(newl=''), end='')
employeeNodeList = doc.getElementsByTagName("")


'''
filename = "employees.xml"

# read file 
doc = parse(filename)

print(doc.toprettyxml(newl=''), end='')

employeeNodeList = doc.getElementsByTagName("Employee")
print(len(employeeNodeList))
for employeeNode in employeeNodeList:
    firstNameNode = employeeNode.getElementsByTagName("FirstName").item(0)
    firstName = firstNameNode.firstChild.nodeValue.strip()
    print(firstName)
'''