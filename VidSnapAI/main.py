from enum import unique
from flask import Flask, render_template, request
import uuid
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = 'VidSnapAI/user_uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create", methods=["GET", "POST"])
def create():
    myid = uuid.uuid1()
    if request.method == "POST":
        print(request.files.keys())
        unique_id = request.form.get("uuid")
        description = request.form.get("text")
        for key, value in request.files.items():
            print(key, value)
            #Upload the file
            file = request.files[key]
            if file:
                filename = secure_filename(file.filename)
                # Combined these steps to safely handle existing directories
                target_dir = os.path.join(app.config['UPLOAD_FOLDER'], str(unique_id))
                os.makedirs(target_dir, exist_ok=True)
                file.save(os.path.join(target_dir, filename))
            # Capture the description and save it to a file
            with open(os.path.join(target_dir, "description.txt"), "w") as f:
                f.write(description)

    return render_template("create.html", myid=myid)

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

app.run(debug=True)