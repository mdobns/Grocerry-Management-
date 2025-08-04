

# Grocery Store Management System

## Overview

The **Grocery Store Management System** is an internal system designed to help the store owner manage products, orders, and customers. The system uses a MySQL database to store data such as product details, customer information, and order records.

This project is intended for use by the store owner only for managing and tracking the operations of the grocery store.

## Features

* **Product Management**: Add, update, delete, and view products.
* **Order Management**: Track and update customer orders.
* **Customer Management**: Manage customer details and orders.

## Technologies Used

* **Frontend**: Vue.js (for the user interface).
* **Backend**: Flask (Python framework for the API).
* **Database**: MySQL (for storing product, order, and customer data).

## Project Structure

```
grocery-store/
├── backend/                # Flask API for the backend
│   ├── app.py              # Main application file
│   ├── models.py           # Database models
│   ├── resources/          # API resources (endpoints)
│   └── requirements.txt    # Python dependencies
│
├── ui/                     # Vue.js frontend application
│   ├── src/                # Vue.js source files
│   └── public/             # Public assets (images, icons, etc.)
│
└── database/               # SQL file for setting up the database
    └── grocery_store.sql   # SQL schema and data
```

## Installation

### **Step 1: Set Up the Database**

1. **Create the Database**:

   * **phpMyAdmin**:

     * Open phpMyAdmin at `http://localhost/phpmyadmin`.
     * Create a new database named `grocery_store`.

   * **MySQL Workbench**:

     * Open MySQL Workbench and connect to your MySQL server.
     * Open a new SQL tab and run:

       ```sql
       CREATE DATABASE grocery_store;
       ```

2. **Import the SQL File**:

   * **In phpMyAdmin**:

     1. Select the `grocery_store` database.
     2. Click the **Import** tab.
     3. Choose the `grocery_store.sql` file and click **Go**.

   * **In MySQL Workbench**:

     1. Select the `grocery_store` database.
     2. Open the `grocery_store.sql` file by going to **File** > **Open SQL Script**.
     3. Execute the script by clicking the **lightning bolt icon**.

3. **Verify the Import**:

   * Check the **Tables** section in phpMyAdmin or the schema list in MySQL Workbench to ensure the tables (e.g., `products`, `orders`, `customers`) have been created successfully.

### **Step 2: Set Up the Backend (Flask)**

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/grocery-store.git
   cd grocery-store/backend
   ```

2. **Create a Virtual Environment**:

   * On macOS/Linux:

     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   * On Windows:

     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```

3. **Install Dependencies**:

   ```bash
   pip install 
   ```

4. **Run the Application**:

   ```bash
   python server.py
   ```

   The backend will now be running on `http://127.0.0.1:5000/`.

### **Step 3: Set Up the Frontend (Vue.js)**

1. **Install Node.js and Vue CLI** (if you don’t have them):

   * Download Node.js from [here](https://nodejs.org/) and install Vue CLI:

     ```bash
     npm install -g @vue/cli
     ```

2. **Navigate to the Frontend Directory**:

   ```bash
   cd ../ui
   ```

3. **Install Dependencies**:

   ```bash
   npm install
   ```

4. **Run the Frontend**:

   ```bash
   npm run serve
   ```

   The frontend will now be running on `http://localhost:8080/`.

---

## License

This project is licensed under the MIT License.

---

This version is focused on providing simple instructions for setting up the system for the store owner. Let me know if you need any further adjustments!
