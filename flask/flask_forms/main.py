from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def hello():
    print(request.method)
    print(request.form)
    if(request.method == "POST"):
        with open("file.txt", "w") as f:
            f.write(f"The name is {request.form['name']} and email is {request.form['email']}")
        return render_template("index.html")

@app.route("/contact")
def services():
    return render_template("contact.html")

app.run(debug=True)