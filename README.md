# 🔒 Encryption Software Project

A comprehensive encryption and decryption software with web interface and Python backend, ensuring data privacy and integrity using AES encryption.

## 🌟 Features

- **Secure AES Encryption**: Uses industry-standard AES encryption with CBC mode
- **Web Interface**: User-friendly HTML interface for encryption/decryption
- **REST API**: Flask-based API for programmatic access
- **Password-based Encryption**: Generates secure keys from user passwords using SHA-256
- **Cross-platform**: Pure Python implementation works on Windows, macOS, and Linux

## 🏗️ Project Structure

```
Encryption/
├── encrypt_module.py      # Core AES encryption/decryption module
├── app.py                # Flask web server and API
├── web_encrypt.html      # Web interface
├── encrypt.cpp           # C++ implementation (reference)
└── README.md            # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.12+ (configured in virtual environment)
- Flask
- cryptography library

### Installation & Setup

1. **Clone the repository** (already done):
   ```bash
   git clone https://github.com/Samsann/Encryption-Software-Project
   cd Encryption
   ```

2. **Install dependencies** (already configured):
   ```bash
   pip install flask cryptography
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Access the web interface**:
   Open your browser and go to: `http://127.0.0.1:8080`

## 🎯 Usage

### Web Interface

1. **Encryption**:
   - Enter your plaintext in the text area
   - Provide a secure password/key
   - Click "🔐 Encrypt"
   - Copy the encrypted result

2. **Decryption**:
   - Paste the encrypted text
   - Enter the same password used for encryption
   - Click "🔓 Decrypt"
   - View the original plaintext

### API Endpoints

#### Encrypt Data
```bash
POST /encrypt
Content-Type: application/json

{
    "plaintext": "Hello, World!",
    "key": "mySecretPassword"
}
```

Response:
```json
{
    "ciphertext": "base64_encoded_encrypted_data"
}
```

#### Decrypt Data
```bash
POST /decrypt
Content-Type: application/json

{
    "ciphertext": "base64_encoded_encrypted_data",
    "key": "mySecretPassword"
}
```

Response:
```json
{
    "plaintext": "Hello, World!"
}
```

### Command Line Usage

```bash
python encrypt_module.py "Hello, World!" "mySecretPassword"
```

## 🔧 Technical Details

- **Encryption Algorithm**: AES-256 in CBC mode
- **Key Derivation**: SHA-256 hash of user password
- **Padding**: PKCS7 padding for block alignment
- **IV**: Random 16-byte initialization vector for each encryption
- **Encoding**: Base64 encoding for safe text transmission

## 🛡️ Security Features

- Strong AES-256 encryption
- Random IV generation for each encryption
- Secure key derivation from passwords
- Proper padding implementation
- Error handling for invalid inputs

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

**Samsann** - [GitHub Profile](https://github.com/Samsann)

---

**Note**: This project has been updated to use pure Python implementation instead of C++ for better cross-platform compatibility and easier setup. 
