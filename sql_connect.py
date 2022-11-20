import mysql.connector
from config import login

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
    cursor = conn.cursor()

    cursor.execute(query)

    values = cursor.fetchall()

    closeAll()

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

