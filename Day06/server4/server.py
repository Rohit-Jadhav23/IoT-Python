from flask import Flask, request
from utils.database import execute_query
from utils.database import execute_select_query

app = Flask(__name__)

@app.route('/person', methods=['POST'])
def insert_person():
    # extract data from request form
    uid = request.form.get('uid')
    name = request.form.get('name')
    age = request.form.get('age')
    address = request.form.get('address')
    mobile = request.form.get('mobile')

    # create a query
    query = f"insert into persons values({uid}, '{name}', {age}, '{address}', '{mobile}');"

    # execute a query
    execute_query(query)

    # return response
    return f"person with uid = {uid} is inserted successfully\n"

@app.route('/person', methods=['GET'])
def get_persons():
    # create a select query
    query = "select * from persons;"

    # execute the query
    persons = execute_select_query(query=query)

    # return persons list into response
    return persons

@app.route('/person', methods=['PUT'])
def update_person():
    uid = request.form.get('uid')
    address = request.form.get('address')

    query = f"update persons SET address = '{address}' where uid = {uid};"

    execute_query(query)

    return f"address of person with uid = {uid} is updated successfully"

@app.route('/person', methods=['DELETE'])
def delete_person():
    uid = request.form.get('uid')

    query = f"delete from persons where uid = {uid};"

    execute_query(query)

    return f"person with uid {uid} is deleted successfully"

if __name__ == '__main__':
    app.run(debug=True)