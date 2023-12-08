#!/bin/bash

target="services.cyberprotection.agency"  # Replace with the actual target address
start_port=14000
end_port=15000

for ((port=$start_port; port<=$end_port; port++)); do
    nc -zvw 1 $target $port  # -z for scanning, -v for verbose output, -w 1 for timeout
done

