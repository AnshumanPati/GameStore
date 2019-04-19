from flask import Flask, render_template, request
import sys

app = Flask(__name__)

@app.route('/',methods = ['POST', 'GET'])
def login():
	return render_template('login.html')


@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      ans = request.form.to_dict()
      #username = request.form['username']
      print(ans, file=sys.stderr)
      #print "LOL"
      # print username
      return render_template("result.html",result = result)

if __name__ == '__main__':
   app.run(debug = True)