from django.test import TestCase
import re

# Create your tests here.

def split_location(location):
    new_list = re.split('[A-Z]+', location)
    new_list.remove('')
    return new_list


look_start_range = input('START: ')
look_end_range   = input('END: ')


collection_list = [
    {
        'R': 1,
        'L': 2,
        'C': 1
    },
    {
        'R': 1,
        'L': 2,
        'C': 2
    },
    {
        'R': 1,
        'L': 2,
        'C': 3
    },
    {
        'R': 1,
        'L': 2,
        'C': 4
    },
    {
        'R': 1,
        'L': 2,
        'C': 5
    },
    {
        'R': 1,
        'L': 2,
        'C': 6
    },
    {
        'R': 1,
        'L': 2,
        'C': 7
    },
    {
        'R': 1,
        'L': 2,
        'C': 8
    },
    {
        'R': 1,
        'L': 2,
        'C': 9
    },
    {
        'R': 1,
        'L': 2,
        'C': 10
    }
]


new_collection_list = []


look_y = split_location(look_start_range)
look_x = split_location(look_end_range)


for i in collection_list:
    for key, value in i.items():
        if (i['R'] == int(look_y[0]) and i['R'] == int(look_x[0])) and (i['L'] == int(look_y[1]) and i['L'] == int(look_x[1])) and i['C'] >= int(look_y[2]) and i['C'] <= int(look_x[2]):
            layout_char = f'R{i["R"]}L{i["L"]}C{i["C"]}'
            if layout_char not in new_collection_list:
                new_collection_list.append(layout_char)


print('LOCATION LIST: ' + str(new_collection_list))
