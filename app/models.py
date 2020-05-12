from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return Writer.query.get(int(writer_id))


class User(UserMixin, db.Model):
    __tablename__ = 'users'    
    
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)    
    
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())    
    password_hash = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))

    diary = db.relationship('Diary',backref = 'user',lazy="dynamic")
    

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f'User {self.username}'


class Diary(db.Model):
  
  __tablename__ ='diary'

  id = db.Column(db.Integer, primary_key = True)
  title = db.Column(db.String(255))
  description = db.Column(db.String(700))
  posted = db.Column(db.DateTime, default=datetime.utcnow)  
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  picture_pic_path = db.Column(db.String())
  

class Shopping(db.Model):
  
  __tablename__ ='shoppingList'

  id = db.Column(db.Integer, primary_key = True)
  item = db.Column(db.String(55))  
  time = db.Column(db.DateTime, default=datetime.utcnow)  
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
 

class ToDoList(db.Model):
  
  __tablename__ ='todolist'

  id = db.Column(db.Integer, primary_key = True)
  toDo = db.Column(db.String(55))  
  time = db.Column(db.DateTime, default=datetime.utcnow)  
  user_id = db.Column(db.Integer, db.ForeignKey('user.id')) 


