from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/searchProduct')
def index():
    return redirect(url_for('searchProduct'))

@app.route('/searchProduct', method = ['POST'])
def searchProduct():
    # user = request.form['productSKU']
    # print(user)
    return render_template('demand.html')