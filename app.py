from flask import Flask
from markupsafe import escape
from flask import url_for
from flask import render_template
from flask import flash, redirect
from flask import request
from forms import CourseForm
import json
import hashlib

app = Flask(__name__)
app.config['SECRET_KEY'] = '3787b2b3631f5e58b18cc7b9dfa5db08b3c8b2d2f1918172'

@app.route('/', methods=['GET', 'POST'])
def form_hashed_message():
    form = CourseForm()
    if request.method == "POST":
        hashed_message = hashlib.md5(request.form.get('titll').encode()).hexdigest()
        return render_template('base.html',
                                form=form,
                                hashed_message=hashed_message)
    else: return render_template('base.html',
                                form=form)


@app.route('/json', methods=['GET'])
def json_hashed_message():
    hashed_message = 'Hi'
    return {
        'hashed_message' : hashed_message
    }