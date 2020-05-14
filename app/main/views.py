from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User, Shopping, ToDoList, Diary
from flask_login import login_required, current_user
# from .forms import #UpdateProfile, NewPost, NewComment, UpdatePost    #### Import the forms that you create   
from .. import db,photos
from datetime import datetime
# import markdown2
from .forms import ShoppingForm
# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
   

    title = 'Jipange'

    return render_template('index.html', title = title)
    

@main.route('/home/<int:postId>/deletePost',methods = ['GET','POST'])
@login_required
def delete_post(postId):
   post = Posts.query.filter_by(id = postId).first()   
   db.session.delete(post)
   db.session.commit()
   return redirect(url_for("main.home", postId=post.id))  
  


@main.route('/home/<int:postId>/changePost',methods = ['GET','POST'])
@login_required
def update_posts(postId):
   post = Posts.query.filter_by(id = postId).first()
   if post is None:
       abort(404)

   form = UpdatePost()

   if form.validate_on_submit():
     post.description = form.description.data

     db.session.add(post)
     db.session.commit()

     return redirect(url_for('.home'))

   title = "Edit Post"
   return render_template('updateForm.html',form=form, title=title)

@main.route('/user/<uname>')
def profile(uname):
   user = user.query.filter_by(username = uname).first()

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
         writer.profile_pic_path = path
         db.session.commit()
     return redirect(url_for('.profile',uname=uname))


@main.route('/shopping', methods = ['GET','POST'])
@login_required
def shopping():
    user = User.query.filter_by().first()

    if user is None:
        abort(404)


    form = ShoppingForm()
    shopping = Shopping()

    if form.validate_on_submit():
        
        shopping.title= form.title.data
        shopping.message=form.message.data
        shopping.user_id =current_user.id

        db.session.add(shopping)
        db.session.commit()
        
        return redirect(url_for('main.shopping'))

    shopping_list = Shopping.get_shopping()

    return render_template('shopping/shopping.html',user=user,Shopping=form,shopping_list=shopping_list)

@main.route('/delete/<int:item_id>')
def delete_item(item_id):
    shopping_item = Shopping.query.get(item_id)    
    db.session.delete(shopping_item)
    db.session.commit()

    return redirect(url_for('main.shopping'))





# @main.route('/shopping',methods=['GET','POST'])
# def shopping():
#    user = User.query.filter_by(username = uname).first()

# #   if user is None:
# #     abort(404)
#   form = Shopping()

#   if form.validate_on_submit():
#     new_shopping = Shopping(title=title,shopping= shopping,user_id=current_user.id)

#     db.session.add(new_shopping)
#     db.session.commit()

#     return redirect(url_for('main.shopping'))
  
#   shopping_list = Shopping.get_comments_by_post(postId)
  
#   title = "New ShoppingList"
#   return render_template('newcomment.html',title=title, comment_form=form, CommentPost=post, comment_list=comment_list)


# @main.route('/<int:commentId>/delete',methods = ['GET','POST'])
# def delete_comment(commentId):
#   comment = Comments.query.filter_by(id = commentId).first()  
#   db.session.delete(comment)
#   db.session.commit()
#   return redirect(url_for("main.post_comment", postId=comment.post_id))

# @main.route('/shopping')
# def purchases_list():
#     purchases = Shopping.query.all()
#     return render_template('shopping/shopping.html', purchases=purchases)


# @main.route('/purchase', methods=['POST'])
# def add_purchase():
#     content = request.form['content']
#     if not content:
#         return 'Ooops! Error you forgot to input text'

#     purchase = Shopping(content)
#     db.session.add(purchase)
#     db.session.commit()
#     return redirect('/shopping')


# @main.route('/delete/<int:purchase_id>')
# def delete_purchase(purchase_id):
#     purchase = Shopping.query.get(purchase_id)
#     if not purchase:
#         return redirect('/shopping')

#     db.session.delete(purchase)
#     db.session.commit()
#     return redirect('/shopping')


# @main.route('/done/<int:purchase_id>')
# def complete_purchase(purchase_id):
#     purchase = Shopping.query.get(purchase_id)

#     if not purchase:
#         return redirect('/shopping')
#     if purchase.done:
#         purchase.done = False
#     else:
#         purchase.done = True

#     db.session.commit()
#     return redirect('/shopping')


# #if __name__ == '__main__':
# #    app.run(debug=True) 