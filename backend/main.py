from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder='../frontend', static_url_path='/')

# Route to serve frontend files (index.html, etc.)
@app.route('/')
def serve_home():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_file(path):
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    app.run(debug=True)
