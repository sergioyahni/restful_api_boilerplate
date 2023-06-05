from src.root_api import db, Resource,request
from src.books_model import BookModel as Book


class BookController(Resource):
    def get(self, book_id=None):
        if book_id:
            book = Book.query.filter_by(id=book_id).first()
            if book:
                return {'id': book.id, 'title': book.title, 'author': book.author,
                        'published_date': book.published_date, 'isbn': book.isbn}, 200
            else:
                return {'error': 'Book not found.'}, 404
        else:
            books = Book.query.all()
            return {'books': [
                {'id': book.id, 'title': book.title, 'author': book.author, 'published_date': book.published_date,
                 'isbn': book.isbn} for book in books]}, 200

    def post(self):
        book_data = request.form  # fixing the chatGPT error.
        book = Book(title=book_data['title'], author=book_data['author'], published_date=book_data['published_date'],
                    isbn=book_data['isbn'])
        db.session.add(book)
        db.session.commit()
        return {'message': 'Book added successfully.', 'id': book.id}, 201

    def put(self, book_id):
        book = Book.query.filter_by(id=book_id).first()
        if book:
            # book_data = request.get_json() # chatGPT error: TypeError: 'NoneType' object is not subscriptable
            book_data = request.form  # fixing the chatGPT error.
            book.title = book_data.get('title', book.title)
            book.author = book_data.get('author', book.author)
            book.published_date = book_data.get('published_date', book.published_date)
            book.isbn = book_data.get('isbn', book.isbn)
            db.session.commit()
            return {'message': 'Book updated successfully.'}, 200
        else:
            return {'error': 'Book not found.'}, 404

    def delete(self, book_id):
        book = Book.query.filter_by(id=book_id).first()
        if book:
            db.session.delete(book)
            db.session.commit()
            return {'message': 'Book deleted successfully.'}, 200
        else:
            return {'error': 'Book not found.'}, 404