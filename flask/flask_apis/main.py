from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def json():
    marks = {
    "Joash": 36,
    "Joel": 63,
    "Faith": 37,
    "Gloria": 73,
    "Joshua": 48
    }
    values = [1, marks, 77]
    return jsonify(values)

app.run(debug=True)