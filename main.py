from create_tables import create_DB_tables as tables
from get_rates import currency_rates as rates

# create database tables where they do not already exist. - for those running my code. 
tables()


# Pull rates from third party API into the currency_rates table.
rates()