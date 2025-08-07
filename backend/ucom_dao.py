'''
This is for getting the quantity type of product kg/unit
'''
def get_all_ucoms(connection):
    '''
    This is where it accesses the table to read the product quantity type
    :param connection:
    :return:
    '''
    cursor = connection.cursor()
    query = "SELECT ucom_id, ucom_name FROM ucom"
    cursor.execute(query)
    ucoms = []

    for (ucom_id, ucom_name) in cursor:
        ucoms.append({
            'ucom_id': ucom_id,
            'ucom_name': ucom_name
        })
    cursor.close()
    return ucoms
