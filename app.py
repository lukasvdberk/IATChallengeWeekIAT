from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from module.move_kart import *
from main import Rijden
import threading
from flask_socketio import SocketIO, emit

app = Flask(__name__)
rijd = Rijden()
app.config['SECRET_KEY'] = 'ASDJFLKSDA'
socketio = SocketIO(app)

thread = None


@app.route('/start')
def start():
    global thread
    if thread is None:
        thread = threading.Thread(target=rijd.run,)
        thread.start()
    return jsonify({})


@app.route('/push_hit', methods=['POST'])
def push_hit():
    socketio.emit('on_hit', {"start": True}, broadcast=True)
    return jsonify({})


@app.route('/push_start', methods=['POST'])
def push_start():
    socketio.emit('on_start', {"start": True}, broadcast=True)
    return jsonify({})


@app.route('/push_end', methods=['POST'])
def push_end():
    socketio.emit('on_game_over', {"end": True}, broadcast=True)
    return jsonify({})


is_dead = False


@app.route('/push_death', methods=['POST'])
def push_death():
    global is_dead

    if not is_dead:
        socketio.emit('on_death', {"death": True}, broadcast=True)
        is_dead = True
    return jsonify({})


@app.route('/change_direction', methods=['POST'])
def change_direction():
    global rijd
    # Endpoint for chaning direction
    direction_data = request.get_json()
    print(direction_data['direction'])

    if direction_data['direction'] == 'left':
        rijd.directions.append("right")
    if direction_data['direction'] == 'right':
        rijd.directions.append("left")

    return jsonify({"direction": direction_data})


@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


@app.route('/')
def hello_world():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    # socketio.run(app)
