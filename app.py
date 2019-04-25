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
def loginpage():
   return redirect(url_for('login'))

@app.route('/home')
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

               return redirect(url_for('index'))

            else:
               flash('      Incorrect password, please try again!', 'danger')
               return render_template('login.html')

        else:
            flash('  Username not found, please try again', 'danger')
            # Close connection
            cur.close()
            return render_template('login.html')
    return render_template('login.html')

@app.route('/out')
def logout():
    return redirect(url_for('login'))


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
      street = request.form['street']
      city = request.form['city']
      pincode = request.form['pincode']
      cur = mysql.connection.cursor()
      cur.execute("INSERT INTO users(fname, lname, email, username, password, street, city, pincode) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)",(fname, lname, email, uname, password, street, city, pincode))
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
      return render_template('product_detail.html', games=product)
   elif 'cart' in request.args:
      product_id = request.args['cart']    
      if 'uid' in session:
         curso = mysql.connection.cursor()
         uid = session['uid']
         curso.execute("INSERT IGNORE INTO cart VALUES(%s, %s)", (uid, product_id,))
         mysql.connection.commit()
         print(uid)
         print(product_id)
         curso.execute("SELECT * FROM products WHERE id in (select pid from cart where uid = %s)", (uid,))
         product = curso.fetchall()
         flash('Product Added to Cart', 'success')
      return redirect(url_for('cart'))
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
      return render_template('product_detail.html', games=product)
   elif 'cart' in request.args:
      product_id = request.args['cart']    
      if 'uid' in session:
         curso = mysql.connection.cursor()
         uid = session['uid']
         curso.execute("INSERT IGNORE INTO cart VALUES(%s, %s)", (uid, product_id,))
         mysql.connection.commit()
         print(uid)
         print(product_id)
         curso.execute("SELECT * FROM products WHERE id in (select pid from cart where uid = %s)", (uid,))
         product = curso.fetchall()
         flash('Product Added to Cart', 'success')
      return redirect(url_for('cart'))
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
      return render_template('product_detail.html', games=product)
   elif 'cart' in request.args:
      product_id = request.args['cart']    
      if 'uid' in session:
         curso = mysql.connection.cursor()
         uid = session['uid']
         curso.execute("INSERT IGNORE INTO cart VALUES(%s, %s)", (uid, product_id,))
         mysql.connection.commit()
         print(uid)
         print(product_id)
         curso.execute("SELECT * FROM products WHERE id in (select pid from cart where uid = %s)", (uid,))
         product = curso.fetchall()
         flash('Product Added to Cart', 'success')
         curso.close()
      return redirect(url_for('cart'))
   return render_template('ps4.html', ps4=products, form=form)

@app.route('/cart', methods=['GET', 'POST'])
def cart():
   if 'uid' in session:
      curso = mysql.connection.cursor()
      uid = session['uid']
      curso.execute("SELECT * FROM products WHERE id in (select pid from cart where uid = %s)", (uid,))
      product = curso.fetchall()
      curso.close()

   if 'order' in request.args:
      if 'uid' in session:
         cur = mysql.connection.cursor()
         curs = mysql.connection.cursor()
         userid = session['uid']
         cur.execute("SELECT pid, pName, price, category, available FROM cart, products where id = pid AND uid = %s", (userid, ))
         cartrow = cur.fetchone()
         while cartrow is not None:
            curs.execute("INSERT INTO orders(pid, uid, pName, console, price) "
               "VALUES(%s, %s, %s, %s, %s)", 
               (cartrow['pid'], userid, cartrow['pName'], cartrow['category'], cartrow['price']))
            curs.execute("UPDATE products SET available = %s WHERE id = %s", (cartrow['available']-1, cartrow['pid'],))
            cartrow = cur.fetchone()          
            mysql.connection.commit()
         cur.execute("DELETE FROM cart where uid = %s", (userid,))
         mysql.connection.commit()
         cur.close()
         curs.close()
      return redirect(url_for('orders'))
   return render_template('cart.html', result=product)

@app.route('/orders')
def orders():
    curso = mysql.connection.cursor()
    if 'uid' in session:
      userid = session['uid']
      order_rows = curso.execute("SELECT * FROM orders WHERE uid = %s", (userid,))
      result = curso.fetchall()
    
    return render_template('all_orders.html', result=result)


@app.route('/search', methods=['POST', 'GET'])
def search():
    form = OrderForm(request.form)
    if 'q' in request.args:
      q = request.args['q']
      # Create cursor

      if q == '':
        flash('Enter a valid Search Value', 'danger')
        return redirect(url_for('index'))

      cur = mysql.connection.cursor()
      # Get message
      query_string = "SELECT * FROM products WHERE pName LIKE %s and category = %s ORDER BY id ASC"
      values = 'xbox'
      cur.execute(query_string, ('%' + q + '%', values,))
      xbox = cur.fetchall()
      values = 'pc'
      cur.execute(query_string, ('%' + q + '%', values,))
      pc = cur.fetchall()
      values = 'ps4'
      cur.execute(query_string, ('%' + q + '%', values,))
      ps4 = cur.fetchall()

      flash('Showing result for: ' + q, 'success')
      cur.close()

      return render_template('search.html', ps4=ps4, xbox=xbox, pc=pc , form=form)
    else:
      flash('Search again', 'danger')
      return render_template('search.html')



if __name__ == '__main__':
   app.run(debug = True)