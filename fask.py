from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.json
    plaintext = data['plaintext']
    key = data['key']

    # Call the C++ encryption binary
    result = subprocess.run(['./encrypt_binary', plaintext, key], capture_output=True)
    ciphertext = result.stdout.decode('utf-8')

    return jsonify({'ciphertext': ciphertext})

if __name__ == '__main__':
    app.run(debug=True)
