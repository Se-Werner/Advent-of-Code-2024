""""
Python Version: 3.11.0
Author: Sebastian Werner
"""
from aoc_d03 import solution_counter_2


def find_m(coords, vector):

    new_y_pos = coords[0] + vector[0]
    new_x_pos = coords[1] + vector[1]

    if input_lines[new_y_pos][new_x_pos] == 'M':
        if find_a(coords, vector):
            return True
        else:
            return False
    else:
        return False


def find_a(coords, vector):
    new_y_pos = coords[0] + 2 * vector[0]
    new_x_pos = coords[1] + 2 * vector[1]

    if input_lines[new_y_pos][new_x_pos] == 'A':
        if find_s(coords, vector):
            return True
        else:
            return False
    else:
        return False


def find_s(coords, vector):
    new_y_pos = coords[0] + 3 * vector[0]
    new_x_pos = coords[1] + 3 * vector[1]

    if input_lines[new_y_pos][new_x_pos] == 'S':
        return True
    else:
        return False


def find_x(coord):
    '''
    Finds the position of m's and relays them to the find_xs() function to look for opposing s
    :param coord:
    :return: boolan value
    '''
    y = coord[0]
    x = coord[1]

    # print(y, x)
    cross_counter = 0
    for vector in VECTORS:
        if input_lines[y+vector[0]][x+vector[1]] == 'M':
            # print(input_lines[y+vector[0]][x+vector[1]])
            if input_lines[y+vector[0] * -1][x+vector[1] * -1]== 'S':
                # print(input_lines[y+vector[0] * -1][x+vector[1] * -1])
                cross_counter += 1


    # print(cross_counter)
    if cross_counter == 2:
        return True
    elif 0 <= cross_counter <= 1:
        return False
    else:
        print(f'Error cross counter {cross_counter}')


with open('aoc_d04_input.txt', 'r') as file:
    input_content = file.readlines()

input_lines = []
for line in input_content:
    clean_line = line.rstrip('\n')
    input_line = []
    for char in clean_line:
        input_line.append(char)

    input_lines.append(input_line)


solution_list = []
for y_pos in range(0, len(input_lines)):
    line_summary = []
    for x_pos in range(0, len(input_lines[y_pos])):
        if input_lines[y_pos][x_pos] == 'X':
            char_summary = []
            if y_pos < 3:
                if x_pos < 3:
                    # top_left
                    char_summary.append(find_m((y_pos, x_pos), (0, 1)))
                    char_summary.append(find_m((y_pos, x_pos), (1, 1)))
                    char_summary.append(find_m((y_pos, x_pos), (1, 0)))
                elif x_pos + 4 > len(input_lines[y_pos]):
                    # top_right
                    char_summary.append(find_m((y_pos, x_pos), (1, 0)))
                    char_summary.append(find_m((y_pos, x_pos), (1, -1)))
                    char_summary.append(find_m((y_pos, x_pos), (0, -1)))
                else:
                    # top
                    char_summary.append(find_m((y_pos, x_pos), (0, 1)))
                    char_summary.append(find_m((y_pos, x_pos), (1, 1)))
                    char_summary.append(find_m((y_pos, x_pos), (1, 0)))
                    char_summary.append(find_m((y_pos, x_pos), (1, -1)))
                    char_summary.append(find_m((y_pos, x_pos), (0, -1)))
            elif y_pos + 4 > len(input_lines):
                if x_pos < 3:
                    # bottom_left
                    char_summary.append(find_m((y_pos, x_pos), (-1, 0)))
                    char_summary.append(find_m((y_pos, x_pos), (-1, 1)))
                    char_summary.append(find_m((y_pos, x_pos), (0, 1)))
                elif x_pos + 4 > len(input_lines[y_pos]):
                    # bottom_right
                    char_summary.append(find_m((y_pos, x_pos), (-1, 0)))
                    char_summary.append(find_m((y_pos, x_pos), (-1, -1)))
                    char_summary.append(find_m((y_pos, x_pos), (0, -1)))
                else:
                    # bottom
                    char_summary.append(find_m((y_pos, x_pos), (0, 1)))
                    char_summary.append(find_m((y_pos, x_pos), (-1, 1)))
                    char_summary.append(find_m((y_pos, x_pos), (-1, 0)))
                    char_summary.append(find_m((y_pos, x_pos), (-1, -1)))
                    char_summary.append(find_m((y_pos, x_pos), (0, -1)))
            elif x_pos < 3:
                # left
                char_summary.append(find_m((y_pos, x_pos), (-1, 0)))
                char_summary.append(find_m((y_pos, x_pos), (-1, 1)))
                char_summary.append(find_m((y_pos, x_pos), (0, 1)))
                char_summary.append(find_m((y_pos, x_pos), (1, 1)))
                char_summary.append(find_m((y_pos, x_pos), (1, 0)))
            elif x_pos + 4 > len(input_lines[y_pos]):
                # right
                char_summary.append(find_m((y_pos, x_pos), (-1, 0)))
                char_summary.append(find_m((y_pos, x_pos), (-1, -1)))
                char_summary.append(find_m((y_pos, x_pos), (0, -1)))
                char_summary.append(find_m((y_pos, x_pos), (1, -1)))
                char_summary.append(find_m((y_pos, x_pos), (1, 0)))
            else:
                # middle
                char_summary.append(find_m((y_pos, x_pos), (0, 1)))
                char_summary.append(find_m((y_pos, x_pos), (1, 1)))
                char_summary.append(find_m((y_pos, x_pos), (1, 0)))
                char_summary.append(find_m((y_pos, x_pos), (1, -1)))
                char_summary.append(find_m((y_pos, x_pos), (0, -1)))
                char_summary.append(find_m((y_pos, x_pos), (-1, -1)))
                char_summary.append(find_m((y_pos, x_pos), (-1, 0)))
                char_summary.append(find_m((y_pos, x_pos), (-1, 1)))


            for char_case in char_summary:
                # print(char_case)
                line_summary.append(char_case)

    for line_case in line_summary:
        solution_list.append(line_case)


solution_counter_1 = 0
for x in solution_list:
    if x:
        # print(x)
        solution_counter_1 += 1


print(f'The first solution is: {solution_counter_1}')


# Part 2
# -----------------------------------------------------------------

VECTORS = ((-1,1), (1,1), (1,-1), (-1,-1))

solution_counter_2 = 0
for y_pos in range(1, len(input_lines)-1):
    for x_pos in range(1, len(input_lines)-1):

        if input_lines[y_pos][x_pos] == 'A':
            if find_x((y_pos, x_pos)):
                solution_counter_2 += 1


print('-')
print(f'The solution to the second Puzzle is: {solution_counter_2}')