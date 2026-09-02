from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    name = request.args.get('name', 'Joash')
    token = request.args.get('tokens', 67000, type=int)
    return render_template("index.html", name=name, token=token)

app.run(debug=True)