class Node:
    def __init__(self, item, next_node=None):
        self.item = item
        self.next = next_node

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def push(self, value):
        new_node = Node(value)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def pop(self):
        if self.front is None:
            return None
        popped_item = self.front.item
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return popped_item

    def is_empty(self):
        return self.front is None

# Example usage:
queue = Queue()
queue.push(1)
queue.push(2)
print(queue.pop())  # Output: 1
print(queue.is_empty())  # Output: False
print(queue.pop())  # Output: 2
print(queue.is_empty())  # Output: True
