from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    raise Exception("Ooops!")
    return "<p>Hello, World!</p>"