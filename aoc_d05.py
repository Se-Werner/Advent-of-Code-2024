""""
Python Version: 3.11.0
Author: Sebastian Werner
"""
import math

with open('aoc_d05_input.txt', 'r') as file:
    input_content = file.readlines()

list_input = []
data_flag = False
page_orders = []
raw_first_pages = []
rule_list = []
for line in input_content:
    clean_line = line.rstrip('\n')
    if len(clean_line) > 2 and data_flag:
        pages = clean_line.split(',')
        page_orders.append(pages)
    elif len(clean_line) > 2 and not data_flag:
        rule = clean_line.split('|')
        raw_first_pages.append(rule[0])
        rule_list.append(rule)
    else:
        data_flag = True

first_pages = set(raw_first_pages)

comply_lists = []
not_comply_list = []
for pages in page_orders:
    comply_flag = True
    for page in range(1, len(pages)):
        if pages[page] in first_pages:
            for rule in rule_list:
                if pages[page] == rule[0]:
                    if rule[1] in pages[0:page]:
                        if comply_flag:
                            not_comply_list.append(pages)
                            comply_flag = False


    if comply_flag:
        comply_lists.append(pages)


solution_counter_1 = 0
for good_pages in comply_lists:
    solution_counter_1 += int(good_pages[math.floor(len(good_pages)/2)])

print(f'The first solution is: {solution_counter_1}')


# Part 2
# ---------------------------------------------------------------


num_dict = {}
for number in first_pages:
    follower = []
    for rule in rule_list:
        if rule[0] == number:
            follower.append(rule[1])

    num_dict[number] = follower

solved_pages = []
for pages in not_comply_list:
    for dex in range(1, len(pages)):
        # print(dex, len(pages), pages)
        if pages[dex] in first_pages:
            # print(pages[dex])
            for slice_dex in range(0, dex):
                # print(pages, dex)
                if pages[slice_dex] in num_dict[pages[dex]]:
                    # print(pages[slice_dex])
                    pages = pages[0:slice_dex] + [pages[dex]] + pages[slice_dex:dex] + pages[dex + 1:]
                    break
    # print(pages)
    solved_pages.append(pages)

# print(solved_pages)

solution_counter_2 = 0
for good_pages in solved_pages:
    solution_counter_2 += int(good_pages[math.floor(len(good_pages)/2)])
    print(solution_counter_2)

print('')
print(f'The solution to the second Puzzle is: {solution_counter_2}')