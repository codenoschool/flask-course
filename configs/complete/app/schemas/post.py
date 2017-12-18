from app import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    document = db.Column(db.Text(length=None), nullable=False)