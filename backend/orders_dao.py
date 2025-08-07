'''
This is for getting the orders_dao table datas
'''
def get_all_orders(connection):
    '''
    This is for getting data from table R of CRUD
    '''
    cursor = connection.cursor()
    query = (
        "SELECT order_id, customer_name, total, datetime "
        "FROM orders"
    )
    cursor.execute(query)

    results = []
    for (order_id, customer_name, total, datetime) in cursor:
        results.append({
            'order_id': order_id,
            'customer_name': customer_name,
            'total': total,
            'datetime': datetime
        })

    cursor.close()
    return results


def add_new_order(connection, order):
    '''
    This is for inserting data from web form to the table C of CRUD
    '''
    cursor = connection.cursor()

    # Insert into orders table
    order_query = (
        "INSERT INTO orders (customer_name, total, datetime) "
        "VALUES (%s, %s, %s)"
    )
    order_data = (order['customer_name'], order['total'], order['datetime'])
    cursor.execute(order_query, order_data)
    order_id = cursor.lastrowid
    connection.commit()
    cursor.close()
    return order_id
