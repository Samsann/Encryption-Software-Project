from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import hashlib
import base64
import os

class AESEncryption:
    def __init__(self):
        self.backend = default_backend()
    
    def _pad_data(self, data):
        """Pad data to 16-byte blocks"""
        pad_length = 16 - (len(data) % 16)
        return data + bytes([pad_length] * pad_length)
    
    def _unpad_data(self, padded_data):
        """Remove padding from data"""
        pad_length = padded_data[-1]
        return padded_data[:-pad_length]
    
    def _generate_key(self, password):
        """Generate a 32-byte key from password using SHA-256"""
        return hashlib.sha256(password.encode()).digest()
    
    def encrypt(self, plaintext, password):
        """Encrypt plaintext using AES encryption"""
        try:
            # Generate key from password
            key = self._generate_key(password)
            
            # Generate random IV
            iv = os.urandom(16)
            
            # Pad the plaintext
            padded_plaintext = self._pad_data(plaintext.encode())
            
            # Create cipher
            cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=self.backend)
            encryptor = cipher.encryptor()
            
            # Encrypt
            ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()
            
            # Combine IV and ciphertext, then encode to base64
            encrypted_data = iv + ciphertext
            return base64.b64encode(encrypted_data).decode()
            
        except Exception as e:
            raise Exception(f"Encryption failed: {str(e)}")
    
    def decrypt(self, encrypted_data, password):
        """Decrypt encrypted data using AES decryption"""
        try:
            # Generate key from password
            key = self._generate_key(password)
            
            # Decode from base64
            encrypted_bytes = base64.b64decode(encrypted_data.encode())
            
            # Extract IV and ciphertext
            iv = encrypted_bytes[:16]
            ciphertext = encrypted_bytes[16:]
            
            # Create cipher
            cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=self.backend)
            decryptor = cipher.decryptor()
            
            # Decrypt
            padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
            
            # Remove padding
            plaintext = self._unpad_data(padded_plaintext)
            
            return plaintext.decode()
            
        except Exception as e:
            raise Exception(f"Decryption failed: {str(e)}")

# For command line testing
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) == 3:
        aes = AESEncryption()
        plaintext = sys.argv[1]
        password = sys.argv[2]
        
        try:
            encrypted = aes.encrypt(plaintext, password)
            print(encrypted)
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Usage: python encrypt_module.py <plaintext> <password>")
