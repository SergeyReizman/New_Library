# Import necessary modules
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_restful import Api, Resource, reqparse

# Initialize Flask app and Flask-RESTful API
app = Flask(__name__)
api = Api(app)

# Set a secret key for flash messages
app.secret_key = 'your_secret_key_here'

# Create empty data structures to store books and customers
books = []
customers = []

# Define Book and Customer classes
class Book:
    def __init__(self, title, author, year_published, copies):
        self.id = len(books) + 1  # Generate a unique ID for each book
        self.title = title
        self.author = author
        self.year_published = year_published
        self.copies = copies

class Customer:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.borrowed_books = []

# Define request parsers for POST requests
book_parser = reqparse.RequestParser()
book_parser.add_argument('title', type=str, required=True, help='Title of the book')
book_parser.add_argument('author', type=str, required=True, help='Author of the book')
book_parser.add_argument('year_published', type=int, required=True, help='Year the book was published')
book_parser.add_argument('copies', type=int, required=True, help='Number of copies')

customer_parser = reqparse.RequestParser()
customer_parser.add_argument('id', type=str, required=True, help='Customer ID')
customer_parser.add_argument('name', type=str, required=True, help='Customer name')

# Define resource classes for the RESTful API
class BookResource(Resource):
    def get(self):
        return [{'id': book.id, 'title': book.title, 'author': book.author, 'year_published': book.year_published, 'copies': book.copies} for book in books]

    def post(self):
        args = book_parser.parse_args()
        new_book = Book(args['title'], args['author'], args['year_published'], args['copies'])
        books.append(new_book)
        flash('Book added successfully', 'success')
        return redirect(url_for('index'))

    def delete(self, book_id):
        for book in books:
            if book.id == int(book_id):
                books.remove(book)
                flash('Book deleted successfully', 'success')
                return {'message': 'Book deleted successfully'}
        return {'message': 'Book not found'}, 404

class CustomerResource(Resource):
    def get(self):
        return [{'id': customer.id, 'name': customer.name} for customer in customers]

    def post(self):
        args = customer_parser.parse_args()
        new_customer = Customer(args['id'], args['name'])
        customers.append(new_customer)
        flash('Customer added successfully', 'success')
        return redirect(url_for('index'))

    def delete(self, customer_id):
        for customer in customers:
            if customer.id == customer_id:
                customers.remove(customer)
                flash('Customer deleted successfully', 'success')
                return {'message': 'Customer deleted successfully'}
        return {'message': 'Customer not found'}, 404

# Add the resource classes to the API
api.add_resource(BookResource, '/api/books', '/api/books/<string:book_id>')
api.add_resource(CustomerResource, '/api/customers', '/api/customers/<string:customer_id>')

# Home page
@app.route('/')
def index():
    return render_template('index.html', books=books, customers=customers)

# Borrow a book
@app.route('/borrow_book', methods=['POST'])
def borrow_book():
    customer_id = request.form['customer_id']
    book_title = request.form['book_title']
    for customer in customers:
        if customer.id == customer_id:
            for book in books:
                if book.title == book_title and book.copies > 0:
                    customer.borrowed_books.append(book)
                    book.copies -= 1
                    flash('Book borrowed successfully', 'success')
                    return redirect(url_for('index'))
    flash('Book not found or customer not registered.', 'error')
    return redirect(url_for('index'))

# Return a book
@app.route('/return_book', methods=['POST'])
def return_book():
    customer_id = request.form['customer_id']
    book_title = request.form['book_title']
    for customer in customers:
        if customer.id == customer_id:
            for book in customer.borrowed_books:
                if book.title == book_title:
                    customer.borrowed_books.remove(book)
                    book.copies += 1
                    flash('Book returned successfully', 'success')
                    return redirect(url_for('index'))
    flash('Book not found or customer not registered.', 'error')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
