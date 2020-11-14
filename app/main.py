from flask import Flask
import json
from os.path import join, dirname

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_json():

    with open(join(dirname(__file__), 'input', 'data.json')) as f:
        data = json.load(f)
    return data


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
