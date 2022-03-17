from flask import Flask

app = Flask(__name__)

@app.route("/")
def landing():
    return "<h1>It works!</p>"