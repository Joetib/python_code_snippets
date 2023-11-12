# To reverse the order of elements in a queue, we can use a stack.
# We will pop all the elements from the queue and push them into the stack.
# Then, we will pop all the elements from the stack and enqueue them back into the queue.

from queue import Queue
from stack import Stack  # Assuming a Stack implementation is available

def reverse_queue(queue):
    stack = Stack()
    
    # Pop all elements from the queue and push them into the stack
    while not queue.empty():
        stack.push(queue.get())
    
    # Pop all elements from the stack and enqueue them back into the queue
    while not stack.is_empty():
        queue.put(stack.pop())

# Example usage:
q = Queue()
q.put(1)
q.put(2)
q.put(3)
q.put(4)

reverse_queue(q)

# Output: 4 3 2 1
while not q.empty():
    print(q.get(), end=' ')
# Please Like and Subscribe