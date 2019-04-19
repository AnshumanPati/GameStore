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

app = Flask(__name__)
app.secret_key = os.urandom(24)
mysql = MySQL()
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'sys'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql.init_app(app)

def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, *kwargs)
        else:
            return redirect(url_for('login'))

    return wrap


def not_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return redirect(url_for('index'))
        else:
            return f(*args, *kwargs)

    return wrap

def wrappers(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)

    return wrapped

@app.route('/register')
def registration():
	return render_template('registration.html')

class OrderForm(Form):  # Create Order Form
    name = StringField('', [validators.length(min=1), validators.DataRequired()],
                       render_kw={'autofocus': True, 'placeholder': 'Full Name'})
    mobile_num = StringField('', [validators.length(min=1), validators.DataRequired()],
                             render_kw={'autofocus': True, 'placeholder': 'Mobile'})
    quantity = SelectField('', [validators.DataRequired()],
                           choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])
    order_place = StringField('', [validators.length(min=1), validators.DataRequired()],
                              render_kw={'placeholder': 'Order Place'})





@app.route('/')
def index():
    form = OrderForm(request.form)
    # Create cursor
    cur = mysql.connection.cursor()
    # Get message
    values = 'xbox'
    cur.execute("SELECT * FROM products WHERE category=%s ORDER BY RAND() LIMIT 4", (values,))
    xbox = cur.fetchall()
    values = 'pc'
    cur.execute("SELECT * FROM products WHERE category=%s ORDER BY RAND() LIMIT 4", (values,))
    pc = cur.fetchall()
    values = 'ps4'
    cur.execute("SELECT * FROM products WHERE category=%s ORDER BY RAND() LIMIT 4", (values,))
    ps4 = cur.fetchall()
    
    # Close Connection
    cur.close()
    return render_template('index.html', xbox=xbox, pc=pc, ps4=ps4, form=form)


@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        # GEt user form
        username = request.form['username']
        # password_candidate = request.form['password']
        password_candidate = request.form['password']

        # Create cursor
        cur = mysql.connection.cursor()

        # Get user by username
        result = cur.execute("SELECT * FROM users WHERE username=%s", [username])

        if result > 0:
            # Get stored value
            data = cur.fetchone()
            password = data['password']
            uid = data['id']
            name = data['fname']

            # Compare password
            if sha256_crypt.verify(password_candidate, password):
               # passed
               session['logged_in'] = True
               session['uid'] = uid
               session['s_name'] = name
               x = '1'
               cur.execute("UPDATE users SET online=%s WHERE id=%s", (x, uid))

               return redirect(url_for('index'))

            else:
               flash('Incorrect password', 'danger')
               return render_template('login.html')

        else:
            flash('Username not found', 'danger')
            # Close connection
            cur.close()
            return render_template('login.html')
    return render_template('login.html')



@app.route('/regsuccess')
def regsuccess():
   return render_template('regsuccess.html')

@app.route('/regprocess',methods = ['POST', 'GET'])
def regprocess():
   if request.method == 'POST':
      result = request.form
      fname = request.form['first_name']
      lname = request.form['last_name']
      uname = request.form['username']
      password = sha256_crypt.encrypt(str(request.form['password']))
      email = request.form['email']
      cur = mysql.connection.cursor()
      cur.execute("INSERT INTO users(fname, lname, email, username, password) VALUES(%s, %s, %s, %s, %s)",(fname, lname, email, uname, password))
      mysql.connection.commit()
      cur.close()
      ans = request.form.to_dict()
      username = request.form['username']

      flash('You are now registered and can login', 'success')

      return redirect(url_for('regsuccess'))
   return render_template("registration.html")

@app.route('/xbox', methods=['GET', 'POST'])
def xboxdesc():
   form = OrderForm(request.form)
   # Create cursor
   cur = mysql.connection.cursor()
   # Get message
   values = 'xbox'
   cur.execute("SELECT * FROM products WHERE category=%s ORDER BY id ASC", (values,))
   products = cur.fetchall()
   # Close Connection
   cur.close()
   if request.method == 'POST' and form.validate():
      name = form.name.data
      mobile = form.mobile_num.data
      order_place = form.order_place.data
      quantity = form.quantity.data
      pid = request.args['order']
      now = datetime.datetime.now()
      week = datetime.timedelta(days=7)
      delivery_date = now + week
      now_time = delivery_date.strftime("%y-%m-%d %H:%M:%S")
      # Create Cursor
      curs = mysql.connection.cursor()
      if 'uid' in session:
         uid = session['uid']
         curs.execute("INSERT INTO orders(uid, pid, ofname, mobile, oplace, quantity, ddate) "
                      "VALUES(%s, %s, %s, %s, %s, %s, %s)",
                      (uid, pid, name, mobile, order_place, quantity, now_time))
      else:
         curs.execute("INSERT INTO orders(pid, ofname, mobile, oplace, quantity, ddate) "
                     "VALUES(%s, %s, %s, %s, %s, %s)",
                     (pid, name, mobile, order_place, quantity, now_time))
      # Commit cursor
      mysql.connection.commit()

      # Close Connection
      cur.close()

      flash('Order successful', 'success')
      return render_template('xbox.html', xbox=products, form=form)
   if 'view' in request.args:
      product_id = request.args['view']
      curso = mysql.connection.cursor()
      curso.execute("SELECT * FROM products WHERE id=%s", (product_id,))
      product = curso.fetchall()

      if 'uid' in session:
         uid = session['uid']
         # Create cursor
         cur = mysql.connection.cursor()
         cur.execute("SELECT * FROM product_view WHERE user_id=%s AND product_id=%s", (uid, product_id))
         result = cur.fetchall()
         if result:
            now = datetime.datetime.now()
            now_time = now.strftime("%y-%m-%d %H:%M:%S")
            cur.execute("UPDATE product_view SET date=%s WHERE user_id=%s AND product_id=%s",
                        (now_time, uid, product_id))
         else:
            cur.execute("INSERT INTO product_view(user_id, product_id) VALUES(%s, %s)", (uid, product_id))
            mysql.connection.commit()
      return render_template('xbox_desc.html', games=product)
   elif 'order' in request.args:
      product_id = request.args['order']
      curso = mysql.connection.cursor()
      curso.execute("SELECT * FROM products WHERE id=%s", (product_id,))
      product = curso.fetchall()
      return render_template('order_product.html', games=product, form=form)
   return render_template('xbox.html', xbox=products, form=form)

@app.route('/pc', methods=['GET', 'POST'])
def pcdesc():
   form = OrderForm(request.form)
   # Create cursor
   cur = mysql.connection.cursor()
   # Get message
   values = 'pc'
   cur.execute("SELECT * FROM products WHERE category=%s ORDER BY id ASC", (values,))
   products = cur.fetchall()
   # Close Connection
   cur.close()
   if request.method == 'POST' and form.validate():
      name = form.name.data
      mobile = form.mobile_num.data
      order_place = form.order_place.data
      quantity = form.quantity.data
      pid = request.args['order']
      now = datetime.datetime.now()
      week = datetime.timedelta(days=7)
      delivery_date = now + week
      now_time = delivery_date.strftime("%y-%m-%d %H:%M:%S")
      # Create Cursor
      curs = mysql.connection.cursor()
      if 'uid' in session:
         uid = session['uid']
         curs.execute("INSERT INTO orders(uid, pid, ofname, mobile, oplace, quantity, ddate) "
                      "VALUES(%s, %s, %s, %s, %s, %s, %s)",
                      (uid, pid, name, mobile, order_place, quantity, now_time))
      else:
         curs.execute("INSERT INTO orders(pid, ofname, mobile, oplace, quantity, ddate) "
                     "VALUES(%s, %s, %s, %s, %s, %s)",
                     (pid, name, mobile, order_place, quantity, now_time))
      # Commit cursor
      mysql.connection.commit()

      # Close Connection
      cur.close()

      flash('Order successful', 'success')
      return render_template('pc.html', pc=products, form=form)
   if 'view' in request.args:
      product_id = request.args['view']
      curso = mysql.connection.cursor()
      curso.execute("SELECT * FROM products WHERE id=%s", (product_id,))
      product = curso.fetchall()

      if 'uid' in session:
         uid = session['uid']
         # Create cursor
         cur = mysql.connection.cursor()
         cur.execute("SELECT * FROM product_view WHERE user_id=%s AND product_id=%s", (uid, product_id))
         result = cur.fetchall()
         if result:
            now = datetime.datetime.now()
            now_time = now.strftime("%y-%m-%d %H:%M:%S")
            cur.execute("UPDATE product_view SET date=%s WHERE user_id=%s AND product_id=%s",
                        (now_time, uid, product_id))
         else:
            cur.execute("INSERT INTO product_view(user_id, product_id) VALUES(%s, %s)", (uid, product_id))
            mysql.connection.commit()
      return render_template('pc_desc.html', games=product)
   elif 'order' in request.args:
      product_id = request.args['order']
      curso = mysql.connection.cursor()
      curso.execute("SELECT * FROM products WHERE id=%s", (product_id,))
      product = curso.fetchall()
      return render_template('order_product.html', games=product, form=form)
   return render_template('pc.html', pc=products, form=form)

@app.route('/ps4', methods=['GET', 'POST'])
def ps4desc():
   form = OrderForm(request.form)
   # Create cursor
   cur = mysql.connection.cursor()
   # Get message
   values = 'ps4'
   cur.execute("SELECT * FROM products WHERE category=%s ORDER BY id ASC", (values,))
   products = cur.fetchall()
   # Close Connection
   cur.close()
   if request.method == 'POST' and form.validate():
      name = form.name.data
      mobile = form.mobile_num.data
      order_place = form.order_place.data
      quantity = form.quantity.data
      pid = request.args['order']
      now = datetime.datetime.now()
      week = datetime.timedelta(days=7)
      delivery_date = now + week
      now_time = delivery_date.strftime("%y-%m-%d %H:%M:%S")
      # Create Cursor
      curs = mysql.connection.cursor()
      if 'uid' in session:
         uid = session['uid']
         curs.execute("INSERT INTO orders(uid, pid, ofname, mobile, oplace, quantity, ddate) "
                      "VALUES(%s, %s, %s, %s, %s, %s, %s)",
                      (uid, pid, name, mobile, order_place, quantity, now_time))
      else:
         curs.execute("INSERT INTO orders(pid, ofname, mobile, oplace, quantity, ddate) "
                     "VALUES(%s, %s, %s, %s, %s, %s)",
                     (pid, name, mobile, order_place, quantity, now_time))
      # Commit cursor
      mysql.connection.commit()

      # Close Connection
      cur.close()

      flash('Order successful', 'success')
      return render_template('ps4.html', ps4=products, form=form)
   if 'view' in request.args:
      product_id = request.args['view']
      curso = mysql.connection.cursor()
      curso.execute("SELECT * FROM products WHERE id=%s", (product_id,))
      product = curso.fetchall()

      if 'uid' in session:
         uid = session['uid']
         # Create cursor
         cur = mysql.connection.cursor()
         cur.execute("SELECT * FROM product_view WHERE user_id=%s AND product_id=%s", (uid, product_id))
         result = cur.fetchall()
         if result:
            now = datetime.datetime.now()
            now_time = now.strftime("%y-%m-%d %H:%M:%S")
            cur.execute("UPDATE product_view SET date=%s WHERE user_id=%s AND product_id=%s",
                        (now_time, uid, product_id))
         else:
            cur.execute("INSERT INTO product_view(user_id, product_id) VALUES(%s, %s)", (uid, product_id))
            mysql.connection.commit()
      return render_template('ps4_desc.html', games=product)
   elif 'order' in request.args:
      product_id = request.args['order']
      curso = mysql.connection.cursor()
      curso.execute("SELECT * FROM products WHERE id=%s", (product_id,))
      product = curso.fetchall()
      return render_template('order_product.html', games=product, form=form)
   return render_template('ps4.html', ps4=products, form=form)


if __name__ == '__main__':
   app.run(debug = True)