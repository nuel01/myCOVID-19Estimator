
from flask import Flask, render_template, flash, request, session, jsonify, redirect, url_for, send_from_directory
from src.estimator import estimator
import ast
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



if __name__=='__main__':
    app.run(debug=True, port=9000)