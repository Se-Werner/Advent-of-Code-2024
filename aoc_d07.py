""""
Python Version: 3.11.0
Author: Sebastian Werner
Comment: Second part was solved with code from first puzzle with minimal adjustment
"""

def calc_step(first, second_list):

    list_results = []
    if len(second_list) > 1:
        value_add = int(first) + int(second_list[0])
        list_results += calc_step(value_add, second_list[1:])

        value_mult = int(first) * int(second_list[0])
        list_results += calc_step(value_mult, second_list[1:])

        value_comb = str(first) + str(second_list[0])                   # added for second part
        list_results += calc_step(value_comb, second_list[1:])          # added for second part

    elif len(second_list) == 1:
        list_results.append(int(first) + int(second_list[0]))
        list_results.append(int(first) * int(second_list[0]))
        list_results.append(int(str(first) + str(second_list[0])))      # added for second part

    return list_results


with open('aoc_d07_input.txt', 'r') as file:
    input_content = file.readlines()

list_targets = []
list_inputs = []
for line in input_content:
    clean_line = line.rstrip('\n')
    first_cut = clean_line.split(':')
    list_targets.append(int(first_cut[0]))
    second_cut = first_cut[1].split(' ')
    list_inputs.append(second_cut[1:])



result_sum = 0
check_list = []
for calib in range(0, len(list_targets)):
    if list_targets[calib] in calc_step(int(list_inputs[calib][0]), list_inputs[calib][1:]):
        result_sum += list_targets[calib]
        check_list.append(list_targets[calib])


print(f'Second solution is: {result_sum}')