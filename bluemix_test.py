# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 14:41:17 2017

@author: Chandresh
"""

import os
from flask import Flask, jsonify, request
import logging
app = Flask(__name__)

port = int(os.getenv('VCAP_APP_PORT',8084))

def authoriseUser(request):
    logging.debug(request.headers)
    if(request.headers.get('apikey') == 'creativeai'):
        return True
    else:
        return False


@app.route('/', methods=['GET'])
def createAd():
    
    # first authenticate the user
    if(not authoriseUser(request)):
        return '{"error":"Invalid headers", "STATUS":"FAIL"}'
    else:
        return jsonify(STATUS="success")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
    
    
