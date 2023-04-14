from flask import Flask, request, jsonify
from pymongo import MongoClient
import pymongo,json
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

@app.route('/api/location', methods=['GET','POST'])
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

@app.route('/data',methods=['GET'])
def data():
    uri = "mongodb+srv://codehubash:serverpass16@cluster0.ptyboko.mongodb.net/?retryWrites=true&w=majority"

    client = pymongo.MongoClient(uri)

    coordinates = {}

    db = client['locationdb']
    collection = db['coordinates']


    # Query for items with latitude and longitude fields
    cursor = collection.find({"latitude": {"$exists": True}, "longitude": {"$exists": True}})

    # Create a list of dictionaries to hold the data
    data_list = []

    for item in cursor:
        data_dict = {}
        data_dict["_id"] = str(item["_id"])
        data_dict["latitude"] = item["latitude"]
        data_dict["longitude"] = item["longitude"]
        data_dict["device_id"] = item["device_id"]
        data_list.append(data_dict)

    # Convert the list of dictionaries to a JSON object
    # json_data = json.dumps(data_list)
    # print(json_data)
    return jsonify(data_list)
# Return the JSON object


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


