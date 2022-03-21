from crypt import methods
from importlib.resources import path
from inspect import getfile
from flask import Flask, abort, redirect, send_file, send_from_directory, url_for
from flask import render_template
from flask import request
import Video_Fetch as vf

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def landing():
    if request.method == 'POST':
        print(request.form['URL'])
        path = vf.DownloadVideo(request.form['URL'])
        return send_file(path, as_attachment=True)
    return render_template('FileInput.html')
