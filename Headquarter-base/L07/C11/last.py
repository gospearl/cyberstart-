import urllib.request
import time

# Function to simulate decryption (replace this with your actual decryption logic)
def decrypt(text):
    # Simulating decryption delay
    time.sleep(1)
    return text[::-1]  # Just reversing the string as an example

# URL to retrieve revString
url = "https://chiquitooenterprise.com/password?code="
response = urllib.request.urlopen(url)
revString = response.read().decode('utf-8').strip()  # Assuming revString is a string

# Start measuring time
start_time = time.time()

# Decrypt the string
decrypted_string = decrypt(revString)

# Construct the URL with the decrypted string
link = "http://www.chiquitooenterprise.com/password"
answer = f"{link}?code={decrypted_string}"

# Perform the network request
response = urllib.request.urlopen(answer)
response = response.read()

# Print the response
print(response.decode('utf-8'))

# Calculate and print the time taken
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Time taken: {elapsed_time:.2f} seconds")

