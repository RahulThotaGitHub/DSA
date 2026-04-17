#!/usr/bin/env python3

def swap(list,idx1,idx2):
    list[idx1],list[idx2]=list[idx2],list[idx1]


def partition(list):
    pivot = list[0]
    j = len(list)
    i = 0
    while i<j:
        i +=1
        while list[i]<=pivot:
            i +=1
        j -=1
        while list[j]>pivot:
            j -=1
        if i<j:
            swap(list,i,j)

    swap(list, 0, j)

    return j

def quick_sort(list):
    if 1<len(list):
        p = partition(list)    
        quick_sort(list[0:p+1])    
        quick_sort(list[p+1:len(list)])    

    return list

list = [10, 16,8,12,15,6, 3,9,5]
quick_sort(list)
print(list)






