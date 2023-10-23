from flask import Flask, render_template, redirect, request, url_for
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user

from mysql_db import myDB 

mydb = myDB()
app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/')
def home():
    logged_in = False
    
    if current_user.is_authenticated:
        logged_in = True
        
    return render_template('home.html', logged_in=logged_in)



@app.route('/books')
def books():
    book_list = mydb('select * from books')
    # returns - (10, 'Self-enabling zero tolerance focus group', Decimal('6.49'))
    # book_list = [
    #     ('Book 1', 'Author 1', 10),
    #     ('Book 2', 'Author 2', 15),
    #     ('Book 3', 'Author 3', 20)
    # ]
    return render_template('books.html', books=book_list)


@app.route('/search')
def search():
    
    query = request.args.get('query', '')
    sql = "SELECT * FROM books WHERE upper(title) LIKE upper(%s)"
    values = (f'%{query}%',)    
    book_list = mydb(sql, values=values, print_output=True)

    return render_template('books.html', books=book_list)


class User(UserMixin):
    def __init__(self, id):
        self.id = id


users = {'test_user': 'password'}  # Replace with your own user data retrieval mechanism

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Retrieve submitted form data
        username = request.form['username']
        password = request.form['password']
        app.secret_key = password

        
        # Perform user registration logic (e.g., store in the database)
        # Make sure to hash and salt the password securely
        
        # Add the new user and password to the users dictionary
        users[username] = password
        
        # Redirect to the login page
        return redirect(url_for('login'))
    
    return render_template('register.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    user_info = None  # Define a default value for user_info

    if request.method == 'POST':
        # Retrieve submitted form data
        username = request.form['username']
        password = request.form['password']
        user_info = (username, password)

        # Perform user authentication logic (e.g., verify credentials against the database)
        # Make sure to compare the hashed password
        authenticated = False
        if username in users.keys() and password == users.get(username):
            authenticated = True

        # If authentication is successful, log in the user
        if authenticated:
            user = User(username)  # Create a User instance
            login_user(user)  # Log in the user using Flask-Login
            
            # Redirect to the user's profile or dashboard page
            return redirect(url_for('profile'))

    # Return a response for GET requests or unsuccessful login attempts
    return render_template('login.html')



@app.route('/logout')
@login_required
def logout():
    logout_user()  # Log out the currently logged-in user
    
    # Redirect to the home page or login page
    return redirect(url_for('home'))

@app.route('/debug')
def debug():
    return str(users)

@app.route('/profile')
@login_required  # Ensure that the user is logged in to access this route
def profile():
    username = current_user.username  # Get the currently logged in user's username
    
    # Retrieve the user's information from the users dictionary
    user_info = users.get(username)
    
    return render_template('profile.html', user_info=user_info)


if __name__ == '__main__':
    app.run(debug=True)