from socketIO_client import SocketIO, LoggingNamespace
from threading import Thread
import time

def listen_for_data():
    def on_new_data(data):
        print('New data received:', data)

    with SocketIO('https://flask-gps-evd.onrender.com', params={'namespace': '/api/location'}) as socketIO:
        socketIO.on('new data', on_new_data, namespace='/api/location')
        socketIO.wait()

# Start a separate thread to listen for data
thread = Thread(target=listen_for_data)
thread.start()

# Main thread can perform other tasks while listening for data
while True:
    print('Main thread is still running')
    time.sleep(1)
