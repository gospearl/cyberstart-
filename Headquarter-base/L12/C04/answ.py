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
            # Encode the password to bytes
            password_bytes = password.encode('utf-8')

            # Encode the padding character to bytes
            padding_bytes = PADDING.encode('utf-8')

            # Pad the password if its length is less than BLOCK_SIZE
            padded_password = password_bytes + (BLOCK_SIZE - len(password_bytes) % BLOCK_SIZE) * padding_bytes

            # Create a cipher object using the padded password
            cipher = AES.new(padded_password, AES.MODE_ECB)

            # Try to decrypt the encrypted string
            try:
                decoded = decode_aes(cipher, encrypted)
                print(f"Decrypted with password '{password}': {decoded}")
                return decoded
            except Exception as e:
                # Decryption failed with this password
                pass

    print("Decryption unsuccessful with the provided wordlist.")
    return None

# Example usage
encrypted_string = "xpd4OA7GZYDfn4lTMJW/EEqgp26BlgjxsTonc1Elcgo="
wordlist_path = "words.txt"

with open(wordlist_path, "r") as wordlist_file:
    wordlist = wordlist_file.readlines()

decrypt_with_wordlist(encrypted_string, wordlist)
