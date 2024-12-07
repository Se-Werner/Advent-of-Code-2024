""""
Python Version: 3.11.0
Author: Sebastian Werner
"""

def update_vector(vector):

    if vector == [-1, 0]:
        return [0, 1]
    elif vector == [0, 1]:
        return [1, 0]
    elif vector == [1, 0]:
        return [0, -1]
    elif vector == [0, -1]:
        return [-1, 0]
    else:
        print('Error Vector Update')

def check_loop(guard_dict, list_obstacles):
    global grid_height, grid_width
    guard_info = guard_dict.copy()
    on_map_flag = True
    step_counter = 0
    while on_map_flag and step_counter <= 100_000:
        old_pos = [guard_info['y_pos'], guard_info['x_pos']]
        old_vector = guard_info['vector']
        new_pos = [old_pos[0] + old_vector[0], old_pos[1] + old_vector[1]]
        # print(new_pos)
        if 0 <= new_pos[0] < grid_height and 0 <= new_pos[1] < grid_width:
            if new_pos in list_obstacles:
                guard_info['vector'] = update_vector(old_vector)
            else:
                guard_info['y_pos'] = new_pos[0]
                guard_info['x_pos'] = new_pos[1]
                step_counter += 1
        else:
            # print(new_pos)
            on_map_flag = False

    # print(step_counter, on_map_flag)
    if on_map_flag:
        return True
    else:
        return False


with open('aoc_d06_input.txt', 'r') as file:
    input_content = file.readlines()

global grid_height, grid_width

grid_height = len(input_content)
grid_width = len(input_content[0])

list_obstacles = []
for line in range(0, len(input_content)):
    clean_line = input_content[line].rstrip('\n')
    for char in range(0, len(clean_line)):
        if clean_line[char] == '#':
            list_obstacles.append([line, char])
        elif clean_line[char] == '^':
            dict_guard = {'y_pos': line, 'x_pos': char, 'vector': [-1, 0]}

'''
on_map_flag = True

list_visit = [[dict_guard['y_pos'], dict_guard['x_pos']]]
while on_map_flag:
    old_pos = [dict_guard['y_pos'], dict_guard['x_pos']]
    old_vector = dict_guard['vector']
    new_pos = [old_pos[0] + old_vector[0], old_pos[1] + old_vector[1]]
    if 0 <= new_pos[0] < grid_height and 0 <= new_pos[1] < grid_width:
        if new_pos in list_obstacles:
            dict_guard['vector'] = update_vector(old_vector)
        else:
            dict_guard['y_pos'] = new_pos[0]
            dict_guard['x_pos'] = new_pos[1]
            if new_pos not in list_visit:
                list_visit.append(new_pos)
    else:
        on_map_flag = False

solution_counter_1 = len(list_visit)

print(f'The first solution is: {solution_counter_1}')
'''

# Part 2
# ----------------------------------------

solution_counter_2 = 0
progress_counter = 1
max_counter = grid_width * grid_height
for y in range(0, grid_height):
    for x in range(0, grid_width):
        print(f'Check for Position {progress_counter} / {max_counter}')
        progress_counter += 1
        if [y, x] not in list_obstacles or not [y, x] == [dict_guard['y_pos'], dict_guard['x_pos']]:
            list_new_obstacles = list_obstacles.copy()
            list_new_obstacles.append([y, x])
            # print(list_new_obstacles)
            if check_loop(dict_guard, list_new_obstacles):
                solution_counter_2 += 1

print(f'\nSecond Solution is: {solution_counter_2}')