
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def _recursive_add_helper(self, current_node, data):
        if current_node is None:
            return Node(data)  # Base case: end of list, create new node
        else:
            current_node.next = self._recursive_add_helper(current_node.next, data)
            return current_node