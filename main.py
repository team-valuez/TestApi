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
    return jsonify({'name': f'{name}'})

@app.route('/names', methods=['POST'])
def process_json():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        data = request.get_json()
        json = {"URL":data['url'],"text":data["text"]}
        return jsonify(json)
    else:
        return 'Content-Type not supported!'

@app.route("/add")
def sum():
    n1 = int(request.args.get("n1"))
    n2 = int(request.args.get("n2"))
    return jsonify({"sum":f"{n1+n2}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0')