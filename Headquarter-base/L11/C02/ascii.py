data = """81
95
33
108
95
26
103
95
95
110
99
104
97
26
91
110
26
110
98
95
26
60
91
92
91
108
111
109
101
99
26
104
99
97
98
110
93
102
111
92
26
99
104
26
70
105
104
94
105
104
26
91
110
26
43
43
106
103
26
110
98
99
109
26
95
112
95
104
99
104
97
40"""

# Split the string into a list of strings
ascii_values = data.split('\n')

# Convert each string element to an integer
int_values = [int(value) for value in ascii_values]
for i in range(1,11):
    modified_values = [value + i for value in int_values]

    # Convert the modified integers to ASCII characters
    ascii_characters = ''.join(chr(value) for value in modified_values)

    print(ascii_characters)
