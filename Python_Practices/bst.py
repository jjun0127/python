class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert_child(self.root, value)

    def _insert_child(self, node, value):
        if node is None:
            node = Node(value)
        else:
            if value < node.data:
                node.left = self._insert_child(node.left, value)
            else:
                node.right = self._insert_child(node.right, value)
        return node

    def search(self, value):
        root, target = self._search_child(self.root, value)
        if root is None:
            print(value, 'is not found')
            return None
        else:
            print(value, 'is found')
            return root, target

    def find(self, key):
        return self._find_value(self.root, key)

    def _find_value(self, root, key):
        if root is None or root.data == key:
            return root is not None
        elif key < root.data:
            return self._find_value(root.left, key)
        else:
            return self._find_value(root.right, key)

    def delete(self, key):
        self.root, deleted = self._delete_value(self.root, key)
        return deleted

    def _delete_value(self, node, key):
        if node is None:
            return node, False

        deleted = False
        if key == node.data:
            deleted = True
            if node.left and node.right:
                # replace the node to the leftmost of node.right
                parent, child = node, node.right
                while child.left is not None:
                    parent, child = child, child.left
                child.left = node.left
                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child
            elif node.left or node.right:
                node = node.left or node.right
            else:
                node = None
        elif key < node.data:
            node.left, deleted = self._delete_value(node.left, key)
        else:
            node.right, deleted = self._delete_value(node.right, key)
        return node, deleted

    def _search_child(self, node, value):
        if node is None:
            return None
        if value == node.data:
            return self.root, node
        else:
            if value < node.data:
                return self._search_child(node.left, value)
            else:
                return self._search_child(node.right, value)

    # def delete(self, value):
    #     root, node = self.search(value)
    #     if node is None:
    #         return False
    #     else:
    #         self.delete_child(node)
    #
    # def delete_child(self, node):
    #     if node.left is None and node.right is None:
    #         print(node.data, 'is deleted')
    #         print(node)
    #         node = None
    #         print(self.root.left.left.data)
    #     elif node.left is None:
    #         node = node.right
    #         self.delete_child(node.right)
    #     elif node.right is None:
    #         node = node.left
    #         self.delete_child(node.left)
    #     return node





if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(9)
    bst.insert(8)
    bst.delete(10)



