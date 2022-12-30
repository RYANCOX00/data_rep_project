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


def selectRates():
    conn = getConnected()
    cursor = conn.cursor(dictionary=True)  # REF: https://stackoverflow.com/questions/43796423/python-converting-mysql-query-result-to-json
    
    query = "select * from currency_rates"
    
    cursor.execute(query)
    values = cursor.fetchall()
    closeAll()
    return values


def selectTransactions():
    conn = getConnected()
    cursor = conn.cursor(dictionary=True) 
    
    query = """
    select t.trans_id, t.mid, m.name, c.foreign_name, t.foreign_amount, t.base_amount, DATE_FORMAT(t.transaction_date, '%d/%m/%Y') as 'transactionDate', DATE_FORMAT(t.processed_date, '%d/%m/%Y') as 'processedDate' 
    from transactions t 
    left join merchant_details m on t.mid = m.MID
    left join currency_rates c on t.rate_id = c.rate_id
    """
    
    cursor.execute(query)
    values = cursor.fetchall()
    closeAll()
    return values


def selectCommissionSplit():
    conn = getConnected()
    cursor = conn.cursor(dictionary=True) 
    
    query = """
    SELECT c.CID, c.acq_id, a.name, c.total_commission_amount, c.acquirer_commission, c.company_commision FROM commission_split c
    left join acquirer_details a
    on c.acq_id = a.acq_id"""
    
    cursor.execute(query)
    values = cursor.fetchall()
    closeAll()
    return values


def selectAcquirer():
    conn = getConnected()
    cursor = conn.cursor(dictionary=True) 
    
    query = "select * from acquirer_details"
    
    cursor.execute(query)
    values = cursor.fetchall()
    closeAll()
    return values


def selectMerchant():
    conn = getConnected()
    cursor = conn.cursor(dictionary=True) 

    query = """
    select m.MID, m.name as merchant, m.acq_id, a.name as acquirer, m.rate_margin, m.acquirer_rate, m.comp_rate from merchant_details m
    left join acquirer_details a
    on a.acq_id = m.acq_id"""
    
    cursor.execute(query)
    values = cursor.fetchall()
    closeAll()
    return values


def deleteAcquirer(acq_id):
    conn = getConnected()
    cursor = conn.cursor()

    query = "delete from acquirer_details where acq_id = %s" % acq_id

    cursor.execute(query)
    connection.commit()

    closeAll()


def createAcquirer(acquirer):
    conn = getConnected()
    cursor = conn.cursor()

    sql = "insert into acquirer_details (name) values (%s)"
    values = [acquirer["name"]]
    
    cursor.execute(sql, values)
    
    connection.commit()
    newid = cursor.lastrowid

    closeAll()
    return newid


def updateAcquirer(acquirer):
    conn = getConnected()
    cursor = conn.cursor()

    sql = "update acquirer_details set name = %s where acq_id = %s"
    values = [acquirer["name"], acquirer["acq_id"]]
    
    cursor.execute(sql, values)
    connection.commit()

    closeAll()



def deleteMerchant(mid):
    conn = getConnected()
    cursor = conn.cursor()

    query = "delete from merchant_details where MID = %s" % mid

    cursor.execute(query)
    connection.commit()

    closeAll()


def createMerchant(merchant):
    conn = getConnected()
    cursor = conn.cursor()

    sql = "insert into merchant_details (name,acq_id, rate_margin,acquirer_rate, comp_rate ) values (%s,%s,%s,%s,%s)"
    values = [merchant["name"],
        merchant["acq_id"],
        merchant["margin"],
        merchant["acqMargin"],
        merchant["CompMargin"],]
    
    cursor.execute(sql, values)
    
    connection.commit()
    newid = cursor.lastrowid

    closeAll()
    return newid


def updateMerchant(merchant):
    conn = getConnected()
    cursor = conn.cursor()

    sql = "update merchant_details set name = %s,rate_margin =%s, acquirer_rate =%s,comp_rate=%s where MID = %s"
    
    values = [merchant["name"],merchant['margin'],merchant['acqMargin'], merchant['compMargin'], merchant["MID"]]
    
    cursor.execute(sql, values)
    connection.commit()

    closeAll()


def insertRates(query, values):
    conn = getConnected()
    cursor = conn.cursor()

    for i in values:
        cursor.execute(query, i)

    connection.commit()
    newid = cursor.lastrowid

    closeAll()
    return newid

# Function to create the database tables. 
def create(queries):
    
    conn = getConnected()
    cursor = conn.cursor()

    # queries is a list of lists.  Double for loop to access the queries one at a time. 
    for i in queries:
        for x in i:
            cursor.execute(x) 

    connection.commit()

    closeAll()


def insertCustomers(query):
    conn = getConnected()
    cursor = conn.cursor()

    cursor.execute(query)

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
