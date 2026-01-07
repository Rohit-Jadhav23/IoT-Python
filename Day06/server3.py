from flask import Flask

server = Flask(__name__)

@server.get('/temperatures')
def get_temperatures():
    temperatures = [34.2, 30, 32.7, 37.2, 31.2]

    return f"Temperatures : {temperatures}\n"

@server.post('/temperatures/<float:temp>')
def receive_temperature(temp):
    print(f"Recieved Temp : {temp}")

    return f"{temp} temperature is recieved\n"

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=4000, debug=True)