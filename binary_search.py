#!/usr/bin/env python3


def binary_search(arr, first_idx, last_idx, search_element):

    mid_idx = (first_idx + last_idx) // 2
    mid = arr[mid_idx]

    if search_element == mid:
        return f"The Element is present at index {mid_idx} and its value is {mid}"

    elif first_idx == mid_idx:
        return "Error:The element is not present in the list"

    elif search_element < mid:
        return binary_search(arr, first_idx, mid_idx - 1, search_element)

    elif search_element > mid:
        return binary_search(arr, mid_idx + 1, last_idx, search_element)


def binary(arr, search):
    l = len(arr) - 1
    return binary_search(arr, 0, l, search)


lst = [3, 6, 8, 12, 14, 17, 25, 29, 31, 36, 42, 47, 53, 55, 62]
print(binary(lst, 25))
