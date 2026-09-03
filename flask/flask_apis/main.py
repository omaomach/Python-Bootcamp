from pickle import TRUE
from flask import Flask, jsonify, request

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

@app.route("/students")
def get_students():
    students = [{"name": name, "marks": mark} for name, mark in marks.items()]
    return jsonify(students), 200

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

@app.route("/students", methods=["POST"])
def add_student():
    data = request.get_json(silent=True)

    if data is None:
        return jsonify({
            "error": "Request body must be a valid JSON"
        }), 400
    if "name" not in data or "marks" not in data:
        return jsonify({
            "error": "Both 'name' and 'marks' are required"
        }), 400
    if not isinstance(data["marks"], int):
        return jsonify({
            "error": "'marks' must be a number"
        }), 400
    
    name = data["name"]
    mark = data["marks"]

    marks[name] = mark
    
    return jsonify({
        "name": name,
        "marks": mark
    }), 201


@app.route("/students/<name>", methods=["PUT"])
def update_student(name):
    if name not in marks:
        return jsonify({
            "error": f"No student named '{name}'"
        }), 404
    
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({
            "error": "Request body must be a valid JSON"
        }), 400
    if "marks" not in data:
        return jsonify({
            "error": "'marks' is required"
        }), 400
    if not isinstance(data[marks], int):
        return jsonify({
            "error": "'marks' must be an number"
        }), 400
    
    marks[name] = data["marks"]

    return jsonify({
        "name": name,
        "marks": marks[name]
    }), 200


@app.route("/students/<name>", methods=["DELETE"])
def delete_student(name):
    if name not in marks:
        return jsonify({
            "error": "No student named '{name}'"
        }), 404
    
    del marks(name)

    return jsonify({
        "message": f"Delete '{name}'"
    }), 200

app.run(debug=True)