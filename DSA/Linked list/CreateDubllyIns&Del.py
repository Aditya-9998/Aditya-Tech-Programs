# create a dubbuly linked list and delete a node from it and insert and deleted perform
#code  11,Apr,25

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
    # Function to insert a node at the end of the list
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last
        
    # Function to delete a node from the list
    def delete_node(self, key):
        if self.head is None:
            return
        temp = self.head
        while temp:
            if temp.data == key:
                if temp.prev:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                del temp
                return
            temp = temp.next
            
    # Function to display the list from head to tail
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")
        
# Example usage
if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert_at_end(1)
    dll.insert_at_end(2)
    dll.insert_at_end(3)
    print("Doubly Linked List after inserting elements at end:")
    dll.display()
    
    dll.delete_node(2)
    print("Doubly Linked List after deleting node with data 2:")
    dll.display()
    
    dll.delete_node(1)
    print("Doubly Linked List after deleting node with data 1:")
    dll.display()
    dll.delete_node(3)  
    print("Doubly Linked List after deleting node with data 3:")
    dll.display()
    