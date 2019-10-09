import socketio

# standard Python
sio = socketio.Client()
sio.connect('http://localhost:5000', namespaces=['/chat'])
print('my sid is', sio.sid)


@sio.on('chat_message', namespace='/chat')
def on_message(sid, data):
    print("message ", data)

@sio.on('connect', namespace='/chat')
def connect():
    print("I'm connected to the /chat namespace!")

@sio.event
def disconnect():
    print("I'm disconnected!")
