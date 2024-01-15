Library Management System

Brief description of the project:

Library Management System

A simple library management system implemented using Python and Flask with SQLite database.

Features

View a list of books and customers.
Add new books and customers.
Delete books and customers.
RESTful API for managing books and customers.

Getting Started

Clone the repository:

git clone https://github.com/SergeyReizman/New_Library.git
cd NEW_LIBRARY_Y_2
Create a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

Install the required dependencies:

pip install -r requirements.txt

Set your secret key (replace 'your_secret_key_here'):

In app.py, replace 'your_secret_key_here' with a secure secret key.

Create the database tables:

Run the application once to automatically create the "books" and "customers" tables in the SQLite database:

python app.py

Start the application:

Open a web browser and navigate to http://localhost:5000 to use the web interface for managing books and customers.

API Endpoints
GET /api/books: Get a list of all books.

POST /api/books: Add a new book.

GET /api/books/<int:book_id>: Get details of a specific book.

DELETE /api/books/<int:book_id>: Delete a specific book.

GET /api/customers: Get a list of all customers.

POST /api/customers: Add a new customer.

GET /api/customers/<int:customer_id>: Get details of a specific customer.

DELETE /api/customers/<int:customer_id>: Delete a specific customer.

Dependencies
Flask
Flask-RESTful
SQLite
License
This project is licensed under the MIT License. See the LICENSE file for details.

Flask application with a RESTful API for managing books and customers. 
The application allows users to add, delete, and borrow books, as well as add and delete customers.

HTML template contains the structure and forms for managing books, customers, and book borrowing and returning. Here's a summary of the key elements in your HTML template:

Meta Tags and Title: These tags define the character set and viewport settings for your web page, as well as the title.

External CSS: You link to an external CSS file (styles.css) to style your web page.

Font Awesome Icons: You include Font Awesome icons to enhance the visual elements of your web page.

JavaScript Functions: You define several JavaScript functions for client-side validation and actions, including editing and deleting books and customers.

Navigation Menu: You have a navigation menu with links for adding books, adding customers, borrowing books, and returning books.

Forms:

Add a New Book Form: Allows users to add a new book with fields for title, author, year published, and copies available.

Edit Book Form: Appears when editing a book. It allows users to modify book details.

Display Book Records: Shows a table displaying book records with options to edit or delete each book.

Add a New Customer Form: Allows users to add a new customer with fields for ID and name.

Edit Customer Form: Appears when editing a customer. It allows users to modify customer details.

Display Customer Records: Shows a table displaying customer records with options to edit or delete each customer.

Borrow a Book Form: Allows customers to borrow a book by entering their ID and the book's ID.

Return a Book Form: Allows customers to return a book by entering their ID and the book's ID.

External JavaScript Libraries: You include jQuery, Popper.js, and Bootstrap JS from content delivery networks (CDNs) to enhance your web page's functionality.

Custom JavaScript File: You include a custom JavaScript file (script.js) to add your own custom functionality.

Initialization: You initialize the Flask app, set up a Flask-RESTful API, and define a secret key for flash messages.

Data Structures: You create two empty lists, books and customers, to store information about books and customers.

Book and Customer Classes: You define two classes, Book and Customer, to represent book and customer objects. The Book class stores information about books, and the Customer class stores information about customers, including the books they've borrowed.

Request Parsers: You define request parsers using reqparse from Flask-RESTful to validate and parse incoming POST requests for adding books and customers.

Resource Classes: You define resource classes for the RESTful API. BookResource handles book-related operations, such as getting a list of books, adding a new book, and deleting a book. CustomerResource handles customer-related operations in a similar way.

API Endpoints: You add the resource classes to the API and define the API endpoints for accessing books and customers.

Home Page (index): You define a route for the home page (/) that renders an HTML template with lists of books and customers.

Borrow and Return Books: You define routes for borrowing and returning books (/borrow_book and /return_book) that allow customers to borrow and return books. These routes interact with the Customer and Book objects and update the respective lists.

Main Execution: You start the Flask app with debugging enabled when the script is run directly (if __name__ == '__main__':).

Overall, this Flask application provides a basic interface for managing books and customers, including RESTful API endpoints for programmatic access and HTML templates for user interaction. Users can add, delete, borrow, and return books, as well as add and delete customers. Flash messages are used to provide feedback on the success or failure of these operations.


## Table of Contents

  - [Project Name](Library)
  - [Table of Contents](#table-of-contents)
  - [Description]

    This documentation provides a clear structure for explaining the project, its features, how to get started with it, and other important details. 

    Flask is the main class used to create a Flask application.
    render_template is used to render HTML templates.
    request is used to handle HTTP requests.
    redirect and url_for are used for URL redirection.

    Two empty lists, books and customers, are created to store information about books and customers.

    Two classes, Book and Customer, are defined to represent book and customer objects, respectively. These classes have constructors to initialize their attributes.

    / (index) route corresponds to the home page. It renders an HTML template (index.html) and passes lists of books and customers to be displayed on the page.

    /add_book route corresponds to the home page. It renders an HTML template (index.html) and passes lists of books and customers to be displayed on the page.

    /add_customer route similar to adding a book, it is used to add a new customer. 
    It retrieves customer information from a form, creates a new Customer object, and adds it to the customers list. Then, it redirects back to the home page.

    /borrow_book route handles borrowing a book. 
    It retrieves the customer ID and book title from a form, finds the customer and book by their respective attributes, and updates the lists accordingly. 
    It also checks if there are available copies of the book.

    /return_book route handles returning a book. It works similarly to the borrow_book route but in reverse. It finds the customer and book and returns the book to the library.

    if __name__ == '__main__':
    app.run(debug=True)
    This block of code checks if the script is the main application and then starts the Flask web server in debug mode if it is. 
    Debug mode provides helpful error messages and auto-reloads the server when you make changes to the code during development.


  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Usage]
## Usage

Here are the steps to get started with the Flask Book Management Application:

### Prerequisites

Before running the application, make sure you have the following prerequisites installed:

- Python (3.7 or higher)
- Flask
- Flask-RESTful

You can install Flask and Flask-RESTful using pip:

```bash
pip install flask flask-restful
pip install flask_cors

    1. Access the Web Interface:
    The librarian should open a web browser and navigate to the URL where the library management system is hosted. 
    By default, it's often http://localhost:5000/.

    2. View Existing Books:
    On the home page of the library management system, the librarian can see a list of existing books in the library. 
    This list displays book titles, authors, and the number of copies available.

    3. Add a New Book:
    The librarian can find a section labeled "Add a New Book." 
    This section typically includes input fields for the book's title, author, and the number of copies available.
    The librarian should fill out these fields with the relevant information for the new book they want to add.

    4. Submit the Book Details:
    After entering the book's information, the librarian should click the "Add Book" or "Submit" button, which will initiate a form submission.

    5. Confirmation and Update:
    Upon successful submission, the system should add the new book to the list of books in the library, including the title, author, and the specified number of copies.
    The librarian will usually receive a confirmation message, such as "Book added successfully."

    6. View Updated Book List:
    The librarian can now see the updated list of books, including the newly added book.

    7. Repeat as Needed:
    If the librarian needs to add more books, they can repeat the process by going back to the "Add a New Book" section and entering the details for each additional book.

    8. Log Out:
    Once the librarian has finished adding books, they can log out or simply close the web browser.
    
    
  - [Features]
    The librarian's interaction with the system is through the user-friendly web interface, 
    which simplifies the process of adding books to the library's collection. 
    The system takes care of storing the book details and updating the list of available books accordingly.
    - Add new books with title, author, and publication year.
    - Update existing book information.
    - Delete books from the library.
    - Search for books by title or author.
  - [Contributing](#contributing)
  - [Testing](#testing)
  - [Deployment](#deployment)
  - [Built With](#built-with)
  - [License](#license)
  - [Acknowledgments](#acknowledgments)

## Deployment

Running the Application
Clone this repository to your local machine:

git clone https://github.com/SergeyReizman/New_Library.git

Open the terminal/command prompt and navigate to the project directory.

cd New_Library

pip install -r requirements.txt

Set Up a Virtual Environment (Optional):

It's a good practice to create a virtual environment to isolate your project's dependencies. You can create a virtual environment using the following commands:

# Create a virtual environment (optional)

python -m venv venv

# Activate the virtual environment (on Windows)

venv\Scripts\activate

# Activate the virtual environment (on macOS/Linux)

source venv/bin/activate

install Flask and Required Dependencies:

Inside your virtual environment (if you created one), install Flask and any other required dependencies using pip:

pip install Flask

pip install flask-restful

pip install Flask-SQLAlchemy

pip install Flask-WTF

pip install Jinja2

In your command prompt or terminal, navigate to the directory containing your Flask application (app.py) and run the application:

py app.py

The application will start, and you will see output indicating that the Flask development server is running similar to:

 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

Open a web browser and go to http://127.0.0.1:5000/ to access the home page.

You should see output .

Access the Application:

Open a web browser and visit http://localhost:5000 (or the URL specified in your Flask application if you customized it). You should be able to access and interact with your library management system.

## Testing

Test the Application:

You can use your web browser to test the functionality by adding books, adding customers, borrowing books, and returning books through the web interface.

Shutdown the Application:

To stop the Flask application, press Ctrl+C in the terminal where the Flask server is running.

Remember that this is a basic test environment for your Flask application. 
In a production environment, you would typically use a production web server (e.g., Gunicorn) and consider deploying your application to a hosting platform like Heroku or a cloud service like AWS or Google Cloud. Additionally, for a production system, you should use a database to store data persistently rather than relying on in-memory data structures as demonstrated in your code.


Adding Books and Customers
To add a book, click on the "Add a Book" button on the home page. Fill in the required information (Title, Author, Copies) and submit the form.

To add a customer, click on the "Add a Customer" button on the home page. Provide the Customer ID and Name and submit the form.

Borrowing and Returning Books
To borrow a book, select a customer from the dropdown list, and enter the title of the book you want to borrow. Click on the "Borrow" button.

To return a book, select the customer who borrowed the book and enter the title of the book you want to return. Click on the "Return" button.

API Endpoints
You can also interact with the application's API endpoints:

Book API: http://127.0.0.1:5000/api/books
Customer API: http://127.0.0.1:5000/api/customers
Troubleshooting
If you encounter any issues or errors, make sure to check the following:

Ensure that the prerequisites are installed correctly.
Check for any syntax errors or typos in your code.
Review the console output for any error messages.
Additional Information
For more information about the Flask framework and Flask-RESTful, please refer to their official documentation:

Flask: Flask Documentation
Flask-RESTful: Flask-RESTful Documentation

Remember to have Flask and any required dependencies installed in your Python environment to run this application successfully.

The exact requirements are as follows:

aniso8601==9.0.1
blinker==1.6.2
click==8.1.7
colorama==0.4.6
Flask==2.3.3
Flask-RESTful==0.3.10
Flask-SQLAlchemy==3.1.1
Flask-WTF==1.1.1
greenlet==2.0.2
itsdangerous==2.1.2
Jinja2==3.1.2
MarkupSafe==2.1.3
pytz==2023.3.post1
six==1.16.0
SQLAlchemy==2.0.20
typing_extensions==4.7.1
Werkzeug==2.3.7
WTForms==3.0.1

## Built With

1. Passion

2. In the provided Python Flask application, several technologies, frameworks, and libraries are used. Here's a list of them:

Flask: Flask is a micro web framework for Python. 
It's used to create web applications and provides tools and libraries for building web applications, including handling routing, HTTP requests, and more.

Jinja2: Jinja2 is a templating engine for Python. It's integrated with Flask and is used for rendering HTML templates with dynamic content.

HTML (HyperText Markup Language): HTML is the standard markup language used for creating web pages. The application uses HTML templates to structure and display web content.

HTTP (Hypertext Transfer Protocol): HTTP is the protocol used for communication between web browsers and web servers. The request object from Flask is used to handle incoming HTTP requests.

Python: Python is the programming language in which the entire application is written.

These are the core technologies and frameworks used in the application.

## License

This project is licensed under the Strict License - see the Unusially Strict License for details.

## Acknowledgments

In our pursuit of knowledge and professional growth, we would like to extend our heartfelt appreciation to John Bryce Tel Aviv and its esteemed team of talented lecturers. 
Their dedication and expertise have played an integral role in shaping our educational journey, and we are deeply grateful for their commitment to excellence.
John Bryce Tel Aviv has consistently demonstrated a commitment to providing high-quality education and training programs that empower individuals to thrive in their respective fields. 
The institution's unwavering dedication to fostering a culture of continuous learning and innovation is truly commendable.
Equally praiseworthy are the lecturers who have shared their wisdom, industry insights, and expertise with us. 
Their passion for teaching, coupled with their real-world experience, has enriched our learning experiences and equipped us with the skills and knowledge needed to excel in our careers.
We would like to express our gratitude for the unwavering support, guidance, and mentorship provided by John Bryce Tel Aviv and its lecturers. 
Their contributions have not only enhanced our professional capabilities but have also inspired us to strive for excellence in all our endeavors.
In conclusion, it is with deep respect and appreciation that we acknowledge John Bryce Tel Aviv and its dedicated lecturers for their invaluable contributions to our educational and professional development. 
Their commitment to nurturing talent and fostering growth sets a benchmark for excellence that we will carry forward throughout our careers.
Thank you, John Bryce Tel Aviv, and the remarkable lecturers who have been instrumental in our journey towards success.
"# New_Library" 