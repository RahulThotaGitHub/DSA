#!/usr/bin/env python3

#list = []
#for i in range(10):
#    list.append(i)
#print(list[0:5])
#def merge():
#
#
def merge(list_1,list_2):
    results=[]
    index_1 = 0
    index_2 = 0

#    for i in range(len(list_1)+len(list_2)): 
#        if list_1[index_1]<list_2[index_2] and index_1==len(list_1):
#            results.append(list_1[index_1])
#            index_1+=1
#        else:
#            results.append(list_2[index_2])
#            index_2+=1
#            if index_2==len(list_2): 
#                while index_1!=len(list_1):
#                    results.append(list_1[index_1])
#                    index_1+=1
#                break
    while index_1!=len(list_1) and index_2!=len(list_2):

        if list_1[index_1]<list_2[index_2]: 
            results.append(list_1[index_1])
            index_1+=1
        else:
            results.append(list_2[index_2])
            index_2+=1

    if index_1==len(list_1):
        for i in list_2[index_2:]:
            results.append(i)

    if index_2==len(list_2):
        for j in list_1[index_1:]:
            results.append(j)
        
                

    return results
             

def merge_sort(list):


    l = 0
    h = len(list)

    if l<h-1 :

        mid = (int)((l/2) + (h/2))

        list_1 = merge_sort(list[l:mid])
        list_2 = merge_sort(list[mid:h])

        return merge(list_1,list_2)

    else:
       return list
        
list = [1, 4, 6, 13, 2, 1, 2, 10, 2, 7, 4, 3, 123, 321, 0, 321, -1 , 21, 2,2 ,5,9,2,12,41]
print(merge_sort(list))

