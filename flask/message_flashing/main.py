from flask import Flask, flash, render_template, redirect

app = Flask(__name__)

app.secret_key = "sdgofgrwugrougq3g4oyqgw4o8g23"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/logout")
def logout():
    flash("Get out bruh!", "success")
    return render_template("logout.html")

app.run(debug=True)