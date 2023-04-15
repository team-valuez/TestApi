#!/usr/bin/env python
# encoding: utf-8

from flask import Flask, jsonify,request
app = Flask(__name__)
#import os

@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})

@app.route('/name')
def nam():
    name = request.args.get('name')
    #email = request.args.get('email')
    return jsonify({'name': f'{name}'})
                    #'email': f'{email}'})

if __name__ == '__main__':
    app.run(host='0.0.0.0')