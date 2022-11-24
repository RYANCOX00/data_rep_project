import mysql.connector
from config import login
import json

connection = None

def getConnected():
    global connection

    connection = mysql.connector.connect(
        host = login["host"],
        user = login["user"],
        password = login["password"],
        database = login["database"])
    
    return connection

def closeAll():
    connection.close()



def select(query):
    conn = getConnected()
    cursor = conn.cursor(dictionary=True) # REF: https://stackoverflow.com/questions/43796423/python-converting-mysql-query-result-to-json
    
    cursor.execute(query)

    #row_headers=[x[0] for x in cursor.description]  
    values = cursor.fetchall()

    closeAll()


    #return json.dumps
    return values


def insert_update_delete(query, values):
    conn = getConnected()
    cursor = conn.cursor()

    for i in values:
        cursor.execute(query, i)

    connection.commit()

    closeAll()


def create(queries):
    
    conn = getConnected()
    cursor = conn.cursor()

    # queries is a list of lists.  Double for loop to access the queries one at a time. 
    for i in queries:
        for x in i:
            cursor.execute(x) 

    connection.commit()

    closeAll()


def transactions_from_file(file_query, values, comm_split):
    conn = getConnected()
    cursor = conn.cursor()

    for i in values:
        cursor.execute(file_query, i)
        cursor.execute(comm_split) 

    connection.commit()

    closeAll()


