# 📚 New_Library — Streamlined Library Management System  

[![Made with Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://www.python.org/)
[![Backend Framework](https://img.shields.io/badge/Flask-Backend-black?logo=flask)](https://flask.palletsprojects.com/)
[![Database](https://img.shields.io/badge/SQLite-Database-blueviolet?logo=sqlite)](https://www.sqlite.org/index.html)
[![REST API](https://img.shields.io/badge/Flask--RESTful-API-green?logo=python)](https://flask-restful.readthedocs.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow?logo=open-source-initiative)](./LICENSE)
[![Version](https://img.shields.io/badge/Version-1.0.0-blue)](#)
[![Build](https://img.shields.io/badge/Build-Passing-brightgreen?logo=githubactions)](#)
[![HTML](https://img.shields.io/badge/Frontend-HTML%2FCSS%2FJS-orange?logo=html5)](#)

---

## 💡 Efficiently Organize, Manage, and Innovate  

**New_Library** is a robust and feature-rich **Library Management System** built with  
🐍 **Python**, ⚙️ **Flask**, and 🗃️ **SQLite**.  
It simplifies daily operations, allowing administrators and patrons to manage books, customers, and transactions through an intuitive, web-based interface.

---

## ✨ Key Features  

### 📖 Book & Patron Management  
- ➕ Add, view, edit, and delete books and patrons  

### 🔄 Borrowing System  
- 📦 Streamlined process for borrowing and returning books  
- 📊 Real-time update of availability and records  

### 🔧 RESTful API Endpoints  
- 🔗 Manage books and patrons programmatically  
- ⚙️ Integration-ready JSON API for external systems  

### 🌐 User-Friendly Interface  
- 💡 Clean HTML templates with Bootstrap styling  
- 🧭 Simple navigation and intuitive layout  

### 📢 Real-Time Feedback  
- 📩 Flash messages confirm actions instantly (add, delete, borrow, return)

---

## 🛠️ Technologies Used  

| Layer | Technology | Description |
|:------|:------------|:-------------|
| 🖥️ Frontend | **HTML**, **CSS**, **JavaScript** | Responsive UI & client-side validation |
| ⚙️ Backend | **Python**, **Flask**, **Flask-RESTful**, **Flask-SQLAlchemy** | API routing, database ORM, and logic |
| 🗄️ Database | **SQLite** | Lightweight relational database |
| 🧰 Other | **Flask-WTF**, **Jinja2**, **WTForms** | Form validation and dynamic rendering |

---

## 📋 Project Overview  

The system provides a unified solution for managing a library’s daily workflow:

- Manage books, customers, and loans  
- Track borrowing history  
- Provide both **web UI** and **REST API** access  
- Enhance user experience via Flask flash messaging  

---

## ⚙️ Getting Started  

### 🧾 Prerequisites  
Make sure you have:
- Python ≥ 3.7  
- Flask, Flask-RESTful, Flask-SQLAlchemy  

Install using pip:  
```bash
pip install flask flask-restful flask-sqlalchemy flask-wtf flask-cors


# Clone the repository
git clone https://github.com/SergeyReizman/New_Library.git
cd New_Library

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py

Access the app at: http://localhost:5000

🌐 Web Interface
🏠 Home Page

Displays:

All books & customers

Forms to add, edit, or delete entries

📚 Add Book

Form fields:

Title

Author

Year Published

Copies Available

👤 Add Customer

Form fields:

Customer ID

Name

🔄 Borrow / Return Books

Borrow or return by entering:

Customer ID

Book ID

🔗 RESTful API Endpoints

📘 Books Management

| Method | Endpoint               | Description            |
| :----- | :--------------------- | :--------------------- |
| GET    | `/api/books`           | Retrieve all books     |
| POST   | `/api/books`           | Add a new book         |
| GET    | `/api/books/<book_id>` | Retrieve specific book |
| DELETE | `/api/books/<book_id>` | Delete a book          |


🧠 Application Structure

New_Library/
 ├─ static/
 │   ├─ styles.css
 │   └─ script.js
 ├─ templates/
 │   └─ index.html
 ├─ app.py
 ├─ requirements.txt
 ├─ README.md
 └─ library.db

🧪 Testing

You can test via:

Web interface (http://localhost:5000)

API tools (e.g., Postman, cURL)

Example test:

curl http://localhost:5000/api/books

Shutdown:

CTRL + C


🌟 Future Enhancements

🔹 Authentication & Roles (Admin/Staff/User)

🔹 Book search & filtering

🔹 Loan history tracking

🔹 Cloud database integration

🔹 Dockerized deployment

🔹 Export/Import (CSV, JSON)

🧾 License

This project is licensed under the MIT License.
See the LICENSE
 file for details.

🙌 Acknowledgments

Special thanks to John Bryce Tel Aviv and its exceptional team of lecturers
for their mentorship, dedication, and inspiration during development.

Your guidance made this project possible and fostered both skill and creativity.
✨ We are grateful for your commitment to excellence in education.

👨‍💻 Author

Sergey Reizman

https://www.linkedin.com/in/sergey-reizman

----------------------------------------------------------------------------------------------------------

📚 New_Library - Streamlined Library Management System

💡 Efficiently Organize, Manage, and Innovate

📋 Project Overview

New_Library is a robust and feature-rich Library Management System developed using 🐍 Python, 🧰 Flask, and 🗃️ SQLite. Designed to simplify library operations, it provides an intuitive and efficient way to manage books and patrons while offering advanced tools for both administrators and users.

✨ Key Features:

📖 Book & Patron Management

 ➕ Add, view, and delete books and patrons easily.

🔄 Borrowing System
 📦 Borrow and return books with a streamlined process.

🔧 RESTful API Endpoints
 🔗 Programmatic access to manage books and patrons.
 ⚙️ Supports automation and external integrations.

🌐 User-Friendly Interface
 💡 Simplified navigation and intuitive HTML templates for seamless interaction.

📢 Real-Time Feedback
 📩 Flash messages confirm successful operations, enhancing user experience.

🛠️ Technologies Used

💻 Frontend: HTML, CSS, JavaScript
⚙️ Backend: Python, Flask
🗄️ Database: SQLite

This Flask application combines a clean interface with powerful backend functionality, making it ideal for managing a small library efficiently and reliably.
🌟 Revolutionize library management with New_Library—where simplicity meets functionality, and technology drives excellence.
Discover how New_Library simplifies library management with modern tech and user-friendly design!

Brief description of the project:

Library Management System

Overview
A web-based application for managing books and customers, implemented with Python, Flask, and SQLite. It features a RESTful API and user-friendly HTML templates for seamless interaction.

Key Features
Books & Customers Management: Add, view, edit, and delete records.
Borrow & Return Books: Track borrowing and returning actions.
RESTful API: Endpoints for programmatic book and customer management.

A simple library management system implemented using Python and Flask with SQLite database.

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

API Endpoints Overview

Books Management:
Retrieve All Books:
GET /api/books

Add a New Book:
POST /api/books

Retrieve a Book by ID:
GET /api/books/<int:book_id>

Delete a Book by ID:
DELETE /api/books/<int:book_id>

Customers Management:
Retrieve All Customers:
GET /api/customers

Add a New Customer:
POST /api/customers

Retrieve a Customer by ID:
GET /api/customers/<int:customer_id>

Delete a Customer by ID:
DELETE /api/customers/<int:customer_id>

Dependencies
Flask - Web framework for building the application.
Flask-RESTful - Adds REST API capabilities.
SQLite - Lightweight database for storing books and customers data (built-in with Python).

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

Built With

Passion

Technologies, Frameworks, and Libraries:

Flask: A micro web framework for Python, used to create web applications, handle routing, process HTTP requests, and manage server-side logic.

Jinja2: A templating engine for rendering dynamic HTML content, integrated with Flask.

HTML (HyperText Markup Language): Used to structure and display web content through templates.

HTTP (Hypertext Transfer Protocol): Enables communication between web browsers and servers, with Flask's request object handling incoming HTTP requests.

Python: The programming language in which the entire application is built.

These core technologies and frameworks form the backbone of the application.

License

This project is licensed under the Strict License - see the "Unusually Strict License" for more details.

Acknowledgments

New_Library

We extend our heartfelt appreciation to John Bryce Tel Aviv and its esteemed team of talented lecturers. Their dedication and expertise have been instrumental in shaping our educational journey, fostering professional growth, and inspiring us to strive for excellence.

John Bryce Tel Aviv consistently demonstrates a commitment to high-quality education, providing training programs that empower individuals to thrive. Their dedication to fostering continuous learning and innovation is truly commendable.

We deeply appreciate the lecturers' passion for teaching, real-world insights, and unwavering support. Their mentorship has enhanced our professional capabilities and inspired us to excel in our careers.

In conclusion, we acknowledge John Bryce Tel Aviv and its dedicated lecturers for their invaluable contributions. Their commitment to nurturing talent and fostering growth sets a benchmark for excellence that we will carry throughout our careers.

Thank you, John Bryce Tel Aviv, and the remarkable lecturers who have been instrumental in our journey toward success.

Why This Project Matters

I built this system to simplify library management through efficient workflows, scalable APIs, and a user-focused design.

New_Library
