import json

from flask import Flask
from flask_cors import CORS
from flask import request, make_response, jsonify

from animal_search.request import scientific_name

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET', 'POST'])
def show_wiki_name():
    if request.method == 'POST':
        data = json.loads(request.data.decode('utf-8'))
        wiki_name = data['name']
        word_list = scientific_name(wiki_name)
        response = {'name': word_list}
        return make_response(jsonify(response))

    return '値を送ってください'


if __name__ == '__main__':
    app.run()
