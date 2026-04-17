#!/usr/bin/env python3

class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
class LinkedList:

    def __init__(self):
        self.node = None


    def insert_node(self, data):
        node = Node(data, self.node)
        self.node = node

    def print(self):

        if self.node is None:
            print("Linked List is empty")
            return
    
        string = ''

        while self.node:
            string += str(self.node.data) + "---->"
            self.node = self.node.next

        print(string)


if __name__ == '__main__':
    ll = LinkedList()
    Ll = LinkedList()
    ll.insert_node(20)
    ll.insert_node(50)
    Ll.insert_node(50)
    ll.print()
    Ll.insert_node(90)
    Ll.print()



