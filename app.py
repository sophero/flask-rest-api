from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
  { 'name': 'DC',
    'items': [
      {
        'name': 'Maryjuana',
        'price': '60.00'
      }
    ]
  }
]

# POST /store {name:}
@app.route('/store', methods=['POST'])
def create_store():
  request_data = request.get_json() # I don't like how request is just mysteriously there without you declaring it like you would in Node. Nice to have learned these principles in JavaScript.
  new_store = {
    'name': request_data['name'],
    'items': []
  }
  stores.append(new_store)
  return jsonify(new_store) # Need to use jsonify! otherwise you're returning a dictionary and you need to return a string. json is a string... wow I totally forgot. JSONView lyf
  


# GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
  pass

@app.route('/store')
def get_stores():
  return jsonify({'stores': stores})

# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store():
  pass



app.run(port=2401)