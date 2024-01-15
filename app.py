from flask import Flask, render_template, request, redirect, url_for, flash
from flask_restful import Api, Resource, reqparse
import sqlite3
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

api = Api(app)

# Set a secret key for flash messages
app.secret_key = 'your_secret_key_here'

# SQLite database configuration
DATABASE = 'mylibrary.db'

# Function to create a database connection
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Create the "books" table if it doesn't exist
def create_books_table():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            year_published INTEGER NOT NULL,
            copies INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Create the "customers" table if it doesn't exist
def create_customers_table():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Home page
@app.route('/')
def index():
    conn = get_db_connection()
    books = conn.execute("SELECT id, title, author, year_published, copies FROM books").fetchall()
    customers = conn.execute("SELECT id, name FROM customers").fetchall()
    conn.close()
    return render_template('index.html', books=books, customers=customers)

# Define Book and Customer resource classes
class BookResource(Resource):
    def get(self):
        conn = get_db_connection()
        books = conn.execute("SELECT id, title, author, year_published, copies FROM books").fetchall()
        conn.close()
        return [{'id': book['id'], 'title': book['title'], 'author': book['author'], 'year_published': book['year_published'], 'copies': book['copies']} for book in books]

    def post(self):
        args = book_parser.parse_args()
        conn = get_db_connection()
        conn.execute("INSERT INTO books (title, author, year_published, copies) VALUES (?, ?, ?, ?)",
                     (args['title'], args['author'], args['year_published'], args['copies']))
        conn.commit()
        conn.close()
        flash('Book added successfully', 'success')
        # return redirect(url_for('api_books'))

        return redirect(url_for('index'))

    def delete(self, book_id):
        conn = get_db_connection()
        conn.execute("DELETE FROM books WHERE id = ?", (book_id,))
        conn.commit()
        conn.close()
        flash('Book deleted successfully', 'success')
        return {'message': 'Book deleted successfully'}

class CustomerResource(Resource):
    def get(self):
        conn = get_db_connection()
        customers = conn.execute("SELECT id, name FROM customers").fetchall()
        conn.close()
        return [{'id': customer['id'], 'name': customer['name']} for customer in customers]

    def post(self):
        args = customer_parser.parse_args()
        conn = get_db_connection()
        conn.execute("INSERT INTO customers (name) VALUES (?)", (args['name'],))
        conn.commit()
        conn.close()
        flash('Customer added successfully', 'success')
        return redirect(url_for('index'))

    def delete(self, customer_id):
        conn = get_db_connection()
        conn.execute("DELETE FROM customers WHERE id = ?", (customer_id,))
        conn.commit()
        conn.close()
        flash('Customer deleted successfully', 'success')
        return {'message': 'Customer deleted successfully'}

# Request parsers for POST requests
book_parser = reqparse.RequestParser()
book_parser.add_argument('title', type=str, required=True, help='Title of the book')
book_parser.add_argument('author', type=str, required=True, help='Author of the book')
book_parser.add_argument('year_published', type=int, required=True, help='Year the book was published')
book_parser.add_argument('copies', type=int, required=True, help='Number of copies')

customer_parser = reqparse.RequestParser()
customer_parser.add_argument('name', type=str, required=True, help='Customer name')

# Add resource classes to the API

api.add_resource(BookResource, '/api/books', '/api/books/<int:book_id>', endpoint='api.books')
api.add_resource(CustomerResource, '/api/customers', '/api/customers/<int:customer_id>')


if __name__ == '__main__':
    with app.test_request_context():
        for rule in app.url_map.iter_rules():
            if 'api.books' in rule.endpoint:
                print(rule.endpoint, rule.methods)
            else:
                print("not found endpoint")
    # Create the "books" and "customers" tables if they don't exist before running the app
    create_books_table()
    create_customers_table()
    app.run(debug=True)