class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, value):
        self.top = Node(value, self.top)
        self._size += 1

    def pop(self):
        if self.top is None:
            raise IndexError("pop from empty stack")

        node = self.top
        self.top = self.top.next
        self._size -= 1

        return node.item

    def is_empty(self):
        return self.top is None

    def peek(self):
        if self.top is None:
            raise IndexError("peek from empty stack")
        
        return self.top.item

    def size(self):
        return self._size



if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Initial stack:", stack)

    print("Popped item:", stack.pop())
    print("Stack after pop:", stack)

    print("Top item:", stack.peek())
    print("Stack size:", stack.size())

    print("Is stack empty?", stack.is_empty())
    stack.pop()
    stack.pop()
    print("Is stack empty after popping all elements?", stack.is_empty())
