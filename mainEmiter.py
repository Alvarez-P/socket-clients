import socketio, time

# standard Python
sio = socketio.Client()
sio.connect('http://localhost:5000', namespaces=['/rpi'])
print('my sid is', sio.sid)


@sio.on('rpi_message', namespace='/rpi')
def message(sid, data):
    print(data)

@sio.on('connect', namespace='/rpi')
def connect():
    print("I'm connected to the /rpi namespace!")

@sio.event
def disconnect():
    print("I'm disconnected!")

while True:
    sio.emit('rpi message', {'data': 'hola'}, namespace='/rpi')
    time.sleep(2)