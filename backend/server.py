'''
This is the main flask app where all the backend server establish
'''
from flask import Flask, jsonify,request
from flask_cors import CORS
from connection import get_sql_connection
import products_dao
import  orders_dao
import ucom_dao


app = Flask(__name__)
CORS(app)
conn = get_sql_connection()


@app.route('/products', methods=['GET'])
def get_products():
    '''
    This is the Products_dao file were accessed for get / read the table
    :return:
    '''
    products = products_dao.get_all_product(conn)
    products = jsonify(products)
    return products


@app.route('/products', methods=['POST'])
def add_product():
    '''
    This is the Products_dao file were accessed to add products to the table
    :return:
    '''
    data = request.get_json()
    product_id = products_dao.insert_new_product(conn, data)
    return jsonify({'status': 'success', 'product_id': product_id})


@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_products(product_id):
    '''
    This is the Products_dao file were accessed to delete data
    '''
    response = products_dao.delete_products(conn, product_id)
    response = jsonify(response)
    return response


@app.route('/ucom', methods=['GET'])
def get_ucom():
    ucoms = ucom_dao.get_all_ucoms(conn)
    return jsonify(ucoms)

@app.route('/orders', methods=['GET'])
def get_orders():
    orders = orders_dao.get_all_orders(conn)
    return jsonify(orders)

@app.route('/orders', methods=['POST'])
def add_order():
    data = request.get_json()
    print("Received Order:", data)
    print("Items:", data.get('items'))
    orders = orders_dao.add_new_order(conn,data)
    return jsonify(orders)


if __name__ == '__main__':
    print("Starting Python Flask Server For Grocery Store Management System")
    app.run(port=5000)
