from flask import Flask, render_template, request, redirect, url_for
import papermill as pm
import pandas as pd
import json
import plotly 
import plotly.express as px

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('search'))

@app.route('/search')
def search():
    return render_template('searchProduct.html')

@app.route('/searchProduct', methods = ['POST'])
def searchProduct():

    # productSKU
    productSKUInput = request.form['productSKU']
    print(productSKUInput)

    pm.execute_notebook('C:\\Users\\xuan4\\Desktop\\FYP\\Dreamshop\\Version 3\\Potential Customer List.ipynb',
    'C:\\Users\\xuan4\\Desktop\\FYP\\Dreamshop\\Version 3\\Potential Customer List Output.ipynb',
    parameters={'productSKU': productSKUInput})
  
    # vizualizeGraph
    pm.execute_notebook('C:\\Users\\xuan4\\Desktop\\FYP\\Dreamshop\\Version 3\\Graph Visualization based product SKU.ipynb',
                    'C:\\Users\\xuan4\\Desktop\\FYP\\Dreamshop\\Version 3\\Graph Visualization based product SKU Output.ipynb',
                    parameters={'productSKU': productSKUInput})

    df = pd.read_excel('C:\\Users\\xuan4\\Desktop\\FYP\\Dreamshop\\Version 3\\Graph Data of Product Quantity Sold.xlsx')
    fig = px.line(df, x=df['Month-Year'], y=df['Quantity'])
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    print(graphJSON)
    
    # productQty
    datasetQty = pd.read_excel('productQuantity.xlsx')
    qtyRow = datasetQty[datasetQty['SKU'] == productSKUInput]['Quantity'].values
    print(qtyRow[0])

    #potentialCustomer
    datasetCustomer = pd.read_excel('Potential Customer List.xlsx')

    return render_template('demand.html', productSKU=productSKUInput, productQty=qtyRow[0], datasetCustomer=datasetCustomer,
    graphJSON=graphJSON)