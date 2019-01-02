"""
Data Structures: Linked List in Python
https://www.youtube.com/playlist?list=PLzjoZGHG3J8vdUH75YPqmO7lbQl_M-xXo
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.nxt = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_head(self, new_node):
        temporary_node = self.head
        self.head = new_node
        self.head.nxt = temporary_node
        del temporary_node

    def insert_end(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.nxt is not None:
                last_node = last_node.nxt
            last_node.nxt = new_node

    def delete_end(self):
        last_node = self.head
        while last_node.nxt is not None:
            previous_node = last_node
            last_node = last_node.nxt
        previous_node.nxt = None

    def print_list(self):
        current = self.head
        while current is not None:
            print current.data
            current = current.nxt


# Create a linked list
my_linked_list = LinkedList()

# Create 1st node
first_node = Node("John")

# Add 1st node to the linked list
my_linked_list.insert_end(first_node)

# Create 2nd node
second_node = Node("Ben")

# Add 2nd node to the linked list
my_linked_list.insert_end(second_node)

# Create 3rd node
third_node = Node("Matthew")

# Add 3rd node to the linked list
my_linked_list.insert_end(third_node)

# Create 4th node
fourth_node = Node("Konstantin")

# Add 4th node at the beginning of the linked list
my_linked_list.insert_head(fourth_node)

# Delete the last element in the linked list
my_linked_list.delete_end()

# Print linked list
my_linked_list.print_list()
