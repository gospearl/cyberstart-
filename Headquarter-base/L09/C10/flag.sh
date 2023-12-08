#!/bin/bash

for ((i=0; i<=10000; i++)); do
    # Format the number as a 4-digit string with leading zeros
    num_str=$(printf "%04d" $i)

    # Run the program-x86 with the formatted number as an argument
    ./program-x86 $num_str
done

