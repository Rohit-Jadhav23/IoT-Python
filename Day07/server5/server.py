from flask import Flask, request
from utils.database import execute_query
from utils.database import execute_select_query
from utils.response1 import create_response

app = Flask(__name__)

@app.route('/temperature', methods=['POST', 'GET', 'DELETE'])
def temperature():
    if request.method == 'GET':
        query = "select * from sensorsData where type = 'LM35';"

        temps = execute_select_query(query)

        return create_response(temps)

    elif request.method == 'POST':
        type = "LM35"
        location = request.get_json().get('location')
        value = request.get_json().get('value')

        query = f"insert into sensorsData(type, location, value) values('{type}', '{location}', {value});"

        execute_query(query=query)

        return create_response("Temperature is inserted successfully")
    
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        return create_response("Error in delete", error=True)

@app.route('/ldr', methods=['POST', 'GET'])
def ldr():
    if request.method == 'GET':
        query = "select * from sensorsData where type = 'LDR';"

        temps = execute_select_query(query)

        return create_response(temps)

    elif request.method == 'POST':
        type = "LDR"
        location = request.get_json().get('location')
        value = request.get_json().get('value')

        query = f"insert into sensorsData(type, location, value) values('{type}', '{location}', {value});"

        execute_query(query=query)

        return create_response("Temperature is inserted successfully")
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)