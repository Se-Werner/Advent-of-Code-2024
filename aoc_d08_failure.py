""""
Python Version: 3.11.0
Author: Sebastian Werner
Comment: Overcomplicated solution that did not work. Off by 1
"""
# import math

# support functions
# ---------------------------------------------------------------------

def calc_slope(first_coord, second_coord):
    y_delta = first_coord[0] - second_coord[0]
    x_delta = first_coord[1] - second_coord[1]

    slope = y_delta / x_delta

    return slope


def calc_intercept(first_coord, slope):
    intercept = first_coord[0] - (slope * first_coord[1])

    return intercept


def calc_distance(first_coord, second_coord):
    y_diff = abs(first_coord[0] - second_coord[0])
    x_diff = abs(first_coord[1] - second_coord[1])

    # distance = math.sqrt(y_diff + x_diff)
    distance = y_diff + x_diff

    return distance


def calc_position(slope, intercept, x_pos):
    y_pos = slope * x_pos + intercept

    return y_pos

# Process Input
# ---------------------------------------------------------------------

with open('aoc_d08_input.txt', 'r') as file:
    input_content = file.readlines()

dict_input = {}
for line in range(0, len(input_content)):
    clean_line = input_content[line].rstrip('\n')
    for char in range(0, len(clean_line)):
        if clean_line[char] != '.' and clean_line[char] != '#':
            if clean_line[char] in dict_input.keys():
                dict_input[clean_line[char]].append([line, char])
            else:
                dict_input[clean_line[char]] = [[line, char]]
        elif clean_line[char] == '#':
            # print([line, char])
            pass


grid_height = len(input_content)
grid_width = len(input_content[0].rstrip('\n'))
# print(dict_input)

# Main Program
# ---------------------------------------------------------------------

solution_list = []
for frequency in dict_input.keys():
    for antenna in range(0, len(dict_input[frequency])-1):
        for counterpart in range(antenna+1, len(dict_input[frequency])):
            line_slope = calc_slope(dict_input[frequency][antenna], dict_input[frequency][counterpart])
            line_intercept = calc_intercept(dict_input[frequency][antenna], line_slope)
            # print('slopes: ', line_slope, line_intercept)

            for x in range(0, grid_width):
                y_position = calc_position(line_slope, line_intercept, x)
                if y_position < dict_input[frequency][antenna][0] or y_position > dict_input[frequency][counterpart][0]:

                    if 0 <= y_position < grid_height and (y_position % 1 > 0.9 or y_position % 1 == 0):
                        dist_ant1 = calc_distance(dict_input[frequency][antenna], [y_position, x])
                        dist_ant2 = calc_distance(dict_input[frequency][counterpart], [y_position, x])
                        # print('pos ', y_position, x)
                        # print('dist ', dist_ant1, dist_ant2)
                        if not (dist_ant1 == 0 or dist_ant2 == 0):
                            if 1.99 < dist_ant1 / dist_ant2 < 2.01 or 1.99 < dist_ant2 / dist_ant1 < 2.01:
                                if [y_position, x] not in solution_list:
                                    solution_list.append([y_position, x])

solution_counter = len(solution_list)
# print(solution_list)
print(f'The first solution is: {solution_counter}')