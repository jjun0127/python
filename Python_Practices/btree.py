import math
import bisect
from random import *
import time
import sys


class Node:
    def __init__(self, data):
        self.index = None
        self.data = data
        self.link = None

    def data_append(self, value):
        self.data.append(value)
        self.data = sorted(self.data)

    def link_insert(self, index, arr):
        self.link.insert(index, Node(sorted(arr)))

    def data_update(self, data):
        self.data = sorted(data)

    def link_grow(self, data):
        self.link = data

    def data_remove(self, value):
        self.data.remove(value)

    def link_update(self, arr):
        self.link = arr

    def link_merge(self, index):
        data = self.link[index+1].data
        self.link[index].append(data)
        self.link.pop(index+1)


class Btree:
    def __init__(self, degree):
        self.degree = degree
        self.t = math.ceil(degree/2)
        self.root = None
        self.node_count = 0

    def traverse(self):
        self.node_count = 0
        if self.root is not None:
            node_count = self._traverse(self.root)
            print('node count is :' + str(node_count))

    def _traverse(self, node):
        #print(node.data)
        self.node_count += len(node.data)
        if node.link is None:
            return self.node_count
        else:
            for link in node.link:
                self._traverse(link)
        return self.node_count

    def insert(self, value):
        if self.root is None:
            self.root = Node([value])
        else:
            self._insert(value)

    def _insert(self, value):
        path = self.get_path(value)
        if path:
            ancestor_index, node = path.pop()
            node.data_append(value)
            while len(node.data) >= self.degree:  # overflow
                if len(path) > 0:
                    new_ancestor_index, ancestor_node = path.pop()
                    node = self.split(node, ancestor_node, ancestor_index)
                    ancestor_index = new_ancestor_index
                else:
                    # for root node
                    node = self.split_and_grow(node)
        #self.traverse()

    def split(self, node, ancestor_node, ancestor_index):
        ancestor_node.data_append(node.data[self.t - 1])
        data = node.data
        ancestor_node.link[ancestor_index].data_update(data[:self.t - 1])
        ancestor_node.link_insert(ancestor_index + 1, data[self.t:])
        return ancestor_node

    def split_and_grow(self, node):
        links = None
        if node.link:
            links = node.link
        node.link_grow([Node(node.data[:self.t - 1]), Node(node.data[self.t:])])
        node.data_update([node.data[self.t - 1]])
        if links:
            node.link[0].link = links[:self.t]
            node.link[1].link = links[self.t:]
        return node

    def get_path(self, value):
        if self.root is not None:
            path = [[0, self.root]]
            return self._get_path(value, self.root, path)
        else:
            return []

    def _get_path(self, value, node, path):
        while node.link is not None:
            index = bisect.bisect_left(node.data, value)
            link = node.link[index]
            path.append([index, link])
            node = link
        return path

    def find_path(self, value):
        if self.root is not None:
            path = []
            return self._find_path(value, self.root, path)
        else:
            return []

    def _find_path(self, value, node, path):
        path.append(node)
        if value in node.data:
            return path
        else:
            index = bisect.bisect_left(node.data, value)
            path = self._find_path(value, node.link[index], path)
        return path

    def delete(self, value):
        path = self.find_path(value)
        if path:
            node = path.pop()
            if node.link:  # for internal node deletion
                link_index = bisect.bisect_left(node.data, value)
                left_child = node.link[link_index]
                right_child = None
                if len(node.link) > 1:
                    right_child = node.link[link_index + 1]
                if len(left_child.data) >= self.t:
                    self.borrow(node, left_child, value, 'left')
                elif right_child:
                    if len(left_child.data) == self.t-1 and len(right_child.data) == self.t-1:
                        self.merge(node, left_child, right_child, value, link_index)
                    elif len(right_child.data) >= self.t:
                        self.borrow(node, right_child, value, 'right')
                    else:
                        print('here1')
                else:
                    print('here2')
            else:  # for leaf node deletion
                print('leaf node')

    def merge(self, node, left_child, right_child, value, link_index):
        if len(node.data) == 1:  # shrink operation
            node.data_update(left_child.data + right_child.data)
            if left_child.link and right_child.link:
                arr = left_child.link + right_child.link
            elif left_child.link:
                arr = left_child.link
            else:
                arr = None
            node.link_update(arr)
        else:
            node.data_remove(value)
            node.link_merge(link_index)

    def borrow(self, node, child, value, flag):
        node.data_remove(value)
        if flag == 'left':
            borrow_value = child.data[-1]
        else:
            borrow_value = child.data[0]
        child.data_remove(borrow_value)
        node.data_append(borrow_value)


if __name__ == '__main__':
    sys.setrecursionlimit(1500)

    start = time.time()
    b = Btree(3)
    #b.root = Node([5,20])
    count = 1
    b.insert(3)
    b.insert(5)
    b.insert(4)
    b.insert(1)
    b.insert(6)
    #b.delete(2)
    # for i in range(100):
    #     b.insert(randint(1, 100))
    #     if count % 1000 == 0:
    #         print(count)
    #     count += 1


    end = time.time()
    print(end - start)
    b.traverse()

