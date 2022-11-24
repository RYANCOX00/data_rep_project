from create_tables import create_DB_tables as tables
from get_rates import currency_rates as rates
import sql_connect as sql
from flask import Flask, jsonify
import json

# create database tables where they do not already exist. - for those running my code. 
tables()

# Pull rates from third party API into the currency_rates table.
rates()




app = Flask(__name__)#, static_url_path = '', static_folder='staticpages')

# An app to return all data from a table.  Table name as variable. 
@app.route('/<table>', methods= ['GET'])
def get_all(table):
    
    comms = sql.select("select * from %s" % table)
        
    return jsonify(comms)





app.run(debug = True)