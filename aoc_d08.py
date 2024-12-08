""""
Python Version: 3.11.0
Author: Sebastian Werner
"""


# support functions
# ---------------------------------------------------------------------

def calc_antinodes(first_coord, second_coord):
    # print(first_coord, second_coord)

    y_pos_1 = first_coord[0] - (second_coord[0] - first_coord[0])
    x_pos_1 = first_coord[1] - (second_coord[1] - first_coord[1])

    y_pos_2 = second_coord[0] + (second_coord[0] - first_coord[0])
    x_pos_2 = second_coord[1] + (second_coord[1] - first_coord[1])

    coord_list = []
    if 0 <= y_pos_1 < grid_height and 0 <= x_pos_1 < grid_width:
        coord_list.append([y_pos_1, x_pos_1])

    if 0 <= y_pos_2 < grid_height and 0 <= x_pos_2 < grid_width:
        coord_list.append([y_pos_2, x_pos_2])

    return coord_list


def updated_antinode(first_coord, second_coord):

    dif_y = second_coord[0] - first_coord [0]
    dif_x = second_coord[1] - first_coord [1]

    coord_list = []
    first_flag = True
    old_y, old_x = first_coord[0], first_coord[1]
    while first_flag:
        new_y = old_y + dif_y
        new_x = old_x + dif_x
        if 0 <= new_y < grid_height and 0 <= new_x < grid_width:
            coord_list.append([new_y, new_x])
            old_y, old_x = new_y, new_x
        else:
            first_flag = False

    second_flag = True
    old_y, old_x = second_coord[0], second_coord[1]
    while second_flag:
        new_y = old_y - dif_y
        new_x = old_x - dif_x
        if 0 <= new_y < grid_height and 0 <= new_x < grid_width:
            coord_list.append([new_y, new_x])
            old_y, old_x = new_y, new_x
        else:
            second_flag = False

    return coord_list






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
            first_node = dict_input[frequency][antenna]
            second_node = dict_input[frequency][counterpart]

            for antinode in calc_antinodes(first_node, second_node):
                if antinode not in solution_list:
                    solution_list.append(antinode)


solution_counter = len(solution_list)
print(f'The first solution is: {solution_counter}')


# Part 2
# -----------------------------------------------------------------------

for frequency in dict_input.keys():
    for antenna in range(0, len(dict_input[frequency])-1):
        for counterpart in range(antenna+1, len(dict_input[frequency])):
            first_node = dict_input[frequency][antenna]
            second_node = dict_input[frequency][counterpart]

            for antinode in updated_antinode(first_node, second_node):
                if antinode not in solution_list:
                    solution_list.append(antinode)

solution_counter_2 = len(solution_list)
print(f'Second Solution is: {solution_counter_2}')