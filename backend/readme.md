#Before doing this please setup the database 

# Backend - Grocery Management System

## Overview
This is the backend for the **Grocery Management System** project. It provides the necessary API endpoints for managing products, orders, and user interactions in the grocery store.

## Technologies Used
- **Flask**: A lightweight WSGI web application framework for Python.
- **SQLAlchemy**: ORM for database management.
- **SQLite/PostgreSQL**: Database for storing user data, products, and orders.
- **JWT**: JSON Web Token for user authentication.
- **Flask-RESTful**: For building REST APIs.

## Features
- **User Authentication**: Sign up, login, and authentication via JWT.
- **Product Management**: Add, update, delete, and retrieve products.
- **Order Management**: Create, update, and retrieve customer orders.
- **Database Operations**: CRUD operations with the database.
- **Error Handling**: Standardized error messages and status codes.

## Project Structure

```plaintext
backend/
├── app.py               # Main application file
├── config.py            # Configuration settings
├── models.py            # Database models
├── resources/           # API resources (endpoints)
│   ├── product.py       # Product management
│   ├── order.py         # Order management
│   └── user.py          # User management
├── database/            # Database connection logic
│   ├── connection.py    # Database connection setup
│   └── init_db.py       # Initialize database
└── requirements.txt     # Python dependencies
```
##To run this you can directly run the server.py 
```
cd backend
python server.py
```
