# To run, it will tell you it is running on something like http://127.0.0.1:5000
# Just copy and paste that into a browser tab - you should get "Hello World" back

from flask import Flask, url_for, redirect

# Create a flask app with the name of this file.
# When you run it you will see "Serving Flask app 'firstflask'" or whatever you called the file.
app = Flask(__name__, static_url_path='', static_folder='staticpages')

# Map URL endpoint to function. Below maps / to a function called index which returns "Hi there"
@app.route('/')
def index():
    return "<h1>Hi there</h1>"

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
    print(f"Using URL {url_for('index')}")
    return redirect(url_for('index'))

# Accept an int in the URL and return the square
@app.route('/square/<int:num>', methods=['GET'])
def sq(num):
    return f"The square of {num} is {num**2}"

#print(url_for(index))

#run Flask
    
if __name__ == '__main__':
    app.run(debug=True)
