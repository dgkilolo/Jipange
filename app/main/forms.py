from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField,FileField
from wtforms.validators import Required

# class UpdateProfile(FlaskForm):
#     bio = TextAreaField('Tell us about you.',validators = [Required()])
#     submit = SubmitField('Submit')

class Shopping(FlaskForm):
   title = StringField("Shopping Title", validators = [Required()])
   post = TextAreaField("Description", validators = [Required()])  
  
   submit=SubmitField("Add Shopping")

class NewComment(FlaskForm):
   comment = TextAreaField("Comment", validators=[Required()])
   submit = SubmitField('Comment')

class UpdatePost(FlaskForm):
     description = TextAreaField('Tell us about you.',validators = [Required()])
     submit = SubmitField('Submit')


        