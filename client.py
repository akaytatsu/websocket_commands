import socketio
import os
sio = socketio.Client()

@sio.event
def connect():
    print('connection established')

@sio.event
def my_message(data):

    print(f"command: " + data.get('command'))

    os.system(data.get('command'))

@sio.event
def disconnect():
    print('disconnected from server')

sio.connect('http://localhost:5050')
sio.wait()