#!/usr/bin/env python3

# Here the data is not chaining like in linkedlist or something like that , we can see there's recursion in here so we can use recursive methods.


class BinarySearchTree:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if self.data == data:
            return
        if self.data > data:
            if self.left is None:
                self.left = BinarySearchTree(data)
            else:
                self.left.add_child(data)
        else:
            if self.right is None:
                self.right = BinarySearchTree(data)
            else:
                self.right.add_child(data)

    def search(self, dat):
        if self.data == dat:
            return True
        # This self.left check is important it says if it exists do this , without this we will get an error.
        while self.data != None:
            if self.data > dat:
                if self.left:
                    return self.left.search(dat)
                else:
                    return False

            elif self.data < dat:
                if self.right:
                    return self.right.search(dat)
                else:
                    return False

        return "no such element"

    def print(self):
        # this is wrong
        # while self.data:
        #     print(self.data)
        #     self.data = self.left

        elements = []

        if self.left:
            elements += self.left.print()

        elements.append(self.data)

        if self.right:
            elements += self.right.print()

        return elements

    # Fix max function , everything else works except this
    def max(self):
        val = 0
        while self.right:
            val = self.data
            self.right = self.right.right

        return val

    def delete(self, dat):
        # if self.data == dat:
        #    if self.left is none and self.right is none:
        #        self.data = none
        #        return f"{dat} is deleted"

        #    elif self.left is none:
        #        if self.right:
        #            self.data = self.right.right

        #    elif self.right is none:
        #        if self.left:
        #            self.data = self.left.left

        # elif self.data < dat:
        #    if self.right:
        #        return self.right.delete(dat)

        # elif self.data > dat:
        #    if self.left:
        #        return self.left.delete(dat)

        if self.data == dat:
            return f"{dat} is root node , you can't delete the root node"

        if self.data > dat:
            if self.left:
                if self.left.data == dat:
                    if self.left.left is None and self.left.right is None:
                        self.left = None
                        return f"{dat} is deleted"

                    if self.left.left is None:
                        if self.left.right:
                            self.left = self.left.right
                            return f"{dat} is deleted"

                    elif self.left.right is None:
                        if self.left.left:
                            self.left = self.left.left
                            return f"{dat} is deleted"

                    else:
                        max_val = self.left.left.max()
                        self.delete(max_val)
                        self.left.data = max_val
                        return f"{dat} is deleted and max_val is {max_val}"

                elif self.left.data < dat:
                    if self.left.right:
                        return self.left.right.delete(dat)

                elif self.left.data > dat:
                    if self.left.left:
                        return self.left.left.delete(dat)

        if self.data < dat:
            if self.right:
                if self.right.data == dat:
                    if self.right.left is None and self.right.right is None:
                        self.right = None
                        return f"{dat} is deleted"

                    elif self.right.left is None:
                        if self.right.right:
                            self.right = self.right.right
                            return f"{dat} is deleted"

                    elif self.right.right is None:
                        if self.right.left:
                            self.right = self.right.left
                            return f"{dat} is deleted"

                    else:
                        max_val = self.right.left.max()
                        self.delete(max_val)
                        self.right.data = max_val
                        return f"{dat} is deleted and max_val is {max_val}"

                elif self.right.data < dat:
                    if self.right.right:
                        return self.right.right.delete(dat)

                elif self.right.data > dat:
                    if self.right.left:
                        return self.right.left.delete(dat)


def list_to_bst(lst):
    root = BinarySearchTree(lst[0])
    for i in range(1, len(lst)):
        root.add_child(lst[i])

    return root


if __name__ == "__main__":
    #    bst = BinarySearchTree(10)
    numbers = [10, 2, 12, 4, 7, 3, 9, 6, 11, 22]
    tree = list_to_bst(numbers)
    print(tree.search(12))
    print(tree.max())
    print(tree.delete(12))
    print(tree.search(22))
    print(tree.print())
