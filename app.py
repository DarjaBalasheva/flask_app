import hashlib

from flask import Flask, render_template, request

from forms import CourseForm

from pydantic_func import DataModel
from marsh import MarshModel
from marshmallow import ValidationError
from config import DefaultSetting

app = Flask(__name__)


app.config.from_object(DefaultSetting())


@app.route("/", methods=["GET", "POST"])
def form_hashed_message():
    form = CourseForm()
    if request.method == "POST":
        hashed_message = hashlib.md5(request.form.get("titll").encode()).hexdigest()
        return render_template("base.html", form=form, hashed_message=hashed_message)

    else:
        return render_template("base.html", form=form)


@app.route("/json", methods=["GET"])
def json_hashed_message():
    data = request.json
    data = DataModel(name=str(data["name"]))  # DataModel(**data)

    return data.name


@app.route("/name", methods=["POST"])
def name_message():
    data = request.get_json()
    schema = MarshModel()  # 401

    try:
        result = schema.load(data)
    except ValidationError as err:
        return {"errors": err.messages}, 401

    if result["type"] == "md5":
        return {"result_md5": hashlib.md5(result["name"].encode()).hexdigest()}
    else:
        return {"result_sha256": hashlib.sha256(result["name"].encode()).hexdigest()}


@app.route("/query")
def query_name_message():
    first_name = request.args["first_name"]
    last_name = request.args.get("last_name")

    return """<h1>The first name value is: {}</h1>
<h1>The last name value is: {}</h1>""".format(
        first_name, last_name
    )


@app.route("/query/type", methods=["POST"])
def query_hashed_message():
    type_message = request.args.get("type")

    if type_message == "md5":
        hashed_message = hashlib.md5(type_message.encode()).hexdigest()
        return {"hashed_message_md5": hashed_message}

    elif type_message == "sha256":
        hashed_message = hashlib.sha256(type_message.encode()).hexdigest()
        return {"hashed_message_sha256": hashed_message}

    else:
        return {"errors": "Недопустимый формат"}, 401
