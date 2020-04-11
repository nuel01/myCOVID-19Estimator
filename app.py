
from flask import Flask, render_template, flash, request, session, jsonify, redirect, url_for, send_from_directory
from src.estimator import estimator
import ast
import logging
app = Flask(__name__)

@app.route('/')
@app.route('/api/v1/on-covid-19', methods = ['POST'])
def getInputData():

    dat = request.args.get('data')
    print(type(dat))
    data = ast.literal_eval(dat)
    print(type(data))


    result = jsonify({'':estimator(data)})   

    return result
@app.route('/')
def index():
    return "<h1> Welcome here </h1>"

#@app.route('/')
#@app.route('/api/v1/on-covid-19/logs')
#def createLog():



if __name__=='__main__':
    app.run(debug=True, host="0.0.0.0")