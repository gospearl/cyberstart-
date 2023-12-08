import subprocess

for i in range(10001):
    # Format the number as a 4-digit string with leading zeros
    num_str = f'{i:04}'

    # Run the program-x86 with the formatted number as an argument
    command = ['./program-x86', num_str]

    # Execute the command
    subprocess.run(command)
