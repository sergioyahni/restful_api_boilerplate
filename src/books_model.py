from src.root_api import db

class BookModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    published_date = db.Column(db.String(10), nullable=False)
    isbn = db.Column(db.String(13), nullable=False)

    def __repr__(self):
        return f"<Book(title='{self.title}', author='{self.author}', published_date='{self.published_date}', isbn='{self.isbn}')>"
