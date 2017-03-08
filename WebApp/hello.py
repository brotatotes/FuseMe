from flask import Flask, request, redirect, url_for
from flask import render_template
from werkzeug import secure_filename
import os

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join('static', secure_filename(f.filename)))
	return render_template('test.html')    

@app.route("/playback", methods=['GET', 'POST'])
def playback():
	return render_template('playback.html')   


if __name__ == "__main__":
    app.run()