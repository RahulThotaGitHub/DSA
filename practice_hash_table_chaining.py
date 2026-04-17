#!/usr/bin/env python3

# This is an different(my) implementation of heap
# Important thing in hashmap is that we need to have a rough idea about the size of the table/list , since to find hash function we need acsii and mod it's sum to get it's index


class Hash_map:

    def __init__(self):
        self.max = 10
        self.table = [[] for i in range(self.max)]

    def get_hash(self, key):
        sum = 0
        for i in key:
            sum += ord(i)

        return sum % 10

    def add(self, key, value):
        arr = [key, value]
        self.table[self.get_hash(key)].append(arr)
        return f"Your value {value} is added"

    def get(self, key):
        our_child_list = self.table[self.get_hash(key)]
        for idx, value in enumerate(our_child_list):
            if value[0] == key:
                return f"The value of {key} is {value[1]}"

    def set(self, key, val):
        our_child_list = self.table[self.get_hash(key)]
        for idx, value in enumerate(our_child_list):
            if value[0] == key:
                value[1] = val
                return f"The value of {key} is now {value[1]}"


if __name__ == "__main__":
    hm = Hash_map()
    print(hm.get_hash("march 6"))
    print(hm.add("march 6", 190))
    print(hm.add("march 17", 290))
    print(hm.get("march 17"))
    print(hm.table)
    print(hm.set("march 17", 300))
    print(hm.table)
