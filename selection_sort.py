#!/usr/bin/env python3



def swap(lst, a, b):
    lst[a],lst[b]=lst[b],lst[a]

def selection_sort(list):

    for i in range(len(list)):

         min = list[i]
         min_idx = i

         for idx, value in enumerate(list):
             if i>idx:
                 continue
             if min>value:
                 min = value
                 min_idx = idx

         swap(list, i, min_idx)   

    return list
    
list = [1,2,-1, 5,2,9,4,10,5,2,6,3,4,1,7,8]
print(selection_sort(list))


