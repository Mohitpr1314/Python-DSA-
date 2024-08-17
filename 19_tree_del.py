class Node:
    def __init__(self, item = None, left = None, right = None):
        self.item = item
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = None


    def min_value(self, temp):
        current = temp
        while current.left is not None:
            current = current.left
        return current.item

    def max_value(self, temp):
        current = temp
        while current.right is not None:
            current = current.right
        return current.item


def delete(self, data):
    self.root = self.rdelete(self.root, data)

def rdelete(self, root, data):
    if root is None:
        return None
    if data < root.item:
        root.left = self.rdelete(root.left, data)
    elif data > root.item:
        root.right = self.rdelete(root.right, data)
    else:
        if root.left is None:
            return root.right
        else:
            root.right is None
            return root.left
        root.item = self.min_value(root.right)
        self.rdelete(root.right, root.item)
    return root

def size(self):
    return len(self.inorder)
