from flask import Flask, request, jsonify
import json
import sqlite3

response = ''
app = Flask(__name__)

@app.route('/api', methods=['GET','POST'])
def location():
    global response
    
    if(request.method == 'POST'):
        request_data = request.data
        request_data = json.loads(request_data.decode('utf-8'))
        lat = request_data['latitude']
        response = f'lat:{lat}'
        return " "

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)