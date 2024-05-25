# backend/app.py

# Import necessary libraries
from flask import Flask, request, jsonify
from models import Order
from utils import validate_order

app = Flask(__name__)

# Create a new order
@app.route('/create_order', methods=['POST'])
def create_order():
    data = request.get_json()
    
    # Validate the order data
    if not validate_order(data):
        return jsonify({'message': 'Invalid order data'}), 400
    
    # Create a new order
    new_order = Order(data['user_id'], data['size'], data['power_level'])
    new_order.save()
    
    return jsonify({'message': 'Order created successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True)