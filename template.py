""""
Python Version: 3.11.0
Author: Sebastian Werner
"""

with open('test.txt', 'r') as file:
    input_content = file.readlines()

list_clean_lines = []
for line in input_content:
    clean_line = line.rstrip('\n')
    list_clean_lines.append(clean_line)
