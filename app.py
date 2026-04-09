from flask import Flask, render_template_string
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Real-time Chat</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.0.1/socket.io.js"></script>
</head>
<body>
    <h2>GS chat</h2>
    <div id="chat" style="border:1px solid #ccc; height:200px; overflow-y:scroll;"></div>
    <input type="text" id="msg" placeholder="Namak">
    <button onclick="send()">Uxxarkel</button>

    <script>
        var socket = io();
        socket.on('new_message', function(data) {
            var p = document.createElement('p');
            p.innerHTML = "<b>Hyur:</b> " + data.msg;
            document.getElementById('chat').appendChild(p);
        });

        function send() {
            var input = document.getElementById('msg');
            socket.emit('send_message', {msg: input.value});
            input.value = '';
        }
    </script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML)

@socketio.on('send_message')
def handle_message(data):
    emit('new_message', data, broadcast=True)

if __name__ == "__main__":
    socketio.run(app, host="192.168.1.21", port=80)