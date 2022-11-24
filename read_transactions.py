import sql_connect as sql
import csv


def read_trans(filename):
    rows = []
    
    # Read in create table queries from CSV file. 
    trans = filename
    with open (trans, 'r') as f:
        csvreader = csv.reader(f)

        next(csvreader)

        for i in csvreader:
            rows.append(tuple(i))
    
    return rows


# Passing a list of create table queries into the sql function. 

def transactions_to_db()

file = read_trans("transactions1.csv")

file_query = """

INSERT INTO transactions (mid, rate_id, foreign_rate, foreign_amount, base_amount, transaction_date, processed_date)
values (%s,
(SELECT rate_id from currency_rates where foreign_name = %s), 
(select foreign_rate from currency_rates where rate_id = (SELECT rate_id from currency_rates where foreign_name = %s)) ,
%s,
foreign_rate * foreign_amount, 
%s, 
(SELECT SYSDATE()) ) 

"""

comm_split = """
INSERT INTO commission_split (acq_id, total_commission_amount, acquirer_commission, company_commision) 
values 
((select acq_id from merchant_details where MID = (select mid from transactions where trans_id = (select max(trans_id) from transactions) )),
(select base_amount from transactions where trans_id = (select max(trans_id) from transactions)) * (select rate_margin from merchant_details where MID = (select mid from transactions where trans_id = (select max(trans_id) from transactions) )), 
(select base_amount from transactions where trans_id = (select max(trans_id) from transactions)) * (select acquirer_rate from merchant_details where MID = (select mid from transactions where trans_id = (select max(trans_id) from transactions) )),
(select base_amount from transactions where trans_id = (select max(trans_id) from transactions)) * (select comp_rate from merchant_details where MID = (select mid from transactions where trans_id = (select max(trans_id) from transactions) )));

"""

sql.transactions_from_file(file_query, file, comm_split)