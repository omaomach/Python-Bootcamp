from flask import Flask, render_template

app = Flask(__name__) # We create an instance of the Flask class.

@app.route("/") # We then use the route decorate to tell Flask what URL should trigger our function
def hello_world():# This function then returns the message we want to display in the user's browser. The default content type is HTML, so HTML in the string will be rendered by the browser.
    return render_template("index.html") # turns index.html template file into HTML sent to the browser: 

app.run(debug=True)