# feedback_routes.py

# Import necessary modules
from flask import Blueprint, request, jsonify
from models import Feedback
from utils import requires_auth

# Create a blueprint for feedback routes
feedback_bp = Blueprint('feedback_bp', __name__)

# Route to submit feedback
@feedback_bp.route('/submit_feedback', methods=['POST'])
@requires_auth
def submit_feedback():
    data = request.get_json()

    if 'user_id' not in data or 'message' not in data:
        return jsonify({'error': 'Missing user_id or message'}), 400

    user_id = data['user_id']
    message = data['message']

    # Save the feedback to the database
    new_feedback = Feedback(user_id=user_id, message=message)
    new_feedback.save()

    return jsonify({'message': 'Feedback submitted successfully'}), 200

# Route to get all feedback
@feedback_bp.route('/get_feedback', methods=['GET'])
@requires_auth
def get_feedback():
    feedback = Feedback.query.all()

    feedback_list = []
    for fb in feedback:
        feedback_list.append({'user_id': fb.user_id, 'message': fb.message})

    return jsonify(feedback_list), 200

# Route to get feedback by user
@feedback_bp.route('/get_feedback/<user_id>', methods=['GET'])
@requires_auth
def get_feedback_by_user(user_id):
    feedback = Feedback.query.filter_by(user_id=user_id).all()

    if not feedback:
        return jsonify({'message': 'No feedback found for this user'}), 404

    feedback_list = []
    for fb in feedback:
        feedback_list.append({'user_id': fb.user_id, 'message': fb.message})

    return jsonify(feedback_list), 200

# Route to delete feedback
@feedback_bp.route('/delete_feedback/<feedback_id>', methods=['DELETE'])
@requires_auth
def delete_feedback(feedback_id):
    feedback = Feedback.query.get(feedback_id)

    if not feedback:
        return jsonify({'message': 'Feedback not found'}), 404

    feedback.delete()

    return jsonify({'message': 'Feedback deleted successfully'}), 200

# End of feedback_routes.py