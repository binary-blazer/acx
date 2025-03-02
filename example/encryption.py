import os
import random

def generate_key(length):
    """Generates a random key with a given length."""
    return os.urandom(length)

def chaotic_permutation(key):
    """Generates a chaotic permutation of the key."""
    indices = list(range(len(key)))
    random.shuffle(indices)
    permuted_key = bytes([key[i] for i in indices])
    return permuted_key, indices

def inverse_permutation(data, indices):
    """Restores the original order of the data."""
    restored = bytearray(len(data))
    for i, idx in enumerate(indices):
        restored[idx] = data[i]
    return bytes(restored)

def encrypt(plaintext):
    """Encrypts the message using the chaotic method."""
    plaintext_bytes = plaintext.encode()
    key = generate_key(len(plaintext_bytes))
    permuted_key, indices = chaotic_permutation(key)
    
    encrypted = bytes([p ^ k for p, k in zip(plaintext_bytes, permuted_key)])
    return encrypted, key, indices

text = "AQC is a great encryption method!"
encrypted, key, indices = encrypt(text)

print("Original:", text)
print("Encrypted:", encrypted)