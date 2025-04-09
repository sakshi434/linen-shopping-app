from flask import Flask, send_from_directory, jsonify
import os

# Initialize Flask app
app = Flask(
    __name__,
    static_folder='../frontend',
    static_url_path='/'
)

# Serve the index.html
@app.route('/')
def serve_home():
    return send_from_directory(app.static_folder, 'index.html')

# Serve any static files (CSS, JS, images, etc.)
@app.route('/<path:path>')
def serve_static_file(path):
    full_path = os.path.join(app.static_folder, path)
    if os.path.isfile(full_path):
        return send_from_directory(app.static_folder, path)
    else:
        return jsonify({"error": "File not found"}), 404

# Run in debug mode only when not in production
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
