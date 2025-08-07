'''
This function is for performing CRUD operation on Products Table
'''

def get_all_product(connection):
    '''
    This is for reading data from the table R of CRUD
    '''
    cursor = connection.cursor()

    query = (
        "SELECT products.products_id , products.product_name, products.ucom_id, products.price_per_unit , "
        "ucom.ucom_name"
        " FROM grocery_store.products inner join ucom on products.ucom_id= ucom.ucom_id;")
    cursor.execute(query)
    products = []
    for (product_id, product_name, ucom_id, price_per_unit, ucom_name) in cursor:
        products.append(
            {
                'product_id': product_id,
                'product_name': product_name,
                'ucom_id': ucom_id,
                'price_per_unit': price_per_unit,
                'ucom_name': ucom_name
            }
        )
    return products


def insert_new_product(connection, product):
    '''
    This is for inserting data from web form to the table C of CRUD
    '''
    cursor = connection.cursor()
    query = ("INSERT INTO products "
             "(product_name, ucom_id, price_per_unit) "
             "VALUES (%s, %s, %s)")
    data = (product['product_name'], product['ucom_id'], product['price_per_unit'])
    cursor.execute(query, data)
    connection.commit()
    product_id = cursor.lastrowid
    cursor.close()
    return product_id



def delete_products(connection, product_id):
    '''
    This is for Deleting data from web form to the table D of CRUD
    '''
    cursor = connection.cursor()
    try:
        query = "DELETE FROM products WHERE products_id = %s"
        cursor.execute(query, (product_id,))
        connection.commit()
        result = {'status': 'success', 'message': f'Product {product_id} deleted.'}
    except Exception as e:
        result = {'status': 'error', 'message': str(e)}
    finally:
        cursor.close()
    return result
