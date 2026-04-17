#!/usr/bin/env python3


class Node:

    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):

        if self.head is None:
            print("There are no nodes")
            return

        string = ''
        
        while self.head:
            string +=   str(self.head.data) + "---->" 
            self.head = self.head.next
            
        print(string)

    def insert_at_end(self, data):

        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next
        
        itr.next = Node(data, None) 

    def insert_values(self, data_list):
        self.head = None
        
        for i in data_list:
            self.insert_at_end(i)
 
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        
        return count

    def remove_at(self, index):

        
        if index < 0 or index > self.get_length():
            raise Exception("Wrong Index")

        if index == 0:
            self.head = self.head.next 
            return

        itr = self.head
        count = 0
        while itr :
           if count == index -1:
               itr.next = itr.next.next
               break
           itr = itr.next
           count += 1
        

    def insert_at(self, index, value):

        if index<0 or index>self.get_length():
            raise Exception("Wrong Index")

 
        if index == 0:
            self.head = Node(value, self.head)
            return       

        itr = self.head
        count = 0
        while itr :
           if count == index -1:
               node = Node(value, itr.next)
               itr.next = node
               break

           itr = itr.next
           count += 1
        
    def insert_after_value(self, value, value_add):

        itr = self.head
        while itr :
           if itr.data == value:
               node = Node(value_add, itr.next)
               itr.next = node
               break

           itr = itr.next

    def remove_by_value(self, data):
        itr = self.head
        count = 0
        while itr:
            if itr.data == data:
                self.remove_at(count )
                break

            itr = itr.next
            count += 1
                


if __name__ == '__main__' :
    ll = LinkedList()
    print(ll.get_length())
    ll.insert_values(["banana"," orange", "grapes", "apple", "pineapple"])
    print(ll.get_length())
    ll.remove_at(3)
#    ll.print()
    ll.insert_at(1, "hello")
    ll.insert_at(1, 65)
    ll.insert_after_value("grapes", 77)
    ll.remove_by_value(77)
    ll.print()





