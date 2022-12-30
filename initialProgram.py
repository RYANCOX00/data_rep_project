# This program should be run before main.py.  This program creates the database and tables, initially inserts the currency exchange rates, 
# initial customers, and reads in transactions from a file.

import mysql.connector
import read_transactions
from config import login
import sql_connect as sqlCon
import requests
import json
import csv



# Create the database. My credentials are read in from a config file.  Any other use will require their own credentials. 
def createdatase():
    connection = mysql.connector.connect(
    host = login["host"],
    user = login["user"],
    password = login["password"])
    #database = login["database"])
        
    cursor = connection.cursor()
    query ="CREATE DATABASE transaction_convertion"
    cursor.execute(query)

    connection.commit()
    connection.close()

# Create database tables for the first time.
def create_DB_tables():
    tables_list = []

    # Read in create table queries from CSV file. 
    DBtables = "initialSetUp/sql_tables.csv"
    with open (DBtables, 'r', newline='') as f:
        csvreader = csv.reader(f, delimiter = '\n')
        for i in csvreader:
            tables_list.append(i)

    # Passing a list of create table queries into the sql function. 
    sqlCon.create(tables_list)


# Insert first set of rates into database.  After the initial run they will be updated on the main program.
def currency_rates():
    url = 'https://api.exchangerate.host/latest'
    response = requests.get(url)
    data = response.json()

    base = data["base"]

    rates =  data["rates"]


    # backup the rates
    filename = 'current_rates_backup.json'

    with open (filename, 'w') as f:
        json.dump(rates,f,indent=4)


    values = []
    for i in rates:
        values.append(list((base, i, rates.get(i) )))
        #values.append(list((rates.get(i), (i))))

    query = "INSERT INTO currency_rates (base_name, foreign_name, foreign_rate) values (%s, %s, %s) "
    #query = "UPDATE currency_rates SET foreign_rate = %s WHERE foreign_name = %s"

    sqlCon.insertRates(query, values)



# Insert initial acquirers and mercahnts into the database.  After this initial transactions file can be received. Acquirer and merchants can be then managed in the GUI. 
def customerSetup():

    # Read in acquirers and merchants from CSV file.  Acquirers come first on the list as they a dependency for merchants. 
    customerList= "initialSetUp/initial_customers.csv"
    with open (customerList, 'r', newline='') as f:
        csvreader = csv.reader(f, delimiter = '\n')
        for line in csvreader:
            
            # Read each line directly into this SQL function as a query.
            for insert in line:
                sqlCon.insertCustomers(insert)




createdatase()
create_DB_tables()
currency_rates()
customerSetup()

file = "initialSetUp/transactions1.csv"
read_transactions.transactions_to_db(file)