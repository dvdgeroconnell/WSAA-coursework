# To run, it will tell you it is running on something like http://127.0.0.1:5000

from flask import Flask, request, url_for, redirect, jsonify, abort

# Create a flask app with the name of this file.
# When you run it you will see "Serving Flask app "the name of the file".
app = Flask(__name__)

# Map URL endpoint to function. Below maps / to a function called index which returns the string
@app.route('/')
def index():
    return "Hi from c_server"

# the URL would be http://127.0.0.1:5000/inquery?name=dave
@app.route('/inquery')
def inquery():
    name=request.args["name"]
    return name

# the URL would be http://127.0.0.1:5000/inquery2?name=dave&age=21&car=Nissan
@app.route('/inquery2')
def inquery2():
    # the args are returned as a dict object sorted alphabetically
    print(type(request.args))
    return request.args

# You mostly don't send data up in a GET request - you can do it in the body of the message.
# Accept a POST command, return 'Creating a user'
@app.route('/inbody', methods=['POST'])
def inbody():
    # assume json. Set the body to be raw json in Postman - {"name":"dave"}
    name = request.json["name"]
    print (request.url)
    return f"you are {name}"

# returning JSON
@app.route('/user')
def getuser():
    # create dict object (single quotes)
    user = {
        'name' : 'Dave',
        'age'  : 21
    }
    return jsonify(user)

# aborts and sends error code 401 back to the user
@app.route('/login')
def login():
    abort(401)
    return

'''
# You can set the methods that get mapped to the URL, e.g.
# @app.route('/user',methods=['GET','POST']))

# Do a GET, Postman returns 'Getting all users'
@app.route('/users', methods=['GET'])
def get_users():
    return "Getting all users"

# Prints the username it was passed in the URL, i.e. http://127.0.0.1:5000/users/dave
# would print "Hello dave"

@app.route('/users/<username>', methods=['GET'])
def get_user_byname(username):
    return f"Hello {username}"

#  Accept an int in the URL (as an ID) instead of a string
@app.route('/users/<int:id>', methods=['GET'])
def get_user_byid(id):
    return f"Your ID is {id}"

# Accept a POST command, return 'Creating a user'
@app.route('/users', methods=['POST'])
def create_users():
    return "Creating a user"

# Accept a PUT command, return 'Update a user'
@app.route('/users', methods=['PUT'])
def update_users():
    return "Update a user"

# Testing redirect, url_for
@app.route('/invalid', methods=['GET'])
def testing_redirect():
    return redirect(url_for('index'))

# Accept an int in the URL and return the square
@app.route('/square/<int:num>', methods=['GET'])
def sq(num):
    return f"The square of {num} is {num**2}"

#print(url_for(index))
'''

#run Flask
    
if __name__ == '__main__':
    app.run(debug=True)
