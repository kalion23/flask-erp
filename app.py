from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL

import os

mysql = MySQL()
app = Flask('__name__')
app.config['SECRET_KEY']=os.urandom(20)
app.config['MYSQL_DATABASE_USER'] = 'dbms'
app.config['MYSQL_DATABASE_PASSWORD'] = 'justanothersecret'
app.config['MYSQL_DATABASE_DB'] = 'erp'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
	username = request.form.get('username')
	password = request.form.get('password')
	cursor = mysql.connect().cursor()
	cursor.execute("SELECT * FROM user where username='" + username + "' and password='" + password + "'")
	data = cursor.fetchone()
	if data is None:
		return render_template('wrong-login.html')
	else:
		return "Logged in successfully"

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=8000,debug=True)