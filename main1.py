from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename

a = Flask(__name__)
@a.route("/")
def index():
    return render_template("index.html")
@a.route("/uploader",methods = ["POST"])
def upload():
    if request.method == "POST":
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath, 'static', 'uploads', secure_filename(f.filename))
        f.save(file_path)
        predictions = "any"
        pred_strings = []
        for _, pred_class, pred_prob in predictions:
            pred_strings.append(str(pred_class).strip() + " : " + str(round(pred_prob, 5)).strip())
        preds = ", ".join(pred_strings)
        print("preds:::", preds)
    return render_template("upload.html", predictions=preds, display_image=f.filename)
if __name__ == "__main__":
    a.run(debug=True)


