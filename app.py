from crypt import methods
from importlib.resources import path
from flask import Flask, redirect, send_from_directory, url_for
from flask import render_template
from flask import request
import Video_Fetch as vf

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def landing():
    if request.method == 'POST':
        print(request.form['URL'])
        path = vf.DownloadVideo(request.form['URL'])
        return redirect(url_for('download', URL=request.form['URL'],path=path))
    return render_template('FileInput.html')

@app.route("/download")
def download():
    print(request.args.get('path'))
    send_from_directory(directory='Downloads/', path=request.args.get('path'))
    return render_template('download.html')