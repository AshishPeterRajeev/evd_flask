from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/api/location', methods=['GET','POST'])
def add_location():
    latitude = request.form['latitude']
    longitude = request.form['longitude']
    device_id = request.form['device_id']

    conn = sqlite3.connect('locations.db')
    c = conn.cursor()
    c.execute('INSERT INTO locations (latitude, longitude, device_id) VALUES (?, ?, ?)',
              (latitude, longitude, device_id))
    conn.commit()
    conn.close()

    return 'Location added successfully!'

@app.route('/',methods=['GET'])
def hello():
    return jsonify('hello world')
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)