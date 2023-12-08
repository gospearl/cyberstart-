# pip install pycryptodome
from Crypto.Cipher import AES
import base64

BLOCK_SIZE = 32
PADDING = '{'

# Encrypted text to decrypt
encrypted = "9l21XiUohS1j9kUx02KJNAkjw51pupGgiMlCkuVNEMo="

def decode_aes(c, e):
    return c.decrypt(base64.b64decode(e)).decode('latin-1').rstrip(PADDING)

# Read passwords from the dictionary file
with open('words.txt', 'r') as file:
    passwords = [line.strip() for line in file]

for secret in passwords:
    if secret[-1:] == "\n":
        print("Error, new line character at the end of the string. This will not match!")
    elif len(secret.encode('utf-8')) >= 32:
        print("Error, string too long. Must be less than 32 bytes.")
    else:
        # encode the secret string into bytes
        secret_bytes = secret.encode('utf-8')

        # create a cipher object using the secret
        cipher = AES.new(secret_bytes + (BLOCK_SIZE - len(secret_bytes) % BLOCK_SIZE) * PADDING.encode('utf-8'), AES.MODE_ECB)

        # decode the encoded string
        decoded = decode_aes(cipher, encrypted)

        if decoded.startswith('FLAG:'):
            print("\n")
            print("Success: "+secret+"\n")
            print(decoded+"\n")
            break  # Stop the loop if a correct password is found
        else:
            print(f'Wrong password: {secret}')
