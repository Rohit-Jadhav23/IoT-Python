from flask import Flask, request
from utils.database import execute_query
from utils.database import execute_select_query

app = Flask(__name__)

@app.route('/ldr', methods=['POST'])
def insert_value():
    type = 'LDR'
    location = request.get_json().get('location')
    value = request.get_json().get('value')

    query = f"insert into sensorsData(type, location, value) values('{type}', '{location}', {value});"

    execute_query(query)
    # publish
    return "value inserted successfully"

@app.route('/ldr', methods=['GET'])
def get_values():
    query = "select * from sensorsData where type = 'LDR';"

    return execute_select_query(query)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)