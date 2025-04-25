# create circular linked list and find mid value of it
# code

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None        
        
class CircularLinkedList:
    def __init__(self):
        self.head = None
        
    # Function to insert a node at the end of the list
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            return
        last = self.head
        while last.next != self.head:
            last = last.next
        last.next = new_node
        new_node.next = self.head
        
    # Function to find the middle value of the circular linked list
    def find_mid_value(self):
        if self.head is None:
            return None
        slow_ptr = self.head
        fast_ptr = self.head
        while fast_ptr and fast_ptr.next != self.head:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        return slow_ptr.data
    # Function to display the list from head to tail    
    def display(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("None")
        
# Example usage 5
if __name__ == "__main__":
    cll = CircularLinkedList()
    cll.insert_at_end(1)
    cll.insert_at_end(2)
    cll.insert_at_end(3)
    cll.insert_at_end(4)
    cll.insert_at_end(5)
    print("Circular Linked List after inserting elements at end:")
    cll.display()
    
    mid_value = cll.find_mid_value()
    print("Middle value of the circular linked list:", mid_value)       
