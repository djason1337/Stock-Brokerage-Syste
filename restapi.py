# Dominic Jason 2203959
import flask
from flask import jsonify
from flask import request


from sql import DBconnection
from sql import execute_read_query
from sql import execute_update_query

import creds

#setup application
app = flask.Flask(__name__)
app.config["DEBUG"] = True

''' INVESTOR CRUD SECTION'''
# Get method
@app.route('/api/investor', methods=['GET'])
def get_investor():
    mycreds = creds.myCreds()
    mycon = DBconnection(mycreds.hostname, mycreds.username, mycreds.password, mycreds.database)

    # CRUD operations - Create, Read, Update and Delete operations on DB
    # Read operation on DB
    sql = "select * from investor"

    items = execute_read_query(mycon, sql)
    return jsonify(items)
# post method
@app.route('/api/investor', methods=['POST'])
def post_investor():
    mycreds = creds.myCreds()
    mycon = DBconnection(mycreds.hostname, mycreds.username, mycreds.password, mycreds.database)
    
    userinput = request.get_json()
    firstname = userinput['firstname']
    lastname = userinput['lastname']

    
    sql = "INSERT INTO investor (firstname, lastname) VALUES (%s, %s)"

    execute_update_query(mycon, sql, (firstname, lastname))
    
    return jsonify({'message': 'Investor added successfully'})
# put method
@app.route('/api/investor', methods=['PUT'])
def update_investor():
    mycreds = creds.myCreds()
    mycon = DBconnection(mycreds.hostname, mycreds.username, mycreds.password, mycreds.database)
    
    userinput = request.get_json()
    id = userinput['id']
    firstname = userinput['firstname']
    lastname = userinput['lastname']
    
    sql = "UPDATE investor SET firstname = %s, lastname = %s WHERE id = %s"

    execute_update_query(mycon, sql, (firstname, lastname, id))
    
    return jsonify({'message': 'investor updated successfully'})


# Delete method
@app.route('/api/investor', methods=['DELETE'])
def delete_investor():
    mycreds = creds.myCreds()
    mycon = DBconnection(mycreds.hostname, mycreds.username, mycreds.password, mycreds.database)
    
    userinput = request.get_json()
    id = userinput['id']
    
    sql = "DELETE FROM investor WHERE id = %s"
    execute_update_query(mycon, sql, (id,))
    
    return jsonify({'message': 'investor deleted successfully'})


'''STOCK CRUD SECTION'''
# Get method
@app.route('/api/stock', methods=['GET'])
def get_stock():
    mycreds = creds.myCreds()
    mycon = DBconnection(mycreds.hostname, mycreds.username, mycreds.password, mycreds.database)

    # CRUD operations - Create, Read, Update and Delete operations on DB
    # Read operation on DB
    sql = "select * from stock"

    items = execute_read_query(mycon, sql)
    return jsonify(items)
# post method
@app.route('/api/stock', methods=['POST'])
def post_stock():
    mycreds = creds.myCreds()
    mycon = DBconnection(mycreds.hostname, mycreds.username, mycreds.password, mycreds.database)
    
    userinput = request.get_json()
    stockname = userinput['stockname']
    abbreviation = userinput['abbreviation']
    currentprice = userinput['currentprice']

    
    sql = "INSERT INTO stock (stockname, abbreviation, currentprice) VALUES (%s, %s, %s)"

    execute_update_query(mycon, sql, (stockname, abbreviation, currentprice))
    
    return jsonify({'message': 'stock added successfully'})
# put method
@app.route('/api/stock', methods=['PUT'])
def update_stock():
    mycreds = creds.myCreds()
    mycon = DBconnection(mycreds.hostname, mycreds.username, mycreds.password, mycreds.database)
    
    userinput = request.get_json()
    id = userinput['id']
    stockname = userinput['stockname']
    abbreviation = userinput['abbreviation']
    currentprice = userinput['currentprice']
    
    sql = "UPDATE stock SET stockname = %s, abbreviation = %s, currentprice = %s WHERE id = %s"

    execute_update_query(mycon, sql, (stockname, abbreviation, currentprice, id))
    
    return jsonify({'message': 'stock updated successfully'})


# Delete method
@app.route('/api/stock', methods=['DELETE'])
def delete_stock():
    mycreds = creds.myCreds()
    mycon = DBconnection(mycreds.hostname, mycreds.username, mycreds.password, mycreds.database)
    
    userinput = request.get_json()
    id = userinput['id']
    
    sql = "DELETE FROM stock WHERE id = %s"
    execute_update_query(mycon, sql, (id,))
    
    return jsonify({'message': 'stock deleted successfully'})

'''bond CRUD SECTION'''
# Get method
@app.route('/api/bond', methods=['GET'])
def get_bond():
    mycreds = creds.myCreds()
    mycon = DBconnection(mycreds.hostname, mycreds.username, mycreds.password, mycreds.database)

    # CRUD operations - Create, Read, Update and Delete operations on DB
    # Read operation on DB
    sql = "select * from bond"

    items = execute_read_query(mycon, sql)
    return jsonify(items)
# post method
@app.route('/api/bond', methods=['POST'])
def post_bond():
    mycreds = creds.myCreds()
    mycon = DBconnection(mycreds.hostname, mycreds.username, mycreds.password, mycreds.database)
    
    userinput = request.get_json()
    bondname = userinput['bondname']
    abbreviation = userinput['abbreviation']
    currentprice = userinput['currentprice']

    
    sql = "INSERT INTO bond (bondname, abbreviation, currentprice) VALUES (%s, %s, %s)"

    execute_update_query(mycon, sql, (bondname, abbreviation, currentprice))
    
    return jsonify({'message': 'bond added successfully'})
# put method
@app.route('/api/bond', methods=['PUT'])
def update_bond():
    mycreds = creds.myCreds()
    mycon = DBconnection(mycreds.hostname, mycreds.username, mycreds.password, mycreds.database)
    
    userinput = request.get_json()
    id = userinput['id']
    bondname = userinput['bondname']
    abbreviation = userinput['abbreviation']
    currentprice = userinput['currentprice']
    
    sql = "UPDATE bond SET bondname = %s, abbreviation = %s, currentprice = %s WHERE id = %s"

    execute_update_query(mycon, sql, (bondname, abbreviation, currentprice, id))
    
    return jsonify({'message': 'bond updated successfully'})


# Delete method
@app.route('/api/bond', methods=['DELETE'])
def delete_bond():
    mycreds = creds.myCreds()
    mycon = DBconnection(mycreds.hostname, mycreds.username, mycreds.password, mycreds.database)
    
    userinput = request.get_json()
    id = userinput['id']
    
    sql = "DELETE FROM bond WHERE id = %s"
    execute_update_query(mycon, sql, (id,))
    
    return jsonify({'message': 'bond deleted successfully'})


'''STOCKtransaction CRUD SECTION'''
# Get method
@app.route('/api/stocktransaction', methods=['GET'])
def get_stocktransaction():
    mycreds = creds.myCreds()
    mycon = DBconnection(mycreds.hostname, mycreds.username, mycreds.password, mycreds.database)

    # CRUD operations - Create, Read, Update and Delete operations on DB
    # Read operation on DB
    sql = "select * from stocktransaction"

    items = execute_read_query(mycon, sql)
    return jsonify(items)
# post method
@app.route('/api/stocktransaction', methods=['POST'])
def post_stocktransaction():
    mycreds = creds.myCreds()
    mycon = DBconnection(mycreds.hostname, mycreds.username, mycreds.password, mycreds.database)
    
    userinput = request.get_json()
    investorid = userinput['investorid']
    stockid = userinput['stockid']
    quantity = userinput['quantity']
    
    sql = "INSERT INTO stocktransaction (investorid, stockid, quantity) VALUES (%s, %s, %s)"
    execute_update_query(mycon, sql, (investorid, stockid, quantity))
    
    return jsonify({'message': 'stock transaction added successfully'})

#put method
@app.route('/api/stocktransaction', methods=['PUT'])
def update_stocktransaction():
    mycreds = creds.myCreds()
    mycon = DBconnection(mycreds.hostname, mycreds.username, mycreds.password, mycreds.database)
    
    userinput = request.get_json()
    investorid = userinput['investorid']
    stockid = userinput['stockid']
    quantity = userinput['quantity']
    id = userinput['id']

    sql = "UPDATE stocktransaction SET investorid = %s, stockid = %s, quantity = %s WHERE id = %s"
    execute_update_query(mycon, sql, (investorid, stockid, quantity, id))
    
    return jsonify({'message': 'stock transaction updated successfully'})

#delete method
@app.route('/api/stocktransaction/', methods=['DELETE'])
def delete_stocktransaction():
    mycreds = creds.myCreds()
    mycon = DBconnection(mycreds.hostname, mycreds.username, mycreds.password, mycreds.database)
    
    userinput = request.get_json()
    id = userinput['id']

    sql = "DELETE FROM stocktransaction WHERE id = %s"
    execute_update_query(mycon, sql, (id,))
    
    return jsonify({'message': 'stock transaction deleted successfully'})

'''bondtransaction CRUD SECTION'''
# Get method
@app.route('/api/bondtransaction', methods=['GET'])
def get_bondtransaction():
    mycreds = creds.myCreds()
    mycon = DBconnection(mycreds.hostname, mycreds.username, mycreds.password, mycreds.database)

    # CRUD operations - Create, Read, Update and Delete operations on DB
    # Read operation on DB
    sql = "select * from bondtransaction"

    items = execute_read_query(mycon, sql)
    return jsonify(items)
# post method
@app.route('/api/bondtransaction', methods=['POST'])
def post_bondtransaction():
    mycreds = creds.myCreds()
    mycon = DBconnection(mycreds.hostname, mycreds.username, mycreds.password, mycreds.database)
    
    userinput = request.get_json()
    investorid = userinput['investorid']
    bondid = userinput['bondid']
    quantity = userinput['quantity']
    
    sql = "INSERT INTO bondtransaction (investorid, bondid, quantity) VALUES (%s, %s, %s)"
    execute_update_query(mycon, sql, (investorid, bondid, quantity))
    
    return jsonify({'message': 'bond transaction added successfully'})

#put method
@app.route('/api/bondtransaction', methods=['PUT'])
def update_bondtransaction():
    mycreds = creds.myCreds()
    mycon = DBconnection(mycreds.hostname, mycreds.username, mycreds.password, mycreds.database)
    
    userinput = request.get_json()
    investorid = userinput['investorid']
    bondid = userinput['bondid']
    quantity = userinput['quantity']
    id = userinput['id']

    sql = "UPDATE bondtransaction SET investorid = %s, bondid = %s, quantity = %s WHERE id = %s"
    execute_update_query(mycon, sql, (investorid, bondid, quantity, id))
    
    return jsonify({'message': 'bond transaction updated successfully'})

#delete method
@app.route('/api/bondtransaction/', methods=['DELETE'])
def delete_bondtransaction():
    mycreds = creds.myCreds()
    mycon = DBconnection(mycreds.hostname, mycreds.username, mycreds.password, mycreds.database)
    
    userinput = request.get_json()
    id = userinput['id']

    sql = "DELETE FROM bondtransaction WHERE id = %s"
    execute_update_query(mycon, sql, (id,))
    
    return jsonify({'message': 'bond transaction deleted successfully'})

'''PORTFOLIO'''
#PORTFOLIO endpoint to view an investors portfolio
@app.route('/api/portfolio', methods=['GET'])
def get_investor_portfolio():
    mycreds = creds.myCreds()
    mycon = DBconnection(mycreds.hostname, mycreds.username, mycreds.password, mycreds.database)
    
    userinput = request.get_json()
    investorid = userinput['investorid']

    stock_sql = "SELECT * FROM stocktransaction WHERE investorid = " + str(investorid)
    stocks = execute_read_query(mycon, stock_sql)
    

    bond_sql = "SELECT * FROM bondtransaction WHERE investorid = " + str(investorid)
    bonds = execute_read_query(mycon, bond_sql)

    portfolio = {
        'stocks': stocks,
        'bonds': bonds
    }
    
    return jsonify(portfolio)




# Run
app.run()