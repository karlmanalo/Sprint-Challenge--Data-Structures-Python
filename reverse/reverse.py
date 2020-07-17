class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # If node is empty
        if node is None:
            return
        
        # Sets tail of SLL as head of reversed list
        if node.get_next() is None:
            self.head = node
            return

        # Recursively reversing by converting the current node to the previous node
        self.reverse_list(node.get_next(), node)

        # Sets next node reference of next node as previous node
        node.get_next().set_next(node)
        
        # Next value becomes none on new tail
        node.set_next(None) 