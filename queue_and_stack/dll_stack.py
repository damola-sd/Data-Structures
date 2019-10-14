from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.storage.add_to_head(value)
        self.size = self.size + 1

    def pop(self):
        if self.size != 0:
            delete_head = self.storage.remove_from_head()
            self.size = self.size - 1
            return delete_head

    def len(self):
        return self.size
