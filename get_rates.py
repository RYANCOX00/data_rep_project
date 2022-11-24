import requests
import json
from sql_connect import insert_update_delete as iud


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
        values.append(list((rates.get(i), i)))

        #values.append(list(rates.get(i), (i)))

    query = "UPDATE currency_rates SET foreign_rate = %s WHERE foreign_name = %s"

    iud(query, values)

