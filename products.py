# import the packages required to create REST APIs with Flask.
from flask import Flask, jsonify, request
import json

# create flask app
app = Flask("Product Server")

# precreated products added to the list
products = [
    {'id': 143, 'name': 'Notebook', 'price': 5.49},
    {'id': 144, 'name': 'Black Marker', 'price': 1.99}
]

# Example request - http://localhost:5000/products
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

# Example request - http://localhost:5000/products/144 - with method GET
@app.route('/products/<id>', methods=['GET'])
def get_product(id):
    id = int(id)
    product = [x for x in products if x["id"] == id[0]]
    return jsonify(product)

# Example request - http://localhost:5000/products - with method POST
@app.route('/products', methods=['PUT'])
def add_product():
    products.append(request.get_json())
    return '', 201

# Example request - http://localhost:5000/products/144 - with method PUT
@app.route('/products/<id>', methods=['PUT'])
def update_product(id):
    id = int(id)
    update_product = json.loads(request.data)
    product = [x for x in products if x["id"] == id][0]
    for key, value in update_product.items():
        product[key] = value
    return '', 204

#  Example request - http://localhost:5000/products/144 - with method DELETE
@app.route('/products/<id>', methods=['DELETE'])
def remove_product(id):
    id = int(id)
    product = [x for x in products if x["id"] == id][0]
    products.remove(product)
    return '', 204

# start the flask app
if __name__ == '__main__':
    app.run(debug=True)