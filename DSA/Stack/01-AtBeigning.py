'''
linkedlist implemention in stack
node class
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            return None
        popped_data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return popped_data

    def peek(self):
        if self.is_empty():
            return None
        return self.head.data

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()        

if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Stack after pushing 10, 20, 30:")
    stack.display()

    print("Peek:", stack.peek())

    print("Pop:", stack.pop())
    print("Stack after popping:")
    stack.display()

    print("Is stack empty?", stack.is_empty())
    print("Stack size:", stack.get_size())