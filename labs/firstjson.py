import json

data = {
    "students" : [
    {'name' : 'Joe', 'age' : 21, "student" : True},
    {'name' : 'Anna', 'age' : 23, "student" : False},
    ]
}

print(data)

# file = open("simple.json",'w') # not good syntax
with open("simple.json",'w') as file:
    json.dump(data, file, indent=4)
json_string = json.dumps(data)
print(f"string is {json_string}")