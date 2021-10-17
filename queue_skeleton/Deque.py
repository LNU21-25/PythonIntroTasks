from dataclasses import dataclass
from typing import Any

# A head-and-tail implementation of a deque using data classes


# Each node is an instance of class Node
@dataclass
class Node:
    value: int = None
    nxt: Any = None  # Any since Node not properly defined at this point


@dataclass
class Deque:
    head: Node = None      # First node in queue
    tail: Node = None      # Last node in queue
    size: int = 0

    # Add element n as first entry in deque
    def add_first(self, n):
        if self.size == 0: # An empty list
            self.head = Node(n, None)
            self.last = self.head
        elif self.size == 1: # Non-empty ==> Find last node
            self.head = Node(n, self.head) 
            self.tail = self.head.nxt 
        else:
            self.head = Node(n, self.head)
        self.size += 1


    # Returns a string representation of the current deque content
    def to_string(self):
        s = "{ "
        n = self.head
        if self.head is None:
            s ="{ }"
            return s
        elif self.tail is None:
            return s + str(self.head.value) + "}"
        else:
            while n.nxt is not None:
                s += str(n.value) + " "
                n = n.nxt
            s += str(n.value) + " }"
            return s

    # Add element n as last entry in deque
    def add_last(self, n):
        if self.size == 0:
            self.head = Node(n, None)
            self.tail = None
            self.size += 1
        elif self.size == 1:
            self.tail = Node(n, None)
            self.head.nxt = self.tail
            self.size += 1
        else:
            self.tail.nxt = Node(n, None)
            self.tail = self.tail.nxt
            self.size += 1



    # Returns (without removing) the last entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    def get_last(self):
        if self.size == 0:
            print("Get can't be applied on an empty list")
            return None
        else:
            return self.tail.value

    # Returns (without removing) the first entry in the deque
    # Gives error message and returns None when accessing empty deque.
    def get_first(self):
        if self.size == 0:
            print("Get can't be applied on an empty list")
            return None
        else:
            return self.head.value

    # Removes and returns the first entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    # The case size = 1 requires speciall handling
    def remove_first(self):
        if self.size == 0:
            print("Get can't be applied on an empty list")
            return None
        elif self.size == 1:
            ret = self.head.value
            self = Deque()
            self.size -= 1
            return ret
        else:
            ret = self.head.value
            self.head = self.head.nxt
            self.size -= 1
            return ret

    # Removes and returns the last entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    # The case size = 1 requires speciall handling
    def remove_last(self):
        if self.size == 0:
            print("Get can't be applied on an empty list")
            return None
        elif self.size == 1:
            ret = self.head.value
            self = Deque()
            self.size -= 1
            return ret
        else:
            ret = self.tail.value
            l = self.head
            while l.nxt is not self.tail:
                l = l.nxt
            self.tail = l
            self.tail.nxt = None
            self.size -= 1
            return ret
    

    def remove_all(self):
        self = Deque()

