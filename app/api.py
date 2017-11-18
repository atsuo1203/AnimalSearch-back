import json

from flask import request, redirect, url_for, make_response, jsonify

from app import app
from app.request import scientific_name


@app.route('/', methods=['POST'])
def show_wiki_name():
    data = json.loads(request.data.decode('utf-8'))
    wiki_name = data['name']
    text = scientific_name(wiki_name)
    response = {'name': text}
    return make_response(jsonify(response))

