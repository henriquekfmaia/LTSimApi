import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None

def run_query(conn, query, parameters=None, return_cursor=False):
    cur = conn.cursor()
    if(parameters != None and len(parameters) > 0):
        cur.execute(query, parameters)
    else:
        cur.execute(query)
    
    rows = cur.fetchall()
    if(return_cursor):
        return [rows, cur]
    else:
        return rows



def get_params_by_size(size):
    s = ''
    for i in range(0, size):
        s = s + '?, '
    s = s[:-2]
    return s