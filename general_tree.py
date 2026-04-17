#!/usr/bin/env python3


class TreeNode:

    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self):
        print(self.data)
        for child in self.children:
            print(child.data)


def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptops")
    laptop.add_child(TreeNode("Macbook"))
    laptop.add_child(TreeNode("Microsoft Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cell_phones = TreeNode("Cell Phones")
    cell_phones.add_child(TreeNode("iPhone"))
    cell_phones.add_child(TreeNode("Google Pixel"))
    cell_phones.add_child(TreeNode("Vivo"))

    television = TreeNode("Televisions")
    television.add_child(TreeNode("Samsung"))
    television.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cell_phones)
    root.add_child(television)

    return root.print_tree()


if __name__ == "__main__":
    build_product_tree()
