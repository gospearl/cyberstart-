import socket

# Specify the target IP address and port range
target_ip = "services.cyberprotection.agency"
start_port = 19000
end_port = 20000

# Loop through the specified port range
for port in range(start_port, end_port + 1):
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Set a timeout for the connection attempt (adjust as needed)
        s.settimeout(1)

        # Attempt to connect to the target
        s.connect((target_ip, port))

        # Print a message if the connection is successful
        print(f"Connection to {target_ip}:{port} successful!")

        # Close the socket
        s.close()

    except (socket.timeout, ConnectionRefusedError):
        # Handle timeout or connection refusal (optional)
        print(f"Connection to {target_ip}:{port} failed.")

# Print a final message after the loop completes
print("Port scanning completed.")
