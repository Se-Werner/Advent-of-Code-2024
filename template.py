""""
Python Version: 3.11.0
Author: Sebastian Werner
"""

with open('test.txt', 'r') as file:
    input_content = file.readlines()

list_input = []
for line in input_content:
    clean_line = line.rstrip('\n')
    list_input.append(clean_line)
