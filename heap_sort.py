#!/usr/bin/env python3

def max(list, num1,num2):
    if list[num1]>list[num2]:
        return num1
    else:
        return num2

def swap(list, idx1, idx2):
    list[idx1], list[idx2]= list[idx2], list[idx1]  

def heapify(list, size):
    for idx in range(size-1, -1 , -1):

        i = idx + 1
        par_idx = int(i/2) - 1
        child_1 = 2*i - 1
        child_2 = 2*i

        if idx>=0:

            if child_1<= size-1 and child_2<= size-1:
                if list[idx]< list[max(list,child_1, child_2)]:
                    swap(list, idx, max(list,child_1, child_2))

            elif child_1<= size-1: 
                if list[idx]< list[child_1]:
                    swap(list, idx, child_1)

    return list


def heap_sort(list):
    size = len(list)
    while size>0:
        heapify(list, size)
        swap(list, 0, size-1)
        size -= 1
    
    return list



lst = [10, 20, 15, 12, 40, 25, 18] 
#if index + 1 is i then, idx = i - 1
#1st child is 2i, then , idx = 2i - 1 
#2nd child is 2i+1, then , idx = 2i 
#then the parent is at [i/2] then, idx = [i/2] - 1
print(lst)
print(heap_sort(lst))




