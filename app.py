from dicttoxml import dicttoxml
from flask import Flask, render_template, flash, request, session, jsonify, redirect, url_for, send_from_directory, g, make_response
from src.estimator import estimator
import ast
import datetime
import time
import logging
import json
app = Flask(__name__)


@app.route('/')
@app.route('/api/v1/on-covid-19/xml', methods = ['POST'])
def getInputData():
    dat = request.args.get('data')
    data = ast.literal_eval(dat)
    result = estimator(data)
    xml = dicttoxml(result, attr_type=False)
    print(type(xml))
    r = make_response(xml)
    r.headers["Content-Type"] = "application/xml; charset=utf-8"
    return r
    # xmlfile = open("students.xml", "w")
    # xmlfile.write(xml.decode())
    # xmlfile.close()
    # #xmlfile.mimetype = "text/xml"
    # xmlfile = open("students.xml", "r")
    # for x in xmlfile:
    #     if x == '<root>':
    #         x = ''
    #         return x
    #     else:
    #         return x
    
@app.route('/')
@app.route('/api/v1/on-covid-19', methods = ['POST'])
def getInputData2():    
    dat = request.args.get('data')
    data = ast.literal_eval(dat)
    result = jsonify(estimator(data))
    
    return result
@app.route('/')
@app.route('/api/v1/on-covid-19/json', methods = ['POST'])
def getInputData3():    
    dat = request.args.get('data')
    data = ast.literal_eval(dat)
    result = jsonify(estimator(data))
    
    return result

@app.route('/')

@app.before_request
def start_timer():
    g.start = time.time()


@app.after_request
def log_request(response):
    if request.path == '/favicon.ico':
        return response
    elif request.path.startswith('/static'):
        return response

    now = time.time()
    duration = round(now - g.start, 3)
    
    log_params = [
        (request.method),
        (request.path),
        (response.status_code),
        (duration),
        ("ms")]

    for ele in str(log_params[3]):
        if ele == '0' or ele == '.':
            log_params[3] = str(log_params[3]).replace(ele, "")
    
    log_params[3] = str(log_params[3])+str(log_params[4])
    log_params.pop(4)

    request_id = request.headers.get('X-Request-ID')
    if request_id:
        log_params.append(('request_id', request_id, 'yellow'))
    
    with open('log.txt', 'a') as logfile:        
        pp = json.dumps(log_params, separators=("\t\t","\n"))
        print(pp,file=logfile)
    logfile.close()
            
    return response

@app.route('/api/v1/on-covid-19/logs', methods=['GET'])
def getLog():
    test ='[]"'
    with open('log.txt', 'rt') as f:
        gg = f.read()
        gg = ''.join(' ' if ch in test else ch for ch in gg)
       
        return gg


if __name__=='__main__':
    app.run(debug=True, port=9000)