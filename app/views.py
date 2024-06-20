from flask import Blueprint, jsonify

views_bp = Blueprint('views', __name__)

@views_bp.route('/api', methods=['GET'])
def api():
    return jsonify({"message": "Hello, World!"}), 200
