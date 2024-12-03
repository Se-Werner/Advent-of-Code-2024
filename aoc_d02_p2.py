""""
Python Version: 3.11.0
Author: Sebastian Werner

This is the solution from the first Puzzle, but modified to fit the second Puzzle
"""


def report_evaluation(list_report, mode):

    current_level = list_report[0]
    rising_rating = 'N/A'
    for num_level in range(1, len(list_report)):
        gradient = list_report[num_level] - current_level
        if gradient > 0 and gradient <= 3:
            current_level = list_report[num_level]
        elif mode == 'recurve':
            list_corrected_var1 = list_report.copy()
            list_corrected_var2 = list_report.copy()
            del list_corrected_var1[num_level - 1]
            del list_corrected_var2[num_level]
            if report_evaluation(list_corrected_var1, 'final') or report_evaluation(list_corrected_var2, 'final'):
                rising_rating = True
                break
            else:
                rising_rating = False
                break
        else:
            rising_rating = False
            break

    if rising_rating == 'N/A':
        rising_rating = True

    current_level = list_report[0]
    decrease_rating = 'N/A'
    for num_level in range(1, len(list_report)):
        gradient = current_level - list_report[num_level]
        if gradient > 0 and gradient <= 3:
            current_level = list_report[num_level]
        elif mode == 'recurve':
            list_corrected_var1 = list_report.copy()
            list_corrected_var2 = list_report.copy()
            del list_corrected_var1[num_level - 1]
            del list_corrected_var2[num_level]
            if report_evaluation(list_corrected_var1, 'final') or report_evaluation(list_corrected_var2, 'final'):
                decrease_rating = True
                break
            else:
                decrease_rating = False
                break
        else:
            decrease_rating = False
            break

    if decrease_rating == 'N/A':

        decrease_rating = True

    if rising_rating or decrease_rating:
        return True
    else:
        return False


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
    list_report_rating.append(report_evaluation(report, 'recurve'))


solution_counter_1 = 0
for report_rating in list_report_rating:
    if report_rating:
        solution_counter_1 += 1


print(f'The solution for the second puzzle is: {solution_counter_1}')