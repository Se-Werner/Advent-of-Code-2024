""""
Python Version: 3.11.0
Author: Sebastian Werner
"""
import re

with open('aoc_d03_input.txt', 'r') as file:
    input_content = file.readlines()


input_string = input_content[0]


list_functions = re.findall(r'mul\(\d{1,3},\d{1,3}\)', input_string)


solution_counter_1 = 0
for function in list_functions:
    # print(function)
    split_numbers = function.lstrip('mul(').rstrip(')').split(',')
    solution_counter_1 += int(split_numbers[0]) * int(split_numbers[1])

print(f'The solution is: {solution_counter_1}')
print('\n')


# Part 2
# -----------------------------------------------------

dict_function = {}

for mul_func in re.finditer(r'mul\(\d{1,3},\d{1,3}\)', input_string):
    dict_function[str(mul_func.span()[0])] = mul_func.group(0)

for do_func in re.finditer(r'do\(\)', input_string):
    dict_function[str(do_func.span()[0])] = do_func.group(0)

for dont_func in re.finditer(r"don't\(\)", input_string):
    dict_function[str(dont_func.span()[0])] = dont_func.group(0)


work_flag = True
solution_counter_2 = 0
for step in range(0, len(input_string)):
    str_step = str(step)
    if str_step in dict_function.keys():
        if dict_function[str_step] == 'do()':
            work_flag = True
        elif dict_function[str_step] == "don't()":
            work_flag = False
        elif work_flag:
            split_numbers = dict_function[str_step].lstrip('mul(').rstrip(')').split(',')
            solution_counter_2 += int(split_numbers[0]) * int(split_numbers[1])


print(f'The second solution is: {solution_counter_2}')