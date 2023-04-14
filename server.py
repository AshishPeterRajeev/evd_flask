import requests

url = 'https://flask-gps-evd.onrender.com/api/location'

response = requests.get(url)

print(response.text)

if response.status_code == 200:
    print('Location received successfully')
else:
    print('Error receiving location')