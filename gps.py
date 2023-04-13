import math

def distance(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude to radians
    rlat1, rlon1, rlat2, rlon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    
    # Haversine formula
    dlat = rlat2 - rlat1
    dlon = rlon2 - rlon1
    a = math.sin(dlat/2)**2 + math.cos(rlat1) * math.cos(rlat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    r = 6371 # Radius of the earth in km
    return c * r * 1000 # Convert to meters

# Fixed coordinate of the traffic light system
fixed_lat = 51.5074
fixed_lon = 0.1278

# Radius around the fixed coordinate
radius = 100 # meters

# GPS coordinates of the vehicle
lat = 51.5098
lon = -0.1180

# Calculate the distance between the vehicle and the fixed coordinate
dist = distance(lat, lon, fixed_lat, fixed_lon)

# Check if the distance is less than or equal to the radius
if dist <= radius:
    print("Vehicle has entered the area")
else:
    print("Vehicle is outside the area")
