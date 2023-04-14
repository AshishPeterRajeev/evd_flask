from socketIO_client import SocketIO, LoggingNamespace

def on_new_data(data):
    print('New data received:', data)

with SocketIO('https://flask-gps-evd.onrender.com/api/location', LoggingNamespace) as socketIO:
    socketIO.on('new data', on_new_data)
    socketIO.wait()
