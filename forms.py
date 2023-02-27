from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, IntegerField, BooleanField,
                     RadioField)
from wtforms.validators import InputRequired, Length
import json
 
class CourseForm(FlaskForm):
   titll = StringField('Введи текст', validators=[InputRequired(),
                                             Length(max=64)])