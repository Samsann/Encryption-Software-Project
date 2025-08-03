<!-- Use this file to provide workspace-specific custom instructions to Copilot. For more details, visit https://code.visualstudio.com/docs/copilot/copilot-customization#_use-a-githubcopilotinstructionsmd-file -->

# Encryption Software Project Instructions

This is a Python-based encryption/decryption software project with the following components:

## Project Structure
- `encrypt_module.py`: Core AES encryption module using the cryptography library
- `app.py`: Flask web server providing REST API and web interface
- `web_encrypt.html`: Frontend web interface for encryption/decryption
- `encrypt.cpp`: Reference C++ implementation (not currently used)

## Key Technologies
- **Python**: Main implementation language
- **Flask**: Web framework for API and serving web interface
- **cryptography**: Python library for AES encryption
- **HTML/CSS/JavaScript**: Frontend web interface

## Coding Standards
- Use AES-256 encryption with CBC mode
- Implement proper PKCS7 padding
- Generate random IVs for each encryption
- Use SHA-256 for key derivation from passwords
- Encode encrypted data in base64 for safe transmission
- Include comprehensive error handling
- Follow RESTful API principles
- Write secure, production-ready code

## Security Considerations
- Always use cryptographically secure random number generation
- Implement proper key derivation functions
- Validate all inputs thoroughly
- Handle encryption/decryption errors gracefully
- Never log or expose sensitive data like keys or plaintext

## Flask Application Structure
- Serve web interface at root route `/`
- Provide `/encrypt` and `/decrypt` POST endpoints
- Return JSON responses with proper error handling
- Use appropriate HTTP status codes
