from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField,FileField
from wtforms.validators import Required

# class UpdateProfile(FlaskForm):
#     bio = TextAreaField('Tell us about you.',validators = [Required()])
#     submit = SubmitField('Submit')

# class NewPost(FlaskForm):
#   title = StringField("Post Title", validators = [Required()])
#   post = TextAreaField("Description", validators = [Required()])  
  
#   submit=SubmitField("Add Post")

# class NewComment(FlaskForm):
#   comment = TextAreaField("Comment", validators=[Required()])
#   submit = SubmitField('Comment')

# class UpdatePost(FlaskForm):
#     description = TextAreaField('Tell us about you.',validators = [Required()])
#     submit = SubmitField('Submit')


        #### I've left these here in case you need to refer to them on how to add forms.