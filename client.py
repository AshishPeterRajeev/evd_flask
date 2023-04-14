import pymongo
import json

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



