# ACX (Advanced Chaotic XOR) Encryption Method

## Overview

ACX is a highly secure encryption method that combines the principles of the One-Time Pad (OTP) with a chaotic key permutation to provide robust encryption. It is designed to be practically unbreakable, leveraging the perfect secrecy of OTP with an added layer of complexity through the key permutation process. This encryption technique is intended for use in scenarios where maximum security is needed and where the key exchange and management systems are reliable.

## Key Aspects of ACX Encryption

### One-Time Pad (OTP) Foundation

- OTP provides perfect encryption by using a randomly generated key that is the same length as the message. The message is encrypted by performing a bitwise XOR operation with each byte of the key and the corresponding byte of the plaintext.
- OTP is theoretically unbreakable if the key is truly random, kept secret, and used only once.

### Chaotic Key Permutation

- To increase security, ACX introduces a chaotic permutation of the randomly generated OTP key.
- The key is shuffled using a randomly generated permutation sequence (essentially a random reordering of the key's indices). This ensures that even if an attacker obtains the key, they will not be able to decrypt the message unless they know the exact permutation used.
- The permutation is pseudo-chaotic: it is generated using random processes but can be reproducible if the same seed or key generation process is used. This unpredictability significantly enhances the security of the encryption.

### XOR Encryption

- The core encryption step in ACX is still the XOR operation, which is used to combine the plaintext with the permuted key.
- XOR is efficient, fast, and provides strong resistance to classical cryptanalysis techniques. The result of XORing the plaintext with the permuted key is the ciphertext, which appears as random noise without the correct key and permutation sequence.

### Decryption Process

- To decrypt the message, the recipient must possess both the original OTP key and the permutation sequence.
- The decryption begins by reversing the chaotic permutation to restore the original key order using the stored permutation indices.
- Once the original key is restored, the XOR operation is applied again between the ciphertext and the restored key to retrieve the plaintext.

### Key Management

- ACX relies on secure key management and secure exchange of both the OTP key and the permutation sequence. The key must be the same length as the plaintext and be completely random.
- Key secrecy and key reuse avoidance are critical. The key should never be used for more than one encryption to maintain the perfect security provided by OTP.
- The permutation sequence must be securely shared along with the key, as it is necessary to restore the original key order for decryption.

## Security of ACX

### Perfect Security with OTP

- ACX is built on the foundation of OTP, which provides perfect security as long as the key is random, never reused, and kept secret. Without access to the key, an attacker cannot decrypt the message, even if they have infinite computational resources.

### Increased Complexity with Chaotic Permutation

- The introduction of a chaotic permutation significantly enhances the security. Even if an attacker manages to get hold of the key, they would also need to figure out how the key was permuted in order to decrypt the message. This introduces an additional layer of complexity and prevents the key from being useful without the permutation sequence.

### Resistance to Classical Attacks

- Since the method uses the XOR operation and introduces a chaotic layer through the key permutation, the encryption is highly resistant to traditional cryptanalytic attacks (e.g., frequency analysis, known-plaintext attacks).

## Example

Below is an example of encrypting a message using the ACX encryption method. The original message is "ACX is a great encryption method!" and the encrypted output is shown in hexadecimal format.

```shell
b'\x15\xb6\x99lr\xc8\x16\x90\x81r\x1dGi\xf8\x02\n\x98`"DF\x8d\xd8S\xca\x1aR\xdc,\xd4\xc6\x98\x1e'
```
