from Crypto.Cipher import AES
import base64

BLOCK_SIZE = 32
PADDING = '{'

def decode_aes(c, e):
    return c.decrypt(base64.b64decode(e)).decode('latin-1').rstrip(PADDING)

def decrypt_with_wordlist(encrypted, wordlist):
    for password in wordlist:
        password = password.strip()  # Remove leading/trailing whitespaces
        if len(password.encode('utf-8')) < BLOCK_SIZE:
            password_bytes = password.encode('utf-8')
            padding_bytes = PADDING.encode('utf-8')
            padded_password = password_bytes + (BLOCK_SIZE - len(password_bytes) % BLOCK_SIZE) * padding_bytes
            cipher = AES.new(padded_password, AES.MODE_ECB)

            try:
                decoded = decode_aes(cipher, encrypted)
                print(f"Decrypted with password '{password}': {decoded}")
            except Exception as e:
                print(f"Decryption failed with password '{password}': {str(e)}")

    print("Decryption attempted with all passwords in the wordlist.")

# Example usage
encrypted_string = "xpd4OA7GZYDfn4lTMJW/EEqgp26BlgjxsTonc1Elcgo="
wordlist_path = "words.txt"

with open(wordlist_path, "r") as wordlist_file:
    wordlist = wordlist_file.readlines()

decrypt_with_wordlist(encrypted_string, wordlist)
