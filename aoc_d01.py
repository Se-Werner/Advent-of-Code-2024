""""
Python Version: 3.11
Author: Sebastian Werner
"""

with open('aoc_d01_input.txt', 'r') as file:
    input_content = file.readlines()

list_sites_a = []
list_sites_b = []
for line in input_content:
    clean_line = line.rstrip('\n')
    split_line = clean_line.split('   ')
    # print(split_line)
    list_sites_a.append(split_line[0])
    list_sites_b.append(split_line[1])

list_sites_a.sort()
list_sites_b.sort()

result_counter_1 = 0
for x in range(len(list_sites_a)):
    if int(list_sites_a[x]) >= int(list_sites_b[x]):
        cur_value = int(list_sites_a[x]) - int(list_sites_b[x])
    elif int(list_sites_b[x]) > int(list_sites_a[x]):
        cur_value = int(list_sites_b[x]) - int(list_sites_a[x])
    else:
        print('Warning: Error size comparison')

    result_counter_1 += cur_value

print(f'Result of puzzle 1 is:  {result_counter_1}')

# --------------------------------------------------------------------------------
# Second Puzzle

sim_score = 0
for left_id in list_sites_a:
    double_counter = 0
    for right_id in list_sites_b:
        if left_id == right_id:
            double_counter += 1

    sim_score += double_counter * int(left_id)

print(f'\nResult of second puzzle is: {sim_score}')
