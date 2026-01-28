from flask import Flask, render_template, request
from config import DevelopmentConfig
from pan_detector import detect_tampering
import os

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

# Make sure upload folder exists
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["GET", "POST"])
def index():
    score = None
    if request.method == "POST":
        file = request.files.get("pan")
        if file and allowed_file(file.filename):
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filepath)

            # Call your ML function
            score = detect_tampering("static/original.png", filepath)
        else:
            score = "Invalid file type"

    return render_template("index.html", score=score)

if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"])
