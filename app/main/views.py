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
    

@main.route('/diary')
def diaryTest():
    '''
    View root page function that returns the home page.
    '''
    title = 'Diary'
    
    return render_template('diary/diary.html', title = title)

@main.route('/shopping')
def shoppingTest():
    '''
    View root page function that returns the home page.
    '''
    title = 'Shopping'
    
    return render_template('shopping/shopping.html', title = title)

@main.route('/todolist')
def todolistTest():
    '''
    View root page function that returns the home page.
    '''
    title = 'ToDoList'
    
    return render_template('todolist/todolist.html', title = title)


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

@main.route('/user/<uname>')
def profile(uname):
  user = User.query.filter_by(username = uname).first()


  if user is None:
      abort(404)
  title = "Profile"
  return render_template("profile/profile.html", user=user, title=title)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data


        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('.profile',uname=uname))



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

  
# Todolist1

# @main.route('/todolist')
# def todo():
#     incomplete = ToDoList.query.filter_by(complete=False).all()
#     complete = ToDoList.query.filter_by(complete=True).all()

#     return render_template('todolist/todolist.html', incomplete=incomplete, complete=complete)

# @main.route('/add', methods=['POST'])
# def add ():
#     todolist = ToDoList(text=request.form['todoitem'], complete=False)
#     db.session.add(todolist)
#     db.session.commit()

#     return redirect(url_for('/todolist'))

# @main.route('/complete/<id>')
# def complete(id):
#     todolist = ToDoList.query.filter_by(id=int(id)).first()
#     todo.complete = True
#     db.session.commit()
    
#     return redirect(url_for('/todolist'))

# todolist2

@main.route('/todolist')
def tasks_list():
    tasks = ToDoList.query.all()
    return render_template('todolist/todolist.html', tasks=tasks)


@main.route('/task', methods=['POST'])
def add_task():
    content = request.form['content']
    if not content:
        return 'Ooops! Error you forgot to input text'

    task = ToDoList(content)
    db.session.add(task)
    db.session.commit()
    return redirect('/todolist')


@main.route('/delete/<int:task_id>')
def delete_task(task_id):
    task = ToDoList.query.get(task_id)
    if not task:
        return redirect('/todolist')

    db.session.delete(task)
    db.session.commit()
    return redirect('/todolist')


@main.route('/done/<int:task_id>')
def resolve_task(task_id):
    task = ToDoList.query.get(task_id)

    if not task:
        return redirect('/todolist')
    if task.done:
        task.done = False
    else:
        task.done = True

    db.session.commit()
    return redirect('/todolist')


if __name__ == '__main__':
    app.run(debug=True)