import json

from flask import request,make_response, jsonify
from flask_cors import cross_origin

from app import app
from app.request import scientific_name


@app.route('/', methods=['POST'])
@cross_origin()
def show_wiki_name():
    data = json.loads(request.data.decode('utf-8'))
    wiki_name = data['name']
    word_list = scientific_name(wiki_name)
    response = {'name': word_list}
    return make_response(jsonify(response))

