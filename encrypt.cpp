#include <openssl/aes.h>
#include <openssl/rand.h>
#include <iostream>
#include <cstring>

// Function to encrypt data
void encrypt(const unsigned char* plaintext, const unsigned char* key, unsigned char* ciphertext) {
    AES_KEY encryptKey;
    AES_set_encrypt_key(key, 128, &encryptKey);
    AES_encrypt(plaintext, ciphertext, &encryptKey);
}

// Function to decrypt data
void decrypt(const unsigned char* ciphertext, const unsigned char* key, unsigned char* plaintext) {
    AES_KEY decryptKey;
    AES_set_decrypt_key(key, 128, &decryptKey);
    AES_decrypt(ciphertext, plaintext, &decryptKey);
}

int main() {
    // Example key and plaintext
    unsigned char key[AES_BLOCK_SIZE] = {0}; // 128-bit key
    unsigned char plaintext[AES_BLOCK_SIZE] = "HelloWorld123456"; // Must be 16 bytes for AES
    unsigned char ciphertext[AES_BLOCK_SIZE];
    unsigned char decryptedtext[AES_BLOCK_SIZE];

    // Encrypt
    encrypt(plaintext, key, ciphertext);
    std::cout << "Encrypted text: ";
    for(int i = 0; i < AES_BLOCK_SIZE; i++) {
        std::cout << std::hex << static_cast<int>(ciphertext[i]);
    }
    std::cout << std::endl;

    // Decrypt
    decrypt(ciphertext, key, decryptedtext);
    std::cout << "Decrypted text: " << decryptedtext << std::endl;

    return 0;
}
