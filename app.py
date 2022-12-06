from flask import Flask, render_template, request, redirect, url_for
import papermill as pm

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('search'))

@app.route('/search')
def search():
    return render_template('searchProduct.html')

@app.route('/searchProduct', methods = ['POST'])
def searchProduct():
    productSKU = request.form['productSKU']
    print(productSKU)

    pm.execute_notebook('C:\\Users\\xuan4\\Desktop\\FYP\\Dreamshop\\Version 3\\Potential Customer List.ipynb',
    'C:\\Users\\xuan4\\Desktop\\FYP\\Dreamshop\\Version 3\\Potential Customer List Output.ipynb',
    parameters={'productSKU': productSKU})
    
    return render_template('demand.html', productSKU=productSKU)