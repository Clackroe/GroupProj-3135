#!/usr/bin/env python3

from authentication.authTools import login_pipeline, update_passwords, hash_password
from database.db import Database
from flask import Flask, redirect, render_template, request, url_for
from core.session import Sessions

app = Flask(__name__)
HOST, PORT = 'localhost', 8080
global username, products, db, sessions, hasAdminAccess
hasAdminAccess = False
username = 'default'
db = Database('database/storeRecords.db')
products = db.get_full_inventory()
sessions = Sessions()
sessions.add_new_session(username, db)


@app.route('/')
def index_page():
    """
    Renders the index page when the user is at the `/` endpoint, passing along default flask variables.

    args:
        - None

    returns:
        - None
    """
    
    
    return render_template('index.html', username=username, products=products, sessions=sessions, hasAdminAccess=hasAdminAccess)


@app.route('/admin')
def admin_page():
    """
    Renders the admin page when the user is at the `/admin` endpoint.

    args:
        - None

    returns:
        - None
    """

    return render_template('adminDash.html', logs=db.get_all_logs(), hasAdminAccess=hasAdminAccess)

@app.route('/admin', methods=['POST'])
def admin_tools():
    
    admin_tool= request.form['admin_tool']
    
    if admin_tool != None:
        return redirect(url_for(admin_tool))
        
        
@app.route('/admin/roles')
def roles():
    roles = db.get_all_user_information()
    logs = db.get_all_logs()
    return render_template('roles.html', roles=roles, logs=logs, hasAdminAccess=hasAdminAccess)

@app.route('/admin/roles', methods=['POST'])
def roles_tools():

    username = request.form['username']
    password = request.form['password']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    role = int(request.form['role'])
    
    salt, key = hash_password(password)
    update_passwords(username, key, salt)
    
    db.insert_user(username, key, email, first_name, last_name, role)
    return redirect(url_for("roles"))


@app.route('/admin/stock')
def stock():
    return render_template('stock.html', logs=db.get_all_logs(), hasAdminAccess=hasAdminAccess)

@app.route('/admin/perms')
def perms():
    return render_template('perms.html', logs=db.get_all_logs(), hasAdminAccess=hasAdminAccess)

@app.route('/login')
def login_page():
    """
    Renders the login page when the user is at the `/login` endpoint.

    args:
        - None

    returns:
        - None
    """
    return render_template('login.html')


@app.route('/home', methods=['POST'])
def login():
    """
    Renders the home page when the user is at the `/home` endpoint with a POST request.

    args:
        - None

    returns:
        - None

    modifies:
        - sessions: adds a new session to the sessions object

    """
    global username
    hasAdminAccess = False
    username = request.form['username']
    password = request.form['password']
    if login_pipeline(username, password):
        
        
        user = db.get_user_by_username(username)
        
        if user['permission'] != 0:
            hasAdminAccess = True
        
        sessions.add_new_session(username, db)
        return render_template('home.html', products=products, sessions=sessions, hasAdminAccess=hasAdminAccess)
    else:
        print(f"Incorrect username ({username}) or password ({password}).")
        return render_template('index.html', hasAdminAccess=hasAdminAccess)


@app.route('/register')
def register_page():
    """
    Renders the register page when the user is at the `/register` endpoint.

    args:
        - None

    returns:
        - None
    """
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    """
    Renders the index page when the user is at the `/register` endpoint with a POST request.

    args:
        - None

    returns:
        - None

    modifies:
        - passwords.txt: adds a new username and password combination to the file
        - database/storeRecords.db: adds a new user to the database
    """
    
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    salt, key = hash_password(password)
    update_passwords(username, key, salt)
    db.insert_user(username, key, email, first_name, last_name, 0 )
    return render_template('index.html')


@app.route('/checkout', methods=['POST'])
def checkout():
    """
    Renders the checkout page when the user is at the `/checkout` endpoint with a POST request.

    args:
        - None

    returns:
        - None

    modifies:
        - sessions: adds items to the user's cart
    """
    order = {}
    global username 
    user_session = sessions.get_session(username)
    itemVins = []
    for item in products:
        print(f"item ID: {item['vin']}")
        if request.form[str(item['vin'])] > '0':
            count =1
            order[item['make']] = count
            user_session.add_new_item(username,
                item['vin'], item["make"] + " " + item["model"], item['price'], 1)
            itemVins.append(item['vin'])
            print(f"Name: {username} ItemVin: {item['vin']}")

    user_session.submit_cart()

    
        
    return render_template('checkout.html', order=order, sessions=sessions, total_cost=user_session.total_cost)


if __name__ == '__main__':
    app.run(debug=True, host=HOST, port=PORT)
