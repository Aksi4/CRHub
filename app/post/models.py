from app import db, login_manager, bcrypt
from flask_login import UserMixin
from datetime import datetime
from sqlalchemy import Enum

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    text = db.Column(db.String, nullable=False)
    contacts = db.Column(db.String, nullable=False)
    image_file = db.Column(db.String(100), nullable=False, default='default.jpg')
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    type = db.Column(db.Enum('Zakarpattia', 'Ivano-Frankivsk', 'Chernivtsi', 'Lviv', 'Other'), nullable=False, default='Other')
    enabled = db.Column(db.Boolean, default=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    reviews = db.relationship('Reviews', backref='post', lazy=True)

    # Coordinates
    latitude = db.Column(db.Float, nullable=True)
    longitude = db.Column(db.Float, nullable=True)

    def __repr__(self):
        return f"Post(id={self.id}, title={self.title}, type={self.type}, created={self.created})"
    
class Reviews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    username = db.relationship('User', backref='reviews')
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    message = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f"Reviews(id={self.id}, user_id={self.user_id}, post_id={self.post_id}, timestamp={self.timestamp})"
