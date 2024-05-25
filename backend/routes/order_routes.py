# backend/routes/order_routes.py

from flask import Blueprint, request, jsonify
from models import Order
from utils import verify_user

order_routes = Blueprint('order_routes', __name__)

@order_routes.route('/create_order', methods=['POST'])
def create_order():
    data = request.json
    user_id = data.get('user_id')
    size = data.get('size')
    power_level = data.get('power_level')

    if not user_id or not size or not power_level:
        return jsonify({'error': 'Missing required fields'}), 400

    if not verify_user(user_id):
        return jsonify({'error': 'Unauthorized access'}), 401

    new_order = Order(user_id=user_id, size=size, power_level=power_level)
    new_order.save()

    return jsonify({'message': 'Order created successfully'}), 201

@order_routes.route('/get_orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    orders_list = [{'id': order.id, 'size': order.size, 'power_level': order.power_level} for order in orders]

    return jsonify({'orders': orders_list}), 200

@order_routes.route('/delete_order/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    order = Order.query.get(order_id)

    if not order:
        return jsonify({'error': 'Order not found'}), 404

    order.delete()

    return jsonify({'message': 'Order deleted successfully'}), 200

# End of order_routes.py
