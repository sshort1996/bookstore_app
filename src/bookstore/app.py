from flask import Flask, render_template, redirect, request, url_for, g, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from flask_login.mixins import AnonymousUserMixin, UserMixin
from scripts.py.role_required import ROLE_required, not_ROLE
from mysql_db import myDB, Users, Books
import logging
import os
import random
import execjs
import bcrypt


mydb = myDB()
app = Flask(__name__)
app.secret_key = os.urandom(24)
app.logger.setLevel(logging.DEBUG)

LoginManager.not_ROLE = not_ROLE
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.not_ROLE_view = 'not_ROLE'


class UnauthorizedUser(AnonymousUserMixin):
    # The AnonymousUserMixin is used by flask-login for unauthorized users.
    pass


class BasicUser(UserMixin):
    def __init__(self, user_id, username=None, password=None, role=None):
        self.id = user_id
        self.username = username 
        self.password = password  
        self.role = None


class RoleUser(UserMixin):
    def __init__(self, user_id, username=None, password=None, role='ROLE'):
        self.id = user_id
        self.username = username 
        self.password = password  
        # RoleUser has role set to the string 'ROLE'.
        self.role = role


@app.route('/')
def home():
    logged_in = False
    is_admin = False
    
    if current_user.is_authenticated:
        app.logger.debug(f'current_user.role: {current_user.role}')
        logged_in = True
        if current_user.role == 'ROLE':
            app.logger.debug('set is admin to true')
            is_admin = True

    return render_template('home.html', logged_in=logged_in, is_admin=is_admin)



@app.route('/books')
def books():
    books_db = Books()
    book_dict = books_db.read(mydb)
    
    logged_in = False
    
    if current_user.is_authenticated:
        logged_in = True
        
    return render_template('books.html', books=book_dict, logged_in=logged_in)


@app.route('/search')
def search():
    
    query = request.args.get('query', '')
    # sql = "SELECT * FROM books WHERE upper(title) LIKE upper(%s)"
    # values = (f'%{query}%',)    
    
    
    # book_list = mydb(sql, values=values, print_output=True, print_results=True)
    where_clause = "upper(title) LIKE upper(%s)"
    values = (f'%{query}%',)  
    
    # print(user.read(mydb, where=where_clause))
    books_db = Books()
    # book.read(mydb, price='5.99')
    books_list = books_db.read(mydb, where=where_clause, values=values)
    # books_dict = books_db.read(mydb, username='test_user').is_admin}")
    # app.logger.debug(f'book_list: {book_list}')

    logged_in = False
    
    if current_user.is_authenticated:
        logged_in = True

    return render_template('books.html', books=books_list, logged_in=logged_in)


@login_manager.user_loader
def load_user(user_id):
    # Retrieve the user's information from the database using the user_id
    # user_info = mydb(f"select * from users where id = {user_id}")
    users_db = Users()
    user_info = users_db.read(mydb, id = user_id)
    if user_info:
        username = user_info.username
        password = user_info.password
        is_admin = user_info.is_admin
        
        app.logger.debug(f'user_info {user_info}')
        app.logger.debug(f'is_admin {is_admin}')

        if is_admin == True:
            app.logger.debug(f'loading user - (is_admin) {is_admin}')
            return RoleUser(user_id, username, password, 'ROLE')
        elif is_admin == False:
            app.logger.debug(f'loading user - (is_admin) {is_admin}')
            return BasicUser(user_id, username, password, None)
    return None


@app.route('/register', methods=['GET', 'POST'])
def register():

    logged_in = False
    
    try:
        if current_user.is_authenticated:
            logged_in = True
    except Exception as err: 
        pass 

    if request.method == 'POST':
        # Retrieve submitted form data
        username = request.form['username']
        password = request.form['password'] 
        salt = bcrypt.gensalt()   
        full_name = request.form['full_name']
        email = request.form['email']
        phone_number = request.form['phone_number']
        home_address = request.form['home_address']

        # Perform form validation
        with open('src/bookstore/scripts/js/validation.js') as file:
            js_code = file.read()
        ctx = execjs.compile(js_code)
        valid_email = ctx.call('validateEmail', email)
        valid_password = ctx.call('validatePassword', password)
        
        if not valid_email or not valid_password:  # Call the validateEmail function from the previous example
            flash("Invalid user info", "error")
            return render_template('register.html', logged_in=logged_in)
        
        users_db = Users(
                username=username,
                password=password,
                full_name=full_name,
                email=email,
                phone_number=phone_number,
                home_address=home_address,
                is_admin=False)
        users_db.insert(mydb)
        
        try:
            if current_user.is_authenticated:
                logged_in = True
        except Exception as err: 
            pass 
        
        flash("New user created", "success")

        # Redirect to the login page
        return redirect(url_for('login', logged_in=logged_in))

    return render_template('register.html', logged_in=logged_in)


@app.route('/login', methods=['GET', 'POST'])
def login():
    user_info = None  # Define a default value for user_info

    logged_in = False
    
    try:
        if current_user.is_authenticated:
            logged_in = True
    except Exception as err: 
        pass 

    if request.method == 'POST':
        # Retrieve submitted form data
        username = request.form['username']
        password = request.form['password']
        
        users_db = Users()
        user_info = users_db.read(mydb, username = username)
        app.logger.debug(user_info)
        app.logger.debug(user_info.is_admin)
        user_id = user_info.id
        user_salt = user_info.salt.encode('utf-8') #mydb(f"select id from users where username = '{username}'")[0][0]
        entered_password_hash = bcrypt.hashpw(password.encode('utf-8'), user_salt)
        # app.logger.debug(f'entered_password_hash: {entered_password_hash}')
        # app.logger.debug(mydb(f"select is_admin from users where username = '{username}'")[0][0])
        # app.logger.debug(bool(mydb(f"select is_admin from users where username = '{username}'")[0][0]))
        # app.logger.debug(mydb(f"select is_admin from users where username = '{username}'")[0][0])
        is_admin = user_info.is_admin #mydb(f"select is_admin from users where username = '{username}'")[0][0]
        

        # user_id = user_data[0][0]
        # is_admin = bool(user_data[0][7])
        app.logger.debug(f"is_admin: {is_admin}")
        # Perform user authentication logic (e.g., verify credentials against the database)
        # Make sure to compare the hashed password
        
        authenticated = False
        hashed_password = user_info.password #mydb(f"select password from users where username = '{username}'")[0][0]
        verify_password = entered_password_hash == hashed_password.encode('utf-8')
        app.logger.debug(f'verify_password: {verify_password}')
         
        # app.logger.debug(f'manual_check: {manual_check}')
        if verify_password:
            authenticated = True
            flash("Logged in successfully!", "success")
        elif password and not verify_password:
            flash("Password is incorrect!", "error")
        # if user_cred == password:
        #     authenticated = True
        
        # If authentication is successful, log in the user
        if authenticated:
            if is_admin == True:
                app.logger.debug(f"created admin role")
                current_user = RoleUser(user_id, username, password, 'ROLE')  # Create a User instance
                app.logger.debug(f"current_user.role: {current_user.role}")
            elif is_admin == False:
                app.logger.debug(f"created basic role")
                current_user = BasicUser(user_id, username, password)  # Create a User instance
                app.logger.debug(f"current_user.role: {current_user.role}")
                
            app.logger.debug(f'current user(id): {current_user.id}')
            app.logger.debug(f'current user(user): {current_user.username}')

            login_user(current_user)  # Log in the user using Flask-Login
                    
            try:
                if current_user.is_authenticated:
                    logged_in = True
            except Exception as err: 
                pass 
            
            return redirect(url_for('profile', logged_in=logged_in))

    # Return a response for GET requests or unsuccessful login attempts
    return render_template('login.html', logged_in=logged_in)


@app.route('/logout')
# @login_required
def logout():
    logout_user()  # Log out the currently logged-in user
    
    # Redirect to the home page or login page
    return redirect(url_for('home'))

@app.route('/debug')
@ROLE_required
def debug():
    users_db = Users()
    user_info = users_db.read(mydb)
    return render_template('users.html', user_data=user_info)

@app.route('/profile')
@login_required  # Ensure that the user is logged in to access this route
def profile():
    username = current_user.username  # Get the currently logged in user's username
    # Retrieve the user's information from the users dictionary
    # user_info = mydb(f"select * from users where username = '{username}'")
    users_db = Users()
    user_info = users_db.read(mydb, username=username)
    return render_template('profile.html', user_info=user_info, logged_in = True)


@app.route('/update_user_info', methods=['POST'])
@login_required
def update_user_info():
    # Retrieve submitted form data
    new_username = request.form['username']
    new_password = request.form['password']
    new_full_name = request.form['full_name']
    new_email = request.form['email']
    new_phone_number = request.form['phone_number']
    new_home_address = request.form['home_address']

    # Update the user information in the database
    user_id = current_user.id
    users_db = Users()
    is_admin = users_db.is_admin
    
    # update_sql = f"""UPDATE users SET username = '{new_username}', password = '{new_password}',
    #      full_name = '{new_full_name}', email = '{new_email}',
    #      phone_number = '{new_phone_number}', home_address = '{new_home_address}'
    #      WHERE id = {user_id}"""
    # app.logger.debug(update_sql)
    # mydb(update_sql)
    
    

    # Redirect to the profile page or any other desired page


    user = Users(id = user_id,
                username=new_username, 
                password=new_password,     
                full_name=new_full_name,
                email=new_email,
                phone_number=new_phone_number,
                home_address=new_home_address,
                is_admin=is_admin)
    user.insert(mydb)
    
    flash("You have updated your information", "success")

    return redirect(url_for('profile'))


if __name__ == '__main__':
    app.run(debug=True)