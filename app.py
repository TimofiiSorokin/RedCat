from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/redcatdb'
db = SQLAlchemy(app)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tittle = db.Column(db.String(120), unique=False)
    descriptions = db.Column(db.String(120), unique=False)

    def __init__(self, tittle, descriptions):
        self.tittle = tittle
        self.descriptions = descriptions


client = app.test_client()

tutorials = [
    {
        'id': 1,
        'tittle': 'First Web ',
        'descriptions': 'WWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
    },
    {
        'id': 2,
        'tittle': 'Second Web',
        'descriptions': 'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBB'
    }
]


@app.route('/')
@app.route('/hello')
def hello_world():
    a = 'Hello World!'
    bbb = a
    return bbb


# to see in route
@app.route('/web', methods=['GET'])
def get_list():
    return jsonify(tutorials)


# to add in route
@app.route('/web', methods=['POST'])
def update_list():
    new_one = request.json
    tutorials.append(new_one)
    return jsonify(tutorials)


# for change in route by id
@app.route('/web/<int:tutorial_id>', methods=['PUT'])
def update_tutorial(tutorial_id):
    item = next((x for x in tutorials if x['id'] == tutorial_id), None)
    params = request.json
    if not item:
        return {'message': 'No tutorials with this id'}, 400
    item.update(params)
    return item


@app.route('/web/<int:tutorial_id>', methods=['DELETE'])
def delete_tutorial(tutorial_id):
    idx, _ = next((x for x in enumerate(tutorials) if x[1]['id'] == tutorial_id), (None, None))
    tutorials.pop(idx)
    return '', 204


if __name__ == '__main__':
    app.debug = True
    # db.create_all()
    # app.run(host="localhost", port=8000, debug=True)
    app.run()
