
from app import app, db, loginManager
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class User():
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    posts = relationship('Post', backref='user')

class Post():
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))


users_roles = db.Table('UserRole',
    db.Column('user_id',
        db.Integer,
        db.ForeignKey('users.id'),
        primary_key=True
    ),
    db.Column('role_id',
        db.Integer, 
        db.ForeignKey('roles.id'), 
        primary_key=True
    )
)

class Post(db.Model):
    __tablename__ = 'posts'
    
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
        nullable=False
    )
    
    tittle = db.Column(
        db.String(50),
        nullable=False
        
    )     
    text = db.Column(
        db.String(300),
        nullable=False
    )     
    
class User(UserMixin, db.Model):
    __tablename__ = 'users'
      
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    login = db.Column(
        db.String(180),
        nullable=False,
        unique=True    
    )  
    password_hash = db.Column(
        db.String(150),
        nullable=False
    )
    
    posts = db.relationship(
        Post.__name__,
        backref=__tablename__
    )
    
    user_roles = db.relationship(
        'Role', 
        secondary=users_roles, 
        backref=db.backref('roles', lazy=True)
    )
    
class Role(db.Model):
    __tablename__ = 'roles'
      
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    name = db.Column(
        db.String(50),
        nullable=False,
        unique=True    
    )  
    
    
@loginManager.user_loader
def load_user(id):
    return User.query.get(int(id))