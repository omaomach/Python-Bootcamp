from flask import Flask, render_template, request
import uuid
from werkzeug.utils import secure_filename #sanitizes an uploaded file's name before you save it to disk
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'user_uploads')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)

# app.config is a dictionary Flask attaches to the app object, meant to hold app-wide settings. 
# A plain settings dict built into every Flask app. 
# You put values in by key, read them back by key, anywhere you have app
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Returns True only if the filename has an allowed image extension (case-insensitive)
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def home():
    return render_template("index.html")

# The function is registered for the "/create" URL, accepting both GET and POST. 
# GET shows the form; POST processes the submission
@app.route("/create", methods=["GET", "POST"]) 
def create():

    # Generates a fresh unique id -- uuid.uuid1() builds it from the machines identity
    # plus the current timestamp.
    # This runs on every request, GET and POST alike.
    myid = uuid.uuid1()

    # Everything indented under the if runs only when the form is submitted.
    # On a GET, all of it is skipped and the jumps to the final "return".
    if request.method == "POST":

        # "request.files" data source -- the uploaded files -- a dick like object mapping each
        # file input's name to its file
        # ".keys" lists those names to the terminal
        print(request.files.keys())

        # Reads the hidden field back
        # This is the "myid" from the GET render, returned via that hidden uuid field
        # ".get()" yields None if it's absent
        unique_id = request.form.get("uuid")

        # Reads the visible description field(named "text"). "None" if absent
        description = request.form.get("text", "")

        # Builds the destination folder path: the upload folder + the session id, joined with OS's separator -- (.../user_uploads/<uuid>)
        target_dir = os.path.join(app.config['UPLOAD_FOLDER'], str(unique_id))

        # Create the folder(and any missing parents)
        # exist_ok=True means "don't error if it's already there"
        os.makedirs(target_dir, exist_ok=True)

        # Loops over the uploaded files. "items()" hands you (field_name, file_object) pairs --
        # key is the input's name, file is the uploaded file itself
        for key, file in request.files.items():

            # Debug print of each file's name and object.
            print(key, file)

            if file and allowed_file(file.filename):

                # file.filename is the untrusted name from the user's machine;
                # secure_filename sanitizes it into a safe, flat name (the path-traversal protection)
                filename = secure_filename(file.filename)

                # Writes the uploaded file's bytes to disk at target_dir/filename
                # .save() is the file object's own method for storing itself
                file.save(os.path.join(target_dir, filename))

        # Opens description.txt in the target folder for writing and writes the description into it.
        with open(os.path.join(target_dir, "description.txt"), "w") as f:
            f.write(description)

    return render_template("create.html", myid=myid)

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

app.run(debug=True)