# insertAtEnd.py
# Python program to insert an element at the end of a stack
# creat class node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
# creat class stack 
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
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
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

    print("Insert 40 at the end:")
    stack.insert_at_end(40)
    stack.display()

    print("Insert 50 at the end:")
    stack.insert_at_end(50)
    stack.display()

    print("Is stack empty?", stack.is_empty())
    print("Size of stack:", stack.get_size())       