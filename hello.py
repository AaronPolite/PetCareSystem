# Store this code in 'app.py' file
from user import User
from UserTree import Node, Tree

from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

abc = 2

app = Flask(__name__)

admin_user = User("admin", "admin", "admin@vet.com", "0", [])
admin_node = Node(admin_user)
helloTree = Tree(admin_node)

test_user = User("test", "test", "test@vet.com", "-1", [])
test_user_node = Node(test_user)
admin_node.add_child(test_user_node)

test_user_2 = User("test2", "test2", "test2@vet.com", "-1", [])
test_user_node_2 = Node(test_user_2)
admin_node.add_child(test_user_node_2)

app.secret_key = 'your secret key'

app.config['MYSQL_HOST'] = '173.62.210.147'
app.config['MYSQL_USER'] = 'access'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'test'

mysql = MySQL(app)



@app.route('/')
@app.route('/login', methods =['GET', 'POST'])
def login():
	msg = ''
	if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
		username = request.form['username']
		password = request.form['password']
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM accounts WHERE username = % s AND password = % s', (username, password, ))
		account = cursor.fetchone()
		if account:
			session['loggedin'] = True
			session['id'] = account['id']
			session['username'] = account['username']
			msg = 'Logged in successfully !'
			if account['id'] == 1:
			   return render_template('admin.html', msg = msg)
			else:
				return render_template('index.html', msg = msg)
		else:
			msg = 'Incorrect username / password !'
	return render_template('login.html', msg = msg)

@app.route('/logout')
def logout():
	session.pop('loggedin', None)
	session.pop('id', None)
	session.pop('username', None)
	return redirect(url_for('login'))

@app.route('/register', methods =['GET', 'POST'])
def register():
	msg = ''
	if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form :
		username = request.form['username']
		password = request.form['password']
		email = request.form['email']
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM accounts WHERE username = % s', (username, ))
		account = cursor.fetchone()
		if account:
			msg = 'Account already exists !'
		elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
			msg = 'Invalid email address !'
		elif not re.match(r'[A-Za-z0-9]+', username):
			msg = 'Username must contain only characters and numbers !'
		elif not username or not password or not email:
			msg = 'Please fill out the form !'
		else:
			cursor.execute('INSERT INTO accounts VALUES (NULL, % s, % s, % s)', (username, password, email, ))
			mysql.connection.commit()
			msg = 'You have successfully registered !'
	elif request.method == 'POST':
		msg = 'Please fill out the form !'
	return render_template('register.html', msg = msg)

@app.route('/edit')
def edit():
	return render_template('edit.html')

@app.route('/modify')
def modify():
	return render_template('modify.html')

@app.route('/modify2')
def modify2():
	return render_template('modify2.html')

@app.route('/view')
def view():
	return render_template('view.html')

@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')

@app.route('/records')
def records():
	return render_template('records.html')

@app.route('/bills')
def bills():
	return render_template('bills.html')

@app.route('/recent')
def recent():
	return render_template('recent.html')

@app.route('/add', methods=['GET', 'POST'])
def add():
	abc = 6
	msg = ''
	#  and 'firstNameText' in request.form and 'lastNameText' in request.form and 'emailText' in request.form and 'phoneNumberText' in request.form and 'petNameText' in request.form and 'speciesText' in request.form and 'petAgeText' in request.form
	if request.method == 'POST' and 'userText' in request.form and 'passText' in request.form:
		first_name = request.form.get('firstNameText')
		last_name = request.form.get('lastNameText')
		email = request.form.get('emailText')
		phone_number = request.form.get('phoneNumberText')
		pet_name = request.form.get('petNameText')
		pet_species = request.form.get('speciesText')
		pet_age = request.form.get('petAgeText')
		username = request.form['userText']
		password = request.form['passText']
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM accounts WHERE id = % s', (abc, ))
		account = cursor.fetchone()
		while account:
			abc += 1
			cursor.execute('SELECT * FROM accounts WHERE id = % s', (abc, ))
			account = cursor.fetchone()
		cursor.execute('INSERT INTO accounts VALUES (%s,  % s, % s, % s)', (abc, username, password, email, ))
		mysql.connection.commit()
		new_user = User(last_name, first_name, email, phone_number, None)
		new_user_node = Node(new_user)
		helloTree.root.add_child(new_user_node)

	helloTree.root.show_children()
	return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)