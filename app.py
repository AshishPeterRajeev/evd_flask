from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

uri = "mongodb+srv://codehubash:serverpass16@cluster0.ptyboko.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = None

# Send a ping to confirm a successful connection
def connect():
    global client
    client = MongoClient(uri)
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

connect()

@app.route('/',methods=['GET'])
def hello():
    return jsonify('hello world')

@app.route('/api/location', methods=['POST'])
def add_location():
    data = request.json
    latitude = data['latitude']
    longitude = data['longitude']
    device_id = data['device_id']

    db = client['locationdb']
    collection = db['coordinates']
    result = collection.insert_one({
        'latitude': latitude,
        'longitude': longitude,
        'device_id': device_id
    })

    return jsonify({'message': 'Location added successfully!'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
