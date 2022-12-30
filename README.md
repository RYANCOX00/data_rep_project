# Data Representation Project. 
## Creating an API and consuming this API through a static page via AJAX

<br>

The purpose of this repository is for course work submission for the Data Representation module in Atlantic Technological University.  

<br>

***

<br>

## Project Description

<br>

This project creates a RESTful API through Flask. Data is pulled from a mysql database and consumed on a static page through AJAX.  

The concept of the project is a company product that provides currency convertions to banks in Europe.  The banks are referred to as the acquirers.  They implement the solution into their point of sale terminals for retail customers.  These retail customers are referred to as merchants. Once a merchant is created with and an is acquirer assigned, the program can accept transactions for that merchant.  Each acquirer and the mock company providing the solution will receive a commission on the currency exchange.  The program will calculate the commission split table depending on the pre-defined margins in the merchant_details. The mock company in this program is called "ABC Currency Solutions". 

Initial exchange rates are received and refreshed from a third party API. These are available to view on the static page under "View Latest Rates".  Once transactions are processed, all transactions and the commission splits can be viewed under "Finance Reports" on the static pages.  Acquirers and Merchants can be viewed, created, deleted, and updated under the "Acquirer and Merchant Manager" page.  

All mysql database tables listed below were made available in the API that was created using Flask. 

- currency_rates
- acquirer_details
- merchant_details
- transactions
- commission_split

<br>

***

<br>

## Steps to install

<br>

The user should then install the packages in requirements.txt.  

To run this program on you own machine the user should then run initialProgram.py.  This program will create the database, tables, initial acquirers and merchants, insert rates from the third party API, and load some sample transactions.  Note that the database is accessed based on mysql credentials on a config file which is not available on github. The user should create their own config file with their own credentials. Note the database name used in this program is "transaction_convertion".

Finally run the python file main.py to start up the server. 

This will run on your localhost.  The first page to be run will be: http://127.0.0.1:5000/login.html.  The login credentials to be used are below.

Username: "user@finance.ie"
<br>
Password: "password"

<br>

Once the initialProgram.py program is run, the user can send more transaction files to the program.  To send a new transaction file to the program, ensure the acquirer & merchant are set up in the GIU and uncomment "rt.transactions_to_db(FILENAME)" on line 12 of main.py and insert the correct filename.  Ensure the correct file format is followed as "transactions1.csv" in the initalSepUp folder. 

<br>

***

<br>

## Contact

<br>

Should any person wish to contact me in relation to the content of this project, they can contact me on my ATU email address: 

[G00398251@atu.ie](mailto:G00398251@atu.ie)


<br>

***