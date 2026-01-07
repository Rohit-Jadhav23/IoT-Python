#  import Flask class from flask module
from flask import Flask

# create instance/variable of Flask
server = Flask(__name__)        #   __main__

@server.get('/')   # decorator used to bind function with web/REST API
def homepage():
    return "This is Home page of Application"

@server.get('/login')
def login():
    return "This is a login page"


# run a flask server
server.run()


# URL - http://127.0.0.1:5000
