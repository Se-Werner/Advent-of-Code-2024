""""
Python Version: 3.11.0
Author: Sebastian Werner
"""

def report_rising(list_report):
    current_level = list_report[0]

    for num_level in range(1, len(list_report)):
        gradient = list_report[num_level] - current_level
        if gradient > 0 and gradient <= 3:
            current_level = list_report[num_level]
        else:
            return False

    return True


def report_decrease(list_report):
    current_level = list_report[0]

    for num_level in range(1, len(list_report)):
        gradient = current_level - list_report[num_level]
        if gradient > 0 and gradient <= 3:
            current_level = list_report[num_level]
        else:
            return False

    return True


with open('aoc_d02_input.txt', 'r') as file:
    input_content = file.readlines()


list_clean_lines = []
for line in input_content:
    clean_line = line.rstrip('\n')
    list_string_input = clean_line.split(' ')
    list_int_input = []
    for level in list_string_input:
        list_int_input.append(int(level))
    list_clean_lines.append(list_int_input)


list_report_rating = []
for report in list_clean_lines:
    if report[0] < report[-1]:
        list_report_rating.append(report_rising(report))
    elif report[0] > report[-1]:
        list_report_rating.append(report_decrease(report))
    else:
        list_report_rating.append(False)


solution_counter_1 = 0
for report_rating in list_report_rating:
    if report_rating:
        solution_counter_1 += 1


print(f'The solution for the first puzzle is: {solution_counter_1}')