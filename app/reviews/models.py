from app import db




class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    message = db.Column(db.Text)

