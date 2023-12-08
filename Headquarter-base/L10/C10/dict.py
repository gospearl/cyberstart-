# pip install pycryptodome
from Crypto.Cipher import AES
import base64

BLOCK_SIZE = 32

PADDING = '{'

# Encrypted text to decrypt
encrypted = "9l21XiUohS1j9kUx02KJNAkjw51pupGgiMlCkuVNEMo="

def decode_aes(c, e):
    return c.decrypt(base64.b64decode(e)).decode('latin-1').rstrip(PADDING)

secret = "password"

if secret[-1:] == "\n":
    print("Error, new line character at the end of the string. This will not match!")
elif len(secret.encode('utf-8')) >= 32:
    print("Error, string too long. Must be less than 32 bytes.")
else:
    # create a cipher object using the secret
    cipher = AES.new(secret + (BLOCK_SIZE - len(secret.encode('utf-8')) % BLOCK_SIZE) * PADDING, AES.MODE_ECB)

    # decode the encoded string
    decoded = decode_aes(cipher, encrypted)

    if decoded.startswith('FLAG:'):
        print("\n")
        print("Success: "+secret+"\n")
        print(decoded+"\n")
    else:
        print('Wrong password')
