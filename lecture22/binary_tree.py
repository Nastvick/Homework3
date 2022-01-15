class ListNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.value}'

    def add_child(self, child: 'ListNode'):
        if self.value:
            if child < self.value:
                if self.left is None:
                    self.left = ListNode(child)
                else:
                    self.left.add_child(child)
            elif child > self.value:
                if self.right is None:
                    self.right = ListNode(child)
                else:
                    self.right.add_child(child)
        else:
            self.value = child


    def is_exists(self, value) -> bool:
        ...

    def remove_this_node(self):
        ...

# queue - FIFO
# stack - LIFO

root = ListNode(5)
root.add_child(ListNode(3))
root.add_child(ListNode(7))
root.add_child(ListNode(4))
root.add_child(ListNode(2))
root.add_child(ListNode(1))
root.add_child(ListNode(6))
root.add_child(ListNode(8))

root = ListNode(value=2, left=ListNode(1, ListNode(0), ListNode(1.5)), right=ListNode(3))


def print_tree(node, level=0):
    if node is not None:
        print_tree(node.right, level + 1)
        print(' ' * 4 * level + '->', node.value)
        print_tree(node.left, level + 1)


if __name__ == '__main__':
    print_tree(root)