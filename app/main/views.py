from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User, Shopping, ToDoList, Diary
from flask_login import login_required, current_user
# from .forms import #UpdateProfile, NewPost, NewComment, UpdatePost    #### Import the forms that you create   
from .. import db,photos
from datetime import datetime
# import markdown2
from forms import ShoppingForm
# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
   

    title = 'Shopping'

    return render_template('index.html', title = title)
    

@main.route('/shopping/', methods = ['GET','POST'])
@login_required
def new_shopping():

    form = ShoppingForm()

    if form.validate_on_submit():
        shopping= form.shopping.data
        title=form.title.data

        
        new_shopping = Shopping(title=title,shopping= shopping,user_id=current_user.id)

        title='New Shopping'

        new_shopping.save_shopping()

        return redirect(url_for('main.index'))

    return render_template('shopping.html',shopping_entry= form)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(author = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(author = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.author))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(author = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/comments/<id>')
@login_required
def comment(id):
    '''
    function to return the comments
    '''
    comm =Comments.get_comment(id)
    print(comm)
    title = 'comments'
    return render_template('comments.html',comment = comm,title = title)

@main.route('/new_comment/<int:shoppingList_id>', methods = ['GET', 'POST'])
@login_required
def new_comment(shoppingList_id):
    shoppingList = ShoppingList.query.filter_by(id = shoppingList_id).first()
    form = CommentForm()

    if form.validate_on_submit():
        comment = form.comment.data

        new_comment = Comments(comment=comment,user_id=current_user.id, shoppingList_id=shoppingList_id)


        new_comment.save_comment()


        return redirect(url_for('main.index'))
    title='New Shopping'
    return render_template('new_comment.html',title=title,comment_form = form,shoppingList_id=shoppingList_id)
