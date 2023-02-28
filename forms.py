from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired, Length


class CourseForm(FlaskForm):
    titll = StringField("Введи текст", validators=[InputRequired(), Length(max=64)])
