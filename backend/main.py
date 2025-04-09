from flask import Flask, request, jsonify
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials, firestore
import os

# Initialize Firebase using Application Default Credentials (from GOOGLE_APPLICATION_CREDENTIALS)
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred)

# Firestore client
db = firestore.client()

# Flask app setup
app = Flask(__name__)
CORS(app)

# Example route to add user data
@app.route('/add_user', methods=['POST'])
def add_user():
    try:
        data = request.json
        user_id = data.get('uid')
        if not user_id:
            return jsonify({'error': 'User ID (uid) is required'}), 400
        db.collection('users').document(user_id).set(data)
        return jsonify({'success': True, 'message': 'User added'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Example route to get user data
@app.route('/get_user/<user_id>', methods=['GET'])
def get_user(user_id):
    try:
        user_ref = db.collection('users').document(user_id)
        user_doc = user_ref.get()
        if user_doc.exists:
            return jsonify(user_doc.to_dict()), 200
        else:
            return jsonify({'error': 'User not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Entry point
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
