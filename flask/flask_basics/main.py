from flask import Flask, render_template
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__) # We create an instance of the Flask class.

@app.route("/") # We then use the route decorate to tell Flask what URL should trigger our function
def hello_world():# This function then returns the message we want to display in the user's browser. The default content type is HTML, so HTML in the string will be rendered by the browser.
    return render_template("index.html") # turns index.html template file into HTML sent to the browser: 

@app.route("/boom")
def boom():
    raise Exception("testing the debugger")

if __name__ == "__main__":
    # debug is off by default; set FLASK_DEBUG=1 locally to turn on auto-reload
    # and the in-browser debugger. Never enable it on a public server.
    app.run(debug=os.environ.get("FLASK_DEBUG") == "1")