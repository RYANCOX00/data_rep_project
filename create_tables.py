from sql_connect import create
import csv

def create_DB_tables():
    tables_list = []

    # Read in create table queries from CSV file. 
    DBtables = "sql_tables.csv"
    with open (DBtables, 'r', newline='') as f:
        csvreader = csv.reader(f, delimiter = '\n')
        for i in csvreader:
            tables_list.append(i)

    # Passing a list of create table queries into the sql function. 
    create(tables_list)
