'''
This function is for to establish connection
'''
import mysql.connector
__CNX = None

def get_sql_connection():
    '''
    This is where the connection get access of the database parameter
    :return:
    '''
    global __CNX
    if __CNX is None:
        __CNX = mysql.connector.connect(user='root', password='root',
                                      host='127.0.0.1',
                                      database='grocery_store')
    return __CNX
