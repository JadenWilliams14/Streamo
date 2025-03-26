from Streamo import db, login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model,UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),unique=True,index=True)
    password_hash = db.Column(db.String(128))

    favorites = db.relationship('Favorite',backref='user',lazy='dynamic')

    def __init__(self,username,password):
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)
    
    def __repr__(self):
        return f"Username {self.username}"
    
class Movies_Show(db.Model):
    
    __tablename__ = 'movies_shows'

    title = db.Column(db.String(64),primary_key=True)
    genre = db.Column(db.String(64),nullable=False)
    description = db.Column(db.String(140),nullable=False)
    release = db.Column(db.Date,nullable=False)
    duration = db.Column(db.Integer,nullable=False)
    poster = db.Column(db.String(64),nullable=False)

    favorite = db.relationship('Favorite',backref='movies_show',uselist=False)

    def __init__(self,title,genre,description,release,duration,poster):
        self.title = title
        self.genre = genre
        self.description = description
        self.release = release
        self.duration = duration
        self.poster = poster

    def __repr__(self):
        return f"Title: {self.title} -- Genre: {self.genre} -- Description: {self.description} -- Release Date: {self.release} -- Duration: {self.duration}"
    
class Favorite(db.Model):

    __tablename__ = 'favorites'

    users = db.relationship(User)
    movies_shows = db.relationship(Movies_Show)

    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)
    movie_title = db.Column(db.String(64),db.ForeignKey('movies_shows.title'),nullable=False)

    def __init__(self,movie_title,user_id):
        self.movie_title = movie_title
        self.user_id = user_id
