# Linked List
# Linear data structure; elements NOT stored at contiguous memory locations;
# "...linear collection of data elements whose order is not given by their
# physical placement in memory. Instead, each ele points to the next. It
# consists of a collection of nodes which together represent a sequence.
# In its most basic form, each node contains data and a reference (link)
# to the next node in the sequence. Allows for efficient insertion or
# removal of ele's from any position in the sequence during iteration.
# Plus: arbitrary access; Drawbacks: access time is linear and difficult
# to pipeline. See also: "doubly linked" lists (like back arrows on website,
# can "traverse" list both forward and backward). Plus: list ele's can be
# easily inserted or removed without reallocation or reorganization of the
# entire structure b/c data items aren't stored contiguously. Allows inser-
# tion of nodes at any point in the list and keeps up with operations by
# storing the link previous to any link being added or removed during a
# list traversal.
# Skills to know: (1) traverse a linked list (be able to travel along the
# nodes and pointers, (2) search a list for the header (a node) or tail
# (last and final node), (3) insert a new header or tail (node) and (4) delete
# a node or tail.  A linked list generally requires a header.
# Create a linked list representing a small family group; be able to do all of
# the operations.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def traversal(self):
        first = self.head
        while first:
            print(first.data)
            first = first.next

    def insert_new_header(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def search(self, z):
        temp = self.head
        while temp is not None:
            if temp.data == z:
                return True
            temp = temp.next

        else:
            return False

    def delete_node(self, data):
        temp = self.head
        while temp is not None:
            if temp.data == data:
                break
            prev = temp
            temp = temp.next
        prev.next = temp.next

    def delete_tail(self):
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None

    def reverse_traverse(self):  # This was from YouTube "CodeFights Interview Practice"
        # I played with this using variously placed print statements and still not sure if
        # or how it works! :D It's been 24 hours, at least, and time to move on :)
        head = self.head
        print(self.head.data)
        if head is None or head.next is None:
            return head

        already_reversed, current = head, head.next
        already_reversed.next = None

        while current is not None:
            store_pointer = current.next
            current.next = already_reversed

            already_reversed = current
            current = store_pointer

        return already_reversed


family = LinkedList()
family.head = Node("Rebecca")
guardian_of_being1 = Node("Alice")
guardian_of_being2 = Node("Finn")
guardian_of_being3 = Node("Lovin")
problem = Node("ego")


family.head.next = guardian_of_being1
guardian_of_being1.next = guardian_of_being2
guardian_of_being2.next = guardian_of_being3
guardian_of_being3.next = problem

#family.traversal()
family.insert_new_header("Love")

# family.delete_tail()

# print(family.search("ego")
# family.delete_node("Rebecca")
family.delete_tail()
family.traversal()
family.reverse_traverse()
