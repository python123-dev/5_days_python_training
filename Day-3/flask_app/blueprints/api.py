#Flask API - plain routes returning JSON via jsonify
#for a bigger project you'd reach for an extension like flask-restful or flask-smorest
#to get request parsing/serialization for free, but plain Flask is enough for a small API
from flask import Blueprint, jsonify, request
import models

api_bp = Blueprint('api', __name__, url_prefix='/api')


#GET /api/customers - list all customers as JSON
@api_bp.route('/customers', methods=['GET'])
def list_customers():
    return jsonify(models.get_all_customers())


#POST /api/customers - create a customer from a JSON body
@api_bp.route('/customers', methods=['POST'])
def create_customer():
    data = request.get_json()
    if not data or 'name' not in data or 'address' not in data:
        return jsonify({'error': 'name and address are required'}), 400
    new_id = models.add_customer(data['name'], data['address'])
    return jsonify(models.get_customer(new_id)), 201


#GET /api/customers/<id> - fetch a single customer
@api_bp.route('/customers/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    customer = models.get_customer(customer_id)
    if customer is None:
        return jsonify({'error': 'customer not found'}), 404
    return jsonify(customer)


#DELETE /api/customers/<id> - remove a customer
@api_bp.route('/customers/<int:customer_id>', methods=['DELETE'])
def remove_customer(customer_id):
    if models.get_customer(customer_id) is None:
        return jsonify({'error': 'customer not found'}), 404
    models.delete_customer(customer_id)
    return jsonify({'deleted': customer_id})
