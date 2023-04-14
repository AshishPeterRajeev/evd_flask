import pymongo
import json
import requests
import time

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
json_data = json.dumps(data_list)
print(json_data)
# Return the JSON object

response = requests.get("https://flask-gps-evd.onrender.com/data")

# Print the status code of the response
print(response.status_code)

# Print the JSON data returned from the Flask route
print(response.json())
previousLatitude = 0.0
previousLongitude = 0.0

# Get the JSON data from the Flask route
json_data = response.json()

# latitude = json_data["latitude"]
# longitude = json_data["longitude"]

while True:
# Replace "http://localhost:5000/data" with the URL of your Flask route
    response = requests.get("https://flask-gps-evd.onrender.com/data")

    latitude = json_data["latitude"]
    longitude = json_data["longitude"]
    
    if( previousLatitude!=latitude or previousLongitude!=longitude):
        print(latitude, longitude)
        previousLatitude = latitude
        previousLongitude = longitude
    
    time.sleep(3)
        

    # Iterate over the list of dictionaries and extract the latitude and longitude values
    # for item in json_data:
    #     latitude = item["latitude"]
    #     longitude = item["longitude"]
    #     print(latitude, longitude)





