from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators, SelectField
from passlib.hash import sha256_crypt
from functools import wraps
from flask_uploads import UploadSet, configure_uploads, IMAGES
import timeit
import datetime
from flask_mail import Mail, Message
import os
from wtforms.fields.html5 import EmailField

mysql = MySQL()
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'sys'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql.init_app(app)

@app.route('/')
def registration():
	return render_template('registration.html')


@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      fname = request.form['first_name']
      lname = request.form['last_name']
      uname = request.form['username']
      password = request.form['password']
      email = request.form['email']
      cur = mysql.connection.cursor()
      query="INSERT INTO registration VALUES (%s,%s,%s,%s,%s);",(fname,lname,uname,password,email)
      cur.execute(query, params=None, multi=False)
      mysql.connection.commit()
      cur.close()
      ans = request.form.to_dict()
      username = request.form['username']

      print(username, file=sys.stderr)
      #print "LOL"
      # print username
      return render_template("result.html",result = result)

if __name__ == '__main__':
   app.run(debug = True)