from flask import Flask, render_template, request
from utils.database import execute_select_query

server = Flask(__name__)

@server.route('/', methods=['GET'])
def homepage():
    return render_template("homepage.html")

@server.route('/welcome', methods=['GET'])
def welcome():
    # string = "IoT Application"
    query = "select * from sensorsData where type = 'LM35';"
    temps = execute_select_query(query)

    return render_template("welcome.html", message=temps)

@server.route('/temperatures', methods=['GET'])
def get_temperatures():
    query = "select value, location from sensorsData where type = 'LM35';"

    temps = execute_select_query(query=query)

    return render_template("table.html", message=temps)

@server.route('/temperature', methods=['GET','POST'])
def add_temperature():
    temp = request.form.get('temp')
    loc = request.form.get('loc')
    print(f"temp = {temp}, location = {loc}")

    return render_template('form.html')

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=4000, debug=True)