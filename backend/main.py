from flask import Flask, request, jsonify
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials, auth, firestore

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests

# Initialize Firebase Admin SDK
cred = credentials.Certificate("firebase-config.json")  # Use the correct path to your config
firebase_admin.initialize_app(cred)

# Initialize Firestore DB
db = firestore.client()
users_ref = db.collection('users')

# Route to register a new user
@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        email = data['email']
        password = data['password']
        name = data.get('name', '')  # Optional name field

        # Create user in Firebase Authentication
        user_record = auth.create_user(email=email, password=password, display_name=name)

        # Store user info in Firestore
        users_ref.document(user_record.uid).set({
            'email': email,
            'name': name,
            'uid': user_record.uid
        })

        return jsonify({'message': 'User registered successfully!', 'uid': user_record.uid}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Route to verify an ID token (from frontend login)
@app.route('/verify-token', methods=['POST'])
def verify_token():
    try:
        data = request.get_json()
        id_token = data['idToken']

        # Verify ID token
        decoded_token = auth.verify_id_token(id_token)
        uid = decoded_token['uid']
        user_doc = users_ref.document(uid).get()

        if user_doc.exists:
            user_data = user_doc.to_dict()
            return jsonify({'message': 'Token verified', 'user': user_data}), 200
        else:
            return jsonify({'error': 'User not found'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 401

# Basic home route
@app.route('/')
def home():
    return "Firebase-Backed Flask API is running."

if __name__ == '__main__':
    app.run(debug=True)
