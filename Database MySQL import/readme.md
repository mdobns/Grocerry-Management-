
# **Grocery Store Database Setup**

## **Overview**

This repository contains the SQL file for setting up the **grocery\_store** database. It includes the schema (tables, relationships) and initial data (e.g., products, orders). Use the following instructions to create the database and import the tables.

## **Steps to Set Up the Database**

### **Step 1: Create the Database**

1. **Open MySQL Workbench or phpMyAdmin**:

   * **phpMyAdmin**: Go to `http://localhost/phpmyadmin/`.
   * **MySQL Workbench**: Open MySQL Workbench and connect to your local or remote MySQL server.

2. **Create the `grocery_store` Database**:

   * **In phpMyAdmin**:

     * Go to the **Databases** tab.
     * Enter `grocery_store` as the database name and click **Create**.
   * **In MySQL Workbench**:

     * Open a new SQL tab and run the following command:

       ```sql
       CREATE DATABASE grocery_store;
       ```

### **Step 2: Import the SQL File**

Once the database is created, follow the steps to import the `.sql` file into the `grocery_store` database.

#### **In phpMyAdmin**:

1. Select the `grocery_store` database from the left sidebar.
2. Click the **Import** tab at the top.
3. Click **Choose File** and select the exported `.sql` file (e.g., `grocery_store.sql`).
4. Click **Go** to start the import process.

#### **In MySQL Workbench**:

1. Open a new SQL tab and connect to your MySQL server.
2. Select the `grocery_store` database:

   ```sql
   USE grocery_store;
   ```
3. Open the exported `.sql` file in MySQL Workbench:

   * Go to **File** > **Open SQL Script** and select the `.sql` file.
4. Run the script by clicking the **lightning bolt icon** or pressing `Ctrl+Shift+Enter`.

### **Step 3: Verify the Import**

After the import is complete, you should see the tables created in the **grocery\_store** database. Verify that the tables have been imported correctly:

1. **In phpMyAdmin**: You will see the tables listed on the left sidebar under the `grocery_store` database.
2. **In MySQL Workbench**: Refresh the schema list, and you should see the `grocery_store` database with all tables under it.

## **License**

This project is licensed under the MIT License.

---

### **Notes**

* Make sure the `.sql` file is correctly formatted, including all `CREATE` and `INSERT` statements for tables and data.
* If you encounter any issues with large SQL files in phpMyAdmin, consider increasing the **upload\_max\_filesize** and **post\_max\_size** settings in the PHP configuration.

---

This short and clear README will help the user create the database and import the tables using the `.sql` file. Let me know if you need more specific details added!
