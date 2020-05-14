from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User, Shopping, ToDoList, Diary
from flask_login import login_required, current_user
from .. import db,photos

from .forms import DiaryForm, UpdateDiary, ShoppingForm
from datetime import date
from sqlalchemy import desc


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Jipange'

    return render_template('index.html', title = title)

@main.route('/diary' ,methods = ['GET', 'POST'])
@login_required
def diary():
    title = "My Diary"
    diary_entries = Diary.query.order_by(desc(Diary.id)).all()
    



    return render_template('diary/diary.html', title = title, diary_entries = diary_entries)


@main.route('/diary/<uname>/addpost', methods = ['GET', 'POST'])
def add_diary(uname):
    title = "Add Entry"
    form = DiaryForm()

    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)
 
    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data

        if "post_photo" in request.files:
            picture = photos.save(request.files["post_photo"])
            path = f"photos/{picture}"
            picture_pic_path = path
        
        new_diary = Diary(title = title, description = description , picture_pic_path = picture_pic_path, user = user)
        new_diary.save_diary()

        return redirect(url_for('main.diary'))

    return render_template('diary/diaryform.html', form = form, title = title)

@main.route('/user/<uname>')
def profile(uname):
  user = User.query.filter_by(username = uname).first()

     form = UpdateProfile()


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

@main.route('/update/<diary_id>', methods = ["GET", "POST"])
def update_diary(diary_id):
    diary = Diary.query.filter_by(id=diary_id).first()
    diary_photo = diary.picture_pic_path
    diary_title = diary.title
    diary_description = diary.description
    

    if diary is None:
        abort(404)

    form = UpdateDiary()
    if form.validate_on_submit():
        if form.title.data:
            diary.title = form.title.data
        else:
            diary.title = diary_title

        if form.description.data:
           diary.description = form.description.data
        else:
            diary.description = diary_description

        if "photo" in request.files:
            picture = photos.save(request.files["photo"])
            path =f"photos/{picture}"
            diary.picture_pic_path = path

        else:
            diary.picture_pic_path = diary_photo

        db.session.add(diary)
        db.session.commit()

        return redirect(url_for("main.diary"))

    return render_template('diary/diary_update.html', form = form)

@main.route('/delete/diary/<diary_id>')
def delete_diary(diary_id):
    diary = Diary.query.filter_by(id = diary_id).first()

    db.session.delete(diary)
    db.session.commit()


    return redirect(url_for('main.diary'))

@main.route('/todolist')
@login_required
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
