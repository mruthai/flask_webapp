from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(120), nullable=True)
    user_posts = db.relationship('Post', backref='author', lazy='dynamic')
    player_post = db.relationship('Player', backref='player_author', lazy='dynamic')

    def __repr__(self):
        if self.email:
            return f'<User: {self.username}>'
        return f'User: {self.username}'
    
    def __str__(self):
        return f'{self.username}'
    
    def hash_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def commit(self):
        db.session.add(self)
        db.session.commit()

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    team_name = db.Column(db.String(64))
    position = db.Column(db.String(64))
    age = db.Column(db.Integer)
    nationality = db.Column(db.String(64))
    price = db.Column(db.Integer)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def commit(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'Player: {self.first_name} {self.last_name} {self.team_name} {self.position} {self.age} {self.nationality} {self.price} {self.date_created}'

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    body = db.Column(db.String(500), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Post: {self.title} {self.body}>'

    def commit(self):
        db.session.add(self)
        db.session.commit()

    
    

    