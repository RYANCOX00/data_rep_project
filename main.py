#from create_tables import create_DB_tables as tables
from get_rates import currency_rates as rates
import sql_connect as sql
import read_transactions
from flask import Flask, jsonify, request
import json


# Function to refresh the rates in the database. 
rates()


app = Flask(__name__, static_url_path = '', static_folder='static')

# An app to get all rates.
@app.route('/getRates/', methods=['GET'])
def getAllRates():
    getRates = sql.selectRates()
    return jsonify(getRates)


# An app to return the transaction report.
@app.route('/transactions/', methods= ['GET'])
def getTransactions():
    values = sql.selectTransactions()
    return jsonify(values)


# An app to get transactions by merchant ID. 
@app.route('/transactions/<int:mid>', methods= ['GET'])
def TransactionsByID(mid):
    values = sql.selectTransactions()
    transaction = list(filter (lambda t : t["mid"]== mid, values))
    if len(transaction) == 0:
        return jsonify({}) , 204
    return jsonify(transaction)


# An app to get all commissionSplits.
@app.route('/commissionSplit/', methods=['GET'])
def getCommission():
    commission = sql.selectCommissionSplit()
    return jsonify(commission)


# An app to get commission splits by acq_id 
@app.route('/commissionSplit/<int:acq_id>', methods= ['GET'])
def CommissionsByID(acq_id):
    values = sql.selectCommissionSplit()
    commission = list(filter (lambda t : t["acq_id"]== acq_id, values))
    if len(commission) == 0:
        return jsonify({}) , 204
    return jsonify(commission)


# An app to return an acqurier. 
@app.route('/customer/acquirer', methods= ['GET'])
def getAllAcquirers():
    customer= sql.selectAcquirer()
    return jsonify(customer)


# An app to delete an acquirer.
@app.route('/acquirer/<int:acq_id>', methods= ['DELETE'])
def deleteAcquirer(acq_id):
    sql.deleteAcquirer(acq_id)
    return jsonify({"done":True})


# An app to return a merchant 
@app.route('/customer/merchant', methods= ['GET'])
def getAllMerchants():
    customer= sql.selectMerchant()
    return jsonify(customer)


# An app to create a new acquirer. 
@app.route('/new/acquirer', methods= ['POST'])
def createAcquirer():

    acquirer = {
        "name": request.json["name"]
    }

    newid = sql.createAcquirer(acquirer)
    
    return jsonify({'id': newid})


# An app to update a acquirer.
@app.route('/update/acquirer/<int:acq_id>', methods= ['PUT'])
def updateAcquirer(acq_id):
    acquirer = {}

    if 'name' in request.json:
        acquirer['name'] = request.json['name']

    acquirer["acq_id"] = request.json['acq_id']

    sql.updateAcquirer(acquirer)

    return jsonify({"done":True})


# An app to delete a merchant.
@app.route('/merchant/<int:mid>', methods= ['DELETE'])
def deleteMerchant(mid):
    sql.deleteMerchant(mid)
    return jsonify({"done":True})



# An app to create a new merchant. 
@app.route('/new/merchant', methods= ['POST'])
def createMerchant():

    merchant = {
        "name": request.json["name"],
        "acq_id": request.json["acq_id"],
        "margin": request.json["margin"],
        "acqMargin": request.json["acqMargin"],
        "CompMargin": request.json["CompMargin"]
        
        }

    newid = sql.createMerchant(merchant)
    
    return jsonify({'id': newid})

# An app to update a merchant.
@app.route('/update/merchant/<int:mid>', methods= ['PUT'])
def updateMerchant(mid):
    merchant = {}

    if 'name' in request.json:
        merchant['name'] = request.json['name']
    if 'margin' in request.json:
        merchant['margin'] = request.json['margin']
    if 'acqMargin' in request.json:
        merchant['acqMargin'] = request.json['acqMargin']
    if 'compMargin' in request.json:
        merchant['compMargin'] = request.json['compMargin']

    merchant["MID"] = request.json['MID']

    sql.updateMerchant(merchant)

    return jsonify({"done":True})


if __name__ == "__main__":
    app.run(debug = True)