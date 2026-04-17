#!/usr/bin/env python3

class HashTableChain:

    def __init__(self):
        self.max_index = 100
        self.array = [ [] for i in range(self.max_index)]


    def hash(self, text):
        sum = 0
        for char in text:
            char = ord(char)
            sum += char
        return sum % self.max_index

# We can use __setitem__ , __getitem__ , in place of set_hash and get, this would give the benefit of directly calling array[key] to set and get value.
#
#    def set_hash(self, key, value):
#        index = self.hash(key)
#        self.array[index] = value
#
#    def get(self, key):
#        return self.array[self.hash(key)]
        
    def __setitem__(self, key, value):
            index = self.hash(key)
            found = False
            for idx, element in enumerate(self.array[index]):
                if element[0]==key and len(element)==2:
                    self.array[index][idx] = (key, value)
                found = True
                break
            if not found:
                self.array[index].append[(key, value)]

    def __getitem__(self, key):
        
            index = self.hash(key)
            for idx, element in enumerate(self.array[index]):
                if element[0] == key:
                    return element[1]
        


h = HashTable()
print(h.hash('march 6'))
#h.set_hash('march 1', 100321)
h['march 1'] = 100321
print(h.hash('march 1'))
#print(h.get('march 1'))
#print(h.get('march 6'))
print(h['march 1']) 
print(h['march 6']) 
