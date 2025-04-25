#In stack implemtation insert at end and also delete
# Node class

class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
# Stack class
class Stack:
    def __init__(self):
        self.top = None
        
    # Function to insert an element at the end of the stack
    def insert_at_end(self, data):
        new_node = node(data)
        if self.top is None:
            self.top = new_node
            return
        current = self.top
        while current.next:
            current = current.next
        current.next = new_node
        
    # Function to delete an element from the end of the stack
    def delete_from_end(self):
        if self.top is None:
            print("Stack is empty")
            return
        if self.top.next is None:
            self.top = None
            return
        current = self.top
        while current.next and current.next.next:
            current = current.next
        current.next = None
        # Function to display the stack
    def display(self):
        if self.top is None:
            print("Stack is empty")
            return
        current = self.top
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")   
# Example usage 
if __name__ == "__main__":
    stack = Stack()
    stack.insert_at_end(1)
    stack.insert_at_end(2)
    stack.insert_at_end(3)
    print("Stack after inserting elements at end:")
    stack.display()
    
    stack.delete_from_end()
    print("Stack after deleting element from end:")
    stack.display()
    
    stack.delete_from_end()
    print("Stack after deleting element from end:")
    stack.display()
    
    stack.delete_from_end()
    print("Stack after deleting element from end:")
    stack.display()
    
    stack.delete_from_end()  # Attempt to delete from an empty stack
    stack.display() 
    # Output:
    

