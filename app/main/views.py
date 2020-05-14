from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User, Shopping, ToDoList, Diary
from flask_login import login_required, current_user
from .. import db,photos
from .forms import DiaryForm, UpdateDiary
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