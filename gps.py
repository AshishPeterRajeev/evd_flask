from pymongo import MongoClient
import pymongo, json
import requests
import time

import math

def distance(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude to radians
    rlat1, rlon1, rlat2, rlon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    
    # Haversine formula
    dlat = rlat2 - rlat1
    dlon = rlon2 - rlon1
    a = math.sin(dlat/2)**2 + math.cos(rlat1) * math.cos(rlat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2( math.sqrt(a), math.sqrt(1 - a) )
    # c = 2*math.asin(math.sqrt(a))
    r = 6371 # Radius of the earth in km
    return c * r * 1000 # Convert to meters

def calculate_bearing(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude to radians
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # Calculate the bearing using the Haversine formula
    dlon = lon2 - lon1
    y = math.sin(dlon) * math.cos(lat2)
    x = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(dlon)
    bearing = math.atan2(y, x)
    bearing = math.degrees(bearing)
    bearing = (bearing + 360) % 360  # Convert bearing to 0-360 degrees
    return bearing

# Fixed coordinate of the traffic light system
# fixed_lat = 51.5074
# fixed_lon = 0.1278
fixed_lat = 9.4300800
fixed_lon = 76.5939460

# Radius around the fixed coordinate
radius = 500 # meters
# uri = "mongodb+srv://codehubash:serverpass16@cluster0.ptyboko.mongodb.net/?retryWrites=true&w=majority"
# client = MongoClient(uri)
# db = client["locationdb"]
# collection = db["coordinates"]

# # Get the latest added document
# latest_doc = collection.find_one(sort=[("_id", -1)])
# print(type(latest_doc),latest_doc)

# GPS coordinates of the vehicle
previousLatitude = 0.0
previousLongitude = 0.0

while True:
#     # Replace "http://localhost:5000/data" with the URL of your Flask route
    response = requests.get("https://flask-gps-evd.onrender.com/data")
    json_data = response.json()
    lat = json_data["latitude"]
    lon = json_data["longitude"]
    
    if( previousLatitude!=lat or previousLongitude!=lon):
        print(lat, lon)
        previousLatitude = lat
        previousLongitude = lon
    
    time.sleep(1)

# lat = 9.4300800
# lon = 76.5939460

# lat = 9.430295034352834
# lon = 76.5983158941853

#     lat = float(latest_doc["latitude"])
#     lon = float(latest_doc["longitude"])
    print(lat,lon)
    # Calculate the distance between the vehicle and the fixed coordinate
    dist = round(distance(lat, lon, fixed_lat, fixed_lon),3)
    bearing = calculate_bearing(fixed_lat, fixed_lon, lat, lon)
    print(dist,bearing)

    # Check if the distance is less than or equal to the radius
    if dist <= radius:
        print("Vehicle has entered the area")
    else:
        print("Vehicle is outside the area")

    if bearing > 315 or bearing < 45 :
        print("Lane 1 - North")
    elif bearing > 45 and bearing < 135 :
        print("Lane 2 - East")
    elif bearing > 135 and bearing < 225 :
        print("Lane 3 - South")
    elif bearing > 225 and bearing < 315 :
        print("Lane 4 - West")