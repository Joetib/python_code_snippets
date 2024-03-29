# Here is a simple implementation to find the middle element of a linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def find_middle_element(head):
    slow_ptr = head
    fast_ptr = head

    while fast_ptr is not None and fast_ptr.next is not None:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

    return slow_ptr.data

# Example usage
# Create a linked list
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# Find the middle element
middle_element = find_middle_element(head)
print(middle_element)

# Output
# >> 3
# Please Like and Subscribe