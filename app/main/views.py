from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User, Shopping, ToDoList, Diary
from flask_login import login_required, current_user
# from .forms import #UpdateProfile, NewPost, NewComment, UpdatePost    #### Import the forms that you create   
from .. import db,photos
from datetime import datetime
# import markdown2

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
   

    title = 'Jipange'

    return render_template('index.html', title = title)
    

@main.route('/home')
def home():
    '''
    View root page function that returns the home page.
    '''
    title = 'Blog'
    posts = Posts.query.all()
    # pitches = Pitch.query.filter_by(category = 'pun').all()
    # comment = Comment.query.filter_by(pitch_id = 1).all()
    
    return render_template('home.html', title = title, posts=posts)


# @main.route('/home/<int:postId>/deletePost',methods = ['GET','POST'])
# @login_required
# def delete_post(postId):
#   post = Posts.query.filter_by(id = postId).first()   
#   db.session.delete(post)
#   db.session.commit()
#   return redirect(url_for("main.home", postId=post.id))  
  


# @main.route('/home/<int:postId>/changePost',methods = ['GET','POST'])
# @login_required
# def update_posts(postId):
#   post = Posts.query.filter_by(id = postId).first()
#   if post is None:
#       abort(404)

#   form = UpdatePost()

#   if form.validate_on_submit():
#     post.description = form.description.data

#     db.session.add(post)
#     db.session.commit()

#     return redirect(url_for('.home'))

#   title = "Edit Post"
#   return render_template('updateForm.html',form=form, title=title)

# @main.route('/writer/<uname>')
# def profile(uname):
#   writer = Writer.query.filter_by(username = uname).first()

#   if writer is None:
#       abort(404)
#   title = "Profile"
#   return render_template("profile/profile.html", writer=writer, title=title)


# @main.route('/writer/<uname>/update',methods = ['GET','POST'])
# @login_required
# def update_profile(uname):
#     writer = Writer.query.filter_by(username = uname).first()
#     if writer is None:
#         abort(404)

#     form = UpdateProfile()

#     if form.validate_on_submit():
#         writer.bio = form.bio.data

#         db.session.add(writer)
#         db.session.commit()

#         return redirect(url_for('.profile',uname=writer.username))

#     return render_template('profile/update.html',form =form)





# @main.route('/writer/<uname>/update/pic',methods= ['POST'])
# @login_required
# def update_pic(uname):
#     writer = Writer.query.filter_by(username = uname).first()
#     if 'photo' in request.files:
#         filename = photos.save(request.files['photo'])
#         path = f'photos/{filename}'
#         writer.profile_pic_path = path
#         db.session.commit()
#     return redirect(url_for('.profile',uname=uname))



# @main.route('/post', methods = ['GET','POST'])
# @login_required
# def add_pitch():
  
#   form = NewPost()
#   if form.validate_on_submit():
#     title = form.title.data
#     post = form.post.data  
    
#     # Updated post instance
#     new_post = Posts(title=title,description=post)

#     # Save post method
#     new_post.save_post()
#     return redirect(url_for('.home'))

#   title = 'New post'
#   return render_template('newpost.html',title = title,pitch_form=form )




# @main.route('/<int:postId>/comment',methods=['GET','POST'])
# def post_comment(postId):
# #   user = User.query.filter_by(username = uname).first()
#   post = Posts.query.filter_by(id = postId).first()
# #   if user is None:
# #     abort(404)
#   form = NewComment()

#   if form.validate_on_submit():
#     new_comment = Comments(comment = form.comment.data, post_id = postId)
#     db.session.add(new_comment)
#     db.session.commit()
#     return redirect(url_for('main.post_comment', postId=post.id))
  
#   comment_list = Comments.get_comments_by_post(postId)
  
#   title = "New Comment"
#   return render_template('newcomment.html',title=title, comment_form=form, CommentPost=post, comment_list=comment_list)


# @main.route('/<int:commentId>/delete',methods = ['GET','POST'])
# def delete_comment(commentId):
#   comment = Comments.query.filter_by(id = commentId).first()  
#   db.session.delete(comment)
#   db.session.commit()
#   return redirect(url_for("main.post_comment", postId=comment.post_id))

  
