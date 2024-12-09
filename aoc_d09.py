""""
Python Version: 3.11.0
Author: Sebastian Werner
"""

with open('aoc_d09_input.txt', 'r') as file:
    input_content = file.readlines()

list_input = []
for line in input_content:
    clean_line = line.rstrip('\n')

'''
file_id_counter = 0
disk_layout = []
for read_pos in range(0, len(clean_line)):
    if read_pos == 0 or read_pos % 2 == 0:
        for x in range(0, int(clean_line[read_pos])):
            disk_layout.append(file_id_counter)

        file_id_counter += 1

    else:
        for y in range(0, int(clean_line[read_pos])):
            disk_layout.append('.')

# print(disk_layout)


for right_block in range(-1, -1 * len(disk_layout), -1):
    print(f'Check Position {-1 * right_block} / {len(disk_layout)}')
    if disk_layout[right_block] != '.':
        for left_block in range(0, len(disk_layout) + right_block):
            if disk_layout[left_block] == '.':
                disk_layout[left_block] = disk_layout[right_block]
                disk_layout[right_block] = '.'
                break

# print(disk_layout)


solution_counter_1 = 0
for block in range(0, len(disk_layout)):
    if disk_layout[block] != '.':
        solution_counter_1 += disk_layout[block] * block

print(f'The first solution is: {solution_counter_1}')
'''

# Part 2
# ---------------------------------------------------------------------------

file_id_counter = 0
disk_layout = []
for read_pos in range(0, len(clean_line)):
    if read_pos == 0 or read_pos % 2 == 0:
        disk_layout.append({'type': 'file', 'file_id': file_id_counter, 'size': int(clean_line[read_pos])})
        file_id_counter += 1

    else:
        disk_layout.append({'type': 'space', 'size': int(clean_line[read_pos])})

print(disk_layout)

for right_block in range(-1, -1 * len(disk_layout), -1):
    print(f'Progress: {round((-1 * right_block)/len(disk_layout)*100, 2)}')
    if disk_layout[right_block]['type'] == 'file':
        file_id = disk_layout[right_block]['file_id']
        file_size = disk_layout[right_block]['size']
        file_copy = disk_layout[right_block].copy()
        for left_block in range(0, len(disk_layout) + right_block):
            if disk_layout[left_block]['type'] == 'space' and disk_layout[left_block]['size'] >= file_size:
                disk_layout.insert(left_block, file_copy)
                disk_layout[left_block + 1]['size'] -= file_size
                disk_layout[right_block]['type'] = 'space'
                break

'''
list_empty_blocks = []
for clean_block in range(0, len(disk_layout)):
    if disk_layout[clean_block]['type'] == 'space' and disk_layout[clean_block]['size'] == 0:
        list_empty_blocks.append(clean_block)
        
for empty in list_empty_blocks:
    del(disk_layout)
    
'''

position_counter = 0
solution_counter_2 = 0
for block in disk_layout:
    if block['type'] == 'file':
        for x in range(0, block['size']):
            solution_counter_2 += position_counter * block['file_id']
            position_counter += 1
    else:
        position_counter += block['size']

print(f'The second solution is: {solution_counter_2}')