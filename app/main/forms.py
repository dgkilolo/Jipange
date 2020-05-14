from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField,FileField
from wtforms.validators import Required
from . import main

class DiaryForm(FlaskForm):
    title = StringField("What are you writing about today?", validators=[Required()])
    description = TextAreaField("Write away ...", validators= [Required()])
    submit = SubmitField("Submit Entry")


class UpdateDiary(FlaskForm):
    title = StringField("Update title")
    description = TextAreaField("Change post")
    submit = SubmitField("Update post")