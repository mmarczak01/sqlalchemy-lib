from app import app, db
from app.models import Book, Author, BookData, books_authors

@app.shell_context_processor
def make_shell_context():
   return {
       "db": db,
       "Book": Book,
       "Author": Author,
       "BookData": BookData
   }
