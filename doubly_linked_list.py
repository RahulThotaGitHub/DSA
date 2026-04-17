#!/usr/bin/env python3


class Node:

    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoubleLinkedList:

    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        if self.head == None:
            node = Node(data, None, self.head)
            self.head = node
        else:
            node = Node(data, None, self.head)
            self.head.prev = node
            self.head = node

    def print(self):

        if self.head is None:
            print("There are no nodes")
            return

        string = ""

        while self.head:
            string += "<-----" + str(self.head.data) + "---->"
            self.head = self.head.next

        print(string)

    def insert_at_value(self, value, dat):
        while self.head:
            if self.head.data == value:
                node = Node(dat, self.head, self.head.next)
                if node.next:
                    node.next.prev = node
                self.head.next = node

            if self.head.next is None:
                break
            self.head = self.head.next

        while self.head:
            if self.head.prev is None:
                break
            self.head = self.head.prev


if __name__ == "__main__":

    dll = DoubleLinkedList()
    dll.insert_at_beginning(10)
    dll.insert_at_beginning(20)
    dll.insert_at_beginning(40)
    dll.insert_at_beginning(50)
    dll.insert_at_value(20, 15)
    dll.insert_at_value(50, 45)
    dll.insert_at_value(40, 35)
    dll.print()
