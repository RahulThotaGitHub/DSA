#!/usr/bin/env python3

def swap(list,idx1,idx2):
    list[idx1],list[idx2]=list[idx2],list[idx1]

def insertion_sort(list):
    for idx, value in enumerate(list):
        if idx == 0:
            continue
        while list[idx-1]>list[idx]:
            swap(list, idx-1, idx)
            idx -= 1
            if idx ==0:
                break
    return list
            

        
list = [1,521,2,7,33,4,6,2,1,8,21,4,2,1,4,6,1,9]
print(insertion_sort(list))








