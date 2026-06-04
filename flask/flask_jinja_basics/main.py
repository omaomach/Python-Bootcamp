from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    marks = {
        "John": 45,
        "Saurabh": 99,
        "Mark": 55,
        "Jeff": 88,
        "Omao": 77,
        "Joel": 99
    }
    return render_template("index.html", marks=marks)

app.run(debug=True)