# To run, it will tell you it is running on something like http://127.0.0.1:5000
# Just copy and paste that into a browser tab - you should get "Hello World" back

#TODO XXXX

from flask import Flask

# Create a flask app with the name of this file.
# When you run it you will see "Serving Flask app 'a_server'" or whatever you called the file.
app = Flask(__name__)

# map the app to a URL - so if someone does a request to / you run a function called index.
@app.route('/')

# the function returns Hello World for app route /
def index():
    return "Hello World"

# map the app to a URL - so if someone does a request to / you run a function called index.
@app.route('/blah')

# the function returns Blah to you too for app route /blah
# and this gets printed: 127.0.0.1 - - [04/Mar/2024 11:49:18] "GET /blah HTTP/1.1" 200 -
def blah():
    return "Blah to you too"


#run Flask
if __name__ == '__main__':
    app.run(debug=True)
