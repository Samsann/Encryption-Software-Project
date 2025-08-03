from flask import Flask, request, jsonify, render_template_string
from encrypt_module import AESEncryption
import os

app = Flask(__name__)
aes_encryption = AESEncryption()

@app.route('/')
def index():
    """Serve the web interface"""
    with open('web_encrypt.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    return render_template_string(html_content)

@app.route('/encrypt', methods=['POST'])
def encrypt():
    """Encrypt the provided plaintext"""
    try:
        data = request.json
        plaintext = data.get('plaintext', '')
        key = data.get('key', '')
        
        if not plaintext or not key:
            return jsonify({'error': 'Both plaintext and key are required'}), 400
        
        # Use Python encryption module
        ciphertext = aes_encryption.encrypt(plaintext, key)
        
        return jsonify({'ciphertext': ciphertext})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/decrypt', methods=['POST'])
def decrypt():
    """Decrypt the provided ciphertext"""
    try:
        data = request.json
        ciphertext = data.get('ciphertext', '')
        key = data.get('key', '')
        
        if not ciphertext or not key:
            return jsonify({'error': 'Both ciphertext and key are required'}), 400
        
        # Use Python encryption module
        plaintext = aes_encryption.decrypt(ciphertext, key)
        
        return jsonify({'plaintext': plaintext})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("Starting Encryption Server...")
    print("Web interface available at: http://127.0.0.1:8080")
    print("API endpoints:")
    print("  POST /encrypt - Encrypt plaintext")
    print("  POST /decrypt - Decrypt ciphertext")
    app.run(debug=True, host='127.0.0.1', port=8080)
