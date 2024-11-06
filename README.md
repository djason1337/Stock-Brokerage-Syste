Overview

This Flask-based API provides a comprehensive solution for managing investor portfolios, including investors, stocks, bonds, and their respective transactions.

Features:

    Investor Management:
        Create, read, update, and delete investor profiles.
    Stock Management:
        Create, read, update, and delete stock information.
    Bond Management:
        Create, read, update, and delete bond information.
    Transaction Management:
        Record stock and bond transactions for investors.
    Portfolio View:
        Retrieve an investor's portfolio, including their stock and bond holdings.

Prerequisites:

    Python 3.x
    Flask
    A database (e.g., MySQL, PostgreSQL)
    creds.py file with database credentials


INVESTOR CRUD OPERATIONS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Set Up the GET Request:
Method: Select GET.
URL: Enter http://127.0.0.1:5000/api/investor.
Click on “Send” to see the response.

Set Up the POST Request:
Method: Select POST.
URL: Enter http://127.0.0.1:5000/api/investor.
Headers: Add a header with Key as Content-Type and Value as application/json.
Body: Select raw and enter the JSON data, for example:
{
  "firstname": "John",
  "lastname": "Pork"
}
Click on “Send” to see the response.|

Set Up the PUT Request:
Method: Select PUT.
URL: Enter http://127.0.0.1:5000/api/investor.
Headers: Add a header with Key as Content-Type and Value as application/json.
Body: Select raw and enter the JSON data, for example:
{
  "firstname": "John",
  "lastname": "Bob",
  "id": 3
}
Click on “Send” to see the response.

Test the DELETE Endpoint in Postman:
Method: Select DELETE.
URL: Enter http://127.0.0.1:5000/api/api/investor.
Headers: Add a header with Key as Content-Type and Value as application/json.
Body: Select raw and enter the JSON data, for example:
{
  "id": 3
}
Click on “Send” to see the response.

STOCK CRUD OPERATIONS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Set Up the GET Request:
Method: Select GET.
URL: Enter http://127.0.0.1:5000/api/stock.
Click on "Send" to see the response.

Set Up the POST Request:
Method: Select POST.
URL: Enter http://127.0.0.1:5000/api/stock.
Headers: Add a header with Key as Content-Type and Value as application/json.
Body: Select raw and enter the JSON data, for example:

{
    "stockname": "Apple",
    "abbreviation": "AAPL",        
    "currentprice": 180.00
}
Click on "Send" to see the response.

Set Up the PUT Request:
Method: Select PUT.
URL: Enter http://127.0.0.1:5000/api/stock.
Headers: Add a header with Key as Content-Type and Value as application/json.
Body: Select raw and enter the JSON data, for example:
    {
        "id": 1,
        "stockname": "Updated Apple",
        "abbreviation": "AAPL",
        "currentprice": 190.00
    }
    Click on "Send" to see the response.

Test the DELETE Endpoint:
    Method: Select DELETE.
    URL: Enter http://127.0.0.1:5000/api/stock.
    Headers: Add a header with Key as Content-Type and Value as application/json.
    Body: Select raw and enter the JSON data, for example:
    {
        "id": 1
    }
Click on "Send" to see the response.

BOND CRUD OPERATIONS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Set Up the GET Request:
Method: Select GET.
URL: Enter http://127.0.0.1:5000/api/bond.
Click on "Send" to see the response.

Set Up the POST Request:
Method: Select POST.
URL: Enter http://127.0.0.1:5000/api/bond.
Headers: Add a header with Key as Content-Type and Value as application/json.
Body: Select raw and enter the JSON data, for example:

{
    "bondname": "iShares ETF",
    "abbreviation": "IEF",        
    "currentprice": 180.00
}
Click on "Send" to see the response.

Set Up the PUT Request:
Method: Select PUT.
URL: Enter http://127.0.0.1:5000/api/bond.
Headers: Add a header with Key as Content-Type and Value as application/json.
Body: Select raw and enter the JSON data, for example:
    {
        "id": 1,
        "bondname": "Updated iShares ETF",
        "abbreviation": "IEF",
        "currentprice": 190.00
    }
    Click on "Send" to see the response.

Test the DELETE Endpoint:
    Method: Select DELETE.
    URL: Enter http://127.0.0.1:5000/api/bond.
    Headers: Add a header with Key as Content-Type and Value as application/json.
    Body: Select raw and enter the JSON data, for example:
    {
        "id": 1
    }
Click on "Send" to see the response.

STOCKTRANSACTION CRUD OPERATIONS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Set Up the GET Request:

    Method: Select GET.
    URL: Enter http://127.0.0.1:5000/api/stocktransaction.
    Click on "Send" to see the response.

Set Up the POST Request:

    Method: Select POST.

    URL: Enter http://127.0.0.1:5000/api/stocktransaction.

    Headers: Add a header with Key as Content-Type and Value as application/json.

    Body: Select raw and enter the JSON data, for example:
    JSON

    {
        "investorid": 1,
        "stockid": 2,
        "quantity": 100
    }



    Click on "Send" to see the response.

Set Up the PUT Request:

    Method: Select PUT.

    URL: Enter http://127.0.0.1:5000/api/stocktransaction.

    Headers: Add a header with Key as Content-Type and Value as application/json.

    Body: Select raw and enter the JSON data, for example:
    JSON

    {
        "id": 1,
        "investorid": 1,
        "stockid": 2,
        "quantity": 150
    }



    Click on "Send" to see the response.

Test the DELETE Endpoint:

    Method: Select DELETE.

    URL: Enter http://127.0.0.1:5000/api/stocktransaction.

    Headers: Add a header with Key as Content-Type and Value as application/json.

    Body: Select raw and enter the JSON data, for example:
    JSON

    {
        "id": 1
    }



Click on "Send" to see the response.

BONDTRANSACTION CRUD OPERATIONS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Set Up the GET Request:

    Method: Select GET.
    URL: Enter http://127.0.0.1:5000/api/bondtransaction.
    Click on "Send" to see the response.

Set Up the POST Request:

    Method: Select POST.

    URL: Enter http://127.0.0.1:5000/api/bondtransaction.

    Headers: Add a header with Key as Content-Type and Value as application/json.

    Body: Select raw and enter the JSON data, for example:
    JSON

    {
        "investorid": 1,
        "bondid": 3,
        "quantity": 50
    }



    Click on "Send" to see the response.

Set Up the PUT Request:

    Method: Select PUT.

    URL: Enter http://127.0.0.1:5000/api/bondtransaction.

    Headers: Add a header with Key as Content-Type and Value as application/json.

    Body: Select raw and enter the JSON data, for example:
    JSON

    {
        "id": 1,
        "investorid": 1,
        "bondid": 3,
        "quantity": 75
    }



    Click on "Send" to see the response.

Test the DELETE Endpoint:

    Method: Select DELETE.

    URL: Enter http://127.0.0.1:5000/api/bondtransaction.

    Headers: Add a header with Key as Content-Type and Value as application/json.

    Body: Select raw and enter the JSON data, for example:
    JSON

    {
        "id": 1
    }


Click on "Send" to see the response.

PORTFOLIO CRUD OPERATIONS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Set Up the GET Request:

    Method: Select GET.

    URL: Enter http://127.0.0.1:5000/api/portfolio.

    Headers: Add a header with Key as Content-Type and Value as application/json.

    Body: Select raw and enter the JSON data, for example:
    JSON

    {
        "investorid": 1,
    }



    Click on "Send" to see the response.
