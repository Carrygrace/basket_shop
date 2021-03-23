from shop23 import db
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
#User

class Product(db.Model):
    __tablename__= 'products'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(), nullable=False)
    body = db.Column(db.Text(), nullable=False)
    price = db.Column(db.Integer(), nullable=False)
    category = db.Column(db.String(), nullable=False, default='Категория')
    availablity = db.Column(db.String(), nullable=False, default='Есть в наличии')
    image = db.Column(db.String(), nullable=False)


    def __repr__(self):
        return self.title
