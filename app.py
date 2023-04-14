from flask import Flask, request, jsonify
import time

app = Flask(__name__)

data_dict = {}  # A dictionary to store the data received in POST requests

@app.route('/api/location', methods=['POST'])
def handle_data():
    # Retrieve the JSON data from the request
    data = request.get_json()

    # Update the data dictionary with the new data
    data_dict.update(data)

    # Return a response to the client
    return 'Data received'

# @app.route('/data', methods=['GET'])
# def get_data():
    
#     time.sleep(6)
#     # Return the data dictionary as JSON
#     return jsonify(data_dict)

@app.route('/',methods=['GET'])
def hello():
    return jsonify('hello world')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')