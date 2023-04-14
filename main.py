#!/usr/bin/env python
# encoding: utf-8

from flask import Flask, jsonify,request
app = Flask(__name__)

@app.route('/name')
def index():
    name = request.args.get('name')
    #email = request.args.get('email')
    return jsonify({'name': f'{name}'})
                    #'email': f'{email}'})
app.run()