#!/usr/bin/env python3

list = [2200, 2350, 2600, 2130, 2190]
print(f" I spent {list[1]- list[0]} extra in feb when compared to jan") 
print(f" Total expense in first quarter is { list[0]+ list[2]+list[3]}")

for i in list:
    if i == 2000:
        print(" Yes i have spent exactly 2k in a month")

list.append(1980)
print("after adding june month: ", end="")
print(list)
print("after updating april month: ")
list[3] = list[3]-200
print(list)
