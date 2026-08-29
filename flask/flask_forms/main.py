from flask import Flask, render_template, request
import os
from dotenv import load_dotenv

load_dotenv()

### TO THE WRITTEN FILE SAVE IN "flask_forms" AND NOT ON THE MAIN WORKING DIRECTORY
# 1. "__file__" -- a variable Python fills with the path to this script
# 2. ".../flask_forms/main.py" -- tied to the file, not where the command was run.
# 3. "os.path.abspath(__file__)" -- expands it to a full absolute path.
# 4. "os.path.dirname(...)" -- chops the filename off, leaving the folder: ".../flask_forms"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def hello():
    print(request.method)
    print(request.form)
    if(request.method == "POST"):
        # 5. "os.path.join(BASE_DIR, "file.txt")" -- glues folder + filename with the correct separator for your OS
        file_path = os.path.join(BASE_DIR, "file.txt")
        with open(file_path, "w") as f:
            f.write(f"The name is {request.form['name']} and email is {request.form['email']}")
    return render_template("index.html")

@app.route("/contact")
def services():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=os.environ.get("FLASK_DEBUG") == "1")


# __name__ tells you how the file was run; __file__ tells you where the file is