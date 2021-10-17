import Deque as deq

# Program starts
empty = deq.Deque()     # An empty deque
deque = deq.Deque()     # To be filled

print("\nTest to remove all elements")
temp = deq.Deque()
for i in range(100, 106):
    temp.add_first(i)
while temp.size > 0:
    temp.remove_last()
print("After removing all elements:", temp.to_string())
print("Size:", temp.size)
