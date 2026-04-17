#!/usr/bin/env python3

# Initial Thinking of maining, you can see many mistakes , i realsied most of them but i missed this silly mistake i made at insert_at_beginning.


class Node:

    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoubleLinkedList:

    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, None, self.head)
        self.head = node

    def print(self):

        if self.head is None:
            print("There are no nodes")
            return

        string = ""

        while self.head:
            string += "<-----" + str(self.head.data) + "---->"
            self.head = self.head.prev

        print(string)

    def insert_at_value(self, value, dat):
        while self.head:
            if self.head.data == value:
                self.head.next = Node(
                    dat, self.head, self.head.next
                )  # Heres a mistake , i knew this was wrong but i understand what was wrong but wasn't able  to implement it or correct it .

            if self.head.next is None:
                break

            self.head = self.head.next


#     def insert_at_end(self, data):
#
#         if self.head is None:
#             self.head = Node(data, None)
#             return
#
#         itr = self.head
#
#         while itr.next:
#             itr = itr.next
#
#         itr.next = Node(data, None)
#
#     def insert_values(self, data_list):
#         self.head = None
#
#         for i in data_list:
#             self.insert_at_end(i)
#
#     def get_length(self):
#         count = 0
#         itr = self.head
#         while itr:
#             count += 1
#             itr = itr.next
#
#         return count
#
#     def remove_at(self, index):
#
#
#         if index < 0 or index > self.get_length():
#             raise Exception("Wrong Index")
#
#         if index == 0:
#             self.head = self.head.next
#             return
#
#         itr = self.head
#         count = 0
#         while itr :
#            if count == index -1:
#                itr.next = itr.next.next
#                break
#            itr = itr.next
#            count += 1
#
#
#     def insert_at(self, index, value):
#
#         if index<0 or index>self.get_length():
#             raise Exception("Wrong Index")
#
#
#         if index == 0:
#             self.head = Node(value, self.head)
#             return
#
#         itr = self.head
#         count = 0
#         while itr :
#            if count == index -1:
#                node = Node(value, itr.next)
#                itr.next = node
#                break
#
#            itr = itr.next
#            count += 1
#
#     def insert_after_value(self, value, value_add):
#
#         itr = self.head
#         while itr :
#            if itr.data == value:
#                node = Node(value_add, itr.next)
#                itr.next = node
#                break
#
#            itr = itr.next
#
#     def remove_by_value(self, data):
#         itr = self.head
#         count = 0
#         while itr:
#             if itr.data == data:
#                 self.remove_at(count )
#                 break
#
#             itr = itr.next
#             count += 1
#


if __name__ == "__main__":

    dll = DoubleLinkedList()
    dll.insert_at_beginning(10)
    dll.insert_at_beginning(20)
    dll.insert_at_beginning(40)
    dll.insert_at_value(20, 15)
    dll.print()
