#!/usr/bin/env python3


def swap(list, index_1, index_2):
    tmp = list[index_1]
    list[index_1] = list[index_2]
    list[index_2] = tmp


# The for loop in bubble sort is very waste, i know i just did it to check things
def bubble_sort(list):
    for elements in list:

        for idx, value in enumerate(list):
            if idx == len(list) - 1:
                continue

            elif list[idx] > list[idx + 1]:
                swap(list, idx, idx + 1)

            idx += 1

    return list


list = [1, 4, 2, 8, 342, 2, 1, 9, 3, 536]
print(bubble_sort(list))
