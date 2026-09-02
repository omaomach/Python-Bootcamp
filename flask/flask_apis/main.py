from flask import Flask, jsonify

app = Flask(__name__)

marks = {
    "Joash": 100,
    "Joel": 63,
    "Faith": 37,
    "Gloria": 73,
    "Joshua": 48
}

@app.route("/")
def get_marks():
    values = [1, marks, 77]
    return jsonify(values)

@app.route("/students/<name>")
def get_student(name):
    if name not in marks:
        return jsonify({
            "error": f"No student named '{name}'"
        }), 404
    return jsonify({
        "name": name,
        "marks": marks[name]
    }), 200

app.run(debug=True)