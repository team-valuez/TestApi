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
        json = {"URL":"None","text":"None"}
        print(data)
        if((data['url'])[:5] == 'https'):
            json["URL"] = "not phishy"
        else:
            json['URL'] = "It seems like phishy"
        
        if('number' in json["text"] or "no." in json["text"]):
            json["text"] = "It seems like phishy"
        else:
            json["text"] = "Not sure, need verification from our server"
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