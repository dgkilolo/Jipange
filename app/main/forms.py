from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField,FileField
from wtforms.validators import Required
from . import main

class DiaryForm(FlaskForm):
    title = StringField("What are you writing about today?", validators=[Required()])
    description = TextAreaField("Write away ...", validators= [Required()])
    submit = SubmitField("Submit Entry")


class ShoppingForm(FlaskForm):
   title = StringField("Category", validators = [Required()])
   message = TextAreaField("Items", validators = [Required()])  
  
   submit=SubmitField("Add Shopping")

class NewComment(FlaskForm):
   comment = TextAreaField("Comment", validators=[Required()])
   submit = SubmitField('Comment')

class UpdatePost(FlaskForm):
   description = TextAreaField('Tell us about you.',validators = [Required()])
   submit = SubmitField('Submit')

class UpdateDiary(FlaskForm):
    title = StringField("Update title")
    description = TextAreaField("Change post")
    submit = SubmitField("Update post")

