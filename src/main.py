from src.root_api import app, db, api
from src.books_controller import BookController

api.add_resource(BookController, '/books', '/books/<int:book_id>')
# with app.app_context():
#     db.create_all()
app.run(debug=True)
