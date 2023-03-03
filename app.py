import hashlib

from flask import Flask, render_template, request
from forms import CourseForm
from pydantic_func import DataModel

app = Flask(__name__)
app.config["SECRET_KEY"] = "3787b2b3631f5e58b18cc7b9dfa5db08b3c8b2d2f1918172"


@app.route("/", methods=["GET", "POST"])
def form_hashed_message():
    form = CourseForm()
    if request.method == "POST":
        hashed_message = hashlib.md5(request.form.get("titll").encode()).hexdigest()
        return render_template("base.html", form=form, hashed_message=hashed_message)

    else:
        return render_template("base.html", form=form)


@app.route("/json", methods=["POST"])
def json_hashed_message():
    data = request.json
    data = DataModel(name=str(data["name"]))
    #    return result
    return data.name


@app.route("/name", methods=["GET"])
def name_message():
    #    data = request.json
    data = {
        "title": "Hi",
        "name": "Dasha",
        "age": 25,
        "city": "Narva",
    }

    return {"name": data["title"]}
