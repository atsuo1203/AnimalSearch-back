from flask import request, redirect, url_for, make_response, jsonify
import json


@app.route('/', methods=['GET'])
def show_users():
    results = []
    return make_response(jsonify(results))

