# import Flask
from flask import Flask

# create instance of Flask
server = Flask(__name__)

@server.get('/')
def homepage():
    return "This is an IoT Application"

@server.get('/welcome')
def welcome():
    return "This is welcome page"

# run flask server
if __name__ == '__main__':
    server.run(host='0.0.0.0', port=4000, debug=True)