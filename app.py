from flask import Flask, jsonify, request, render_template

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

@app.route('/')
def home():
  return render_template('index.html')


#                    #
#   Store Endpoints  #
#                    #

# POST /store {name:}
@app.route('/store', methods=['POST'])
def create_store():
  request_data = request.get_json()
  new_store = {
    'name': request_data['name'],
    'items': []
  }
  stores.append(new_store)
  return jsonify(new_store) # Need to use jsonify! otherwise you're returning a dictionary and you need to return a string. json is a string... wow I totally forgot. JSONView lyf

# GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
  # iterate over stores
  for store in stores:
  # if the store name matches, return it
    if store['name'] == name:
      return jsonify(store)
  # if none match, return an error message
  return jsonify({ 'message': 'No stores found with name {}'.format(name) })

# GET /stores
@app.route('/stores')
def get_stores():
  return jsonify({'stores': stores})

#                    #
#   Item Endpoints   #
#                    #

# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
  req_data = request.get_json()
  for store in stores:
    if store['name'] == name:
      new_item = {
        'name': req_data['name'],
        'price': req_data['price']
      }
      store['items'].append(new_item)
      return jsonify(new_item)
  return jsonify({ 'message': 'No store found with name {}'.format(name )})

# GET /store/<string:name>/items
@app.route('/store/<string:name>/items')
def get_items_in_store(name):
  for store in stores:
    if store['name'] == name:
      return jsonify({ 'items': store['items'] })
  return jsonify({ 'message': 'No store found with name {}'.format(name) })

if __name__ == '__main__':
  app.run(port=2401)