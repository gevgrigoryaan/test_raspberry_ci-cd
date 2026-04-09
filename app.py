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
    <div id="chat" style="border:1px solid #ccc; height:200px; overflow-y:scroll; margin-bottom: 10px; padding: 5px;"></div>
    
    <input type="text" id="username" placeholder="Anun (Name)" style="width: 100px;">
    <input type="text" id="msg" placeholder="Namak (Message)" style="width: 250px;">
    <button onclick="send()">Uxxarkel</button>

    <script>
        var socket = io();
        
        socket.on('new_message', function(data) {
            var p = document.createElement('p');
            
            // If the user didn't type a name, default to "Hyur"
            var sender = data.username.trim() !== "" ? data.username : "Hyur";
            
            p.innerHTML = "<b>" + sender + ":</b> " + data.msg;
            document.getElementById('chat').appendChild(p);
            
            // Auto-scroll to the bottom when a new message appears
            var chatDiv = document.getElementById('chat');
            chatDiv.scrollTop = chatDiv.scrollHeight;
        });

        function send() {
            var user_input = document.getElementById('username');
            var msg_input = document.getElementById('msg');
            
            // Only send if the message isn't empty
            if (msg_input.value.trim() !== "") {
                socket.emit('send_message', {
                    username: user_input.value, 
                    msg: msg_input.value
                });
                // Clear the message input, but keep the username filled in
                msg_input.value = '';
            }
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
    # The 'data' dictionary now contains both 'username' and 'msg'
    emit('new_message', data, broadcast=True)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=8000)
