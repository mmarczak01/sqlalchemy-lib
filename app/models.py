from datetime import datetime
from app import db

books_authors = db.Table('books_authors',
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key=True),
    db.Column('author_id', db.Integer, db.ForeignKey('author.id'), primary_key=True)
)

class Book(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   title = db.Column(db.String(200), index=True, unique=True)
   description = db.Column(db.Text, index=True)
   authors = db.relationship("Author", secondary=books_authors, backref=db.backref("books", lazy=False), lazy="dynamic")
   book_data = db.relationship("BookData", backref="data", lazy="dynamic")

   def __str__(self):
       return f"Title: {self.title}"
   
class Author(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(100), index=True)
   surname = db.Column(db.String(100), index=True)

   def __str__(self):
       return f"Author: {self.name} {self.surname}"
   
class BookData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    rented = db.Column(db.Boolean, index=True)
    rent_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __str__(self):
        return f"Book ID: {self.book_id}, rented: {self.rented}, rendt date: {self.rent_date}"