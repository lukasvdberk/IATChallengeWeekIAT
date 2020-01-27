from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify

app = Flask(__name__)


@app.route('/change_direction', methods=['POST'])
def change_direction():
    # Endpoint for chaning direction
    direction_data = request.get_json()
    print(direction_data['direction'])

    response = ''
    if direction_data['direction'] == 'left':
        response = "left"
    if direction_data['direction'] == 'right':
        response = "right"

    return jsonify({"direction": response})


@app.route('/')
def hello_world():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0')
