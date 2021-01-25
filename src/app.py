from flask import Flask, request, abort
from flask_socketio import SocketIO

from utils import Command

command_data = Command()

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret!"
socketio = SocketIO(app)


@app.route("/command")
def command():
    command = request.args.get("command")

    executor = command_data.find_command(command)

    if not executor:
        abort(404, description="Command not found")

    socketio.emit("my_message", {"command": executor})
    return ""


@socketio.on("disconnect")
def test_disconnect():
    print("Client disconnected")


if __name__ == "__main__":
    socketio.run(app)
