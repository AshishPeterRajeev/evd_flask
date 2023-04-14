from flask import Flask, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')

@app.route('/location', methods=['POST'])
def process_location():
    data = request.get_json()
    # Process the data
    processed_data = {'status': 'ok'}
    # Emit the processed data to the socket
    socketio.emit('new data', data)
    return 'Data received and processed'

if __name__ == '__main__':
    socketio.run(app)
