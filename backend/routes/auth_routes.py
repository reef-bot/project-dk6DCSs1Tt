# backend/routes/auth_routes.py

from flask import Blueprint, request, jsonify
from models import User
from utils import verify_password, generate_token

auth_routes = Blueprint('auth_routes', __name__)

@auth_routes.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'Username already exists'}), 400

    user = User(username=username, password=password)
    user.save()

    return jsonify({'message': 'User registered successfully'}), 201

@auth_routes.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    user = User.query.filter_by(username=username).first()

    if not user or not verify_password(password, user.password):
        return jsonify({'error': 'Invalid username or password'}), 401

    token = generate_token(user.id)
    return jsonify({'token': token}), 200

@auth_routes.route('/profile', methods=['GET'])
def profile():
    user_id = request.headers.get('user_id')

    if not user_id:
        return jsonify({'error': 'User ID is required'}), 400

    user = User.query.filter_by(id=user_id).first()

    if not user:
        return jsonify({'error': 'User not found'}), 404

    return jsonify({'username': user.username}), 200

# End of auth_routes.py