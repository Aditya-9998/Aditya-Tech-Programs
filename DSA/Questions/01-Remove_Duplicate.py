# Remove duplicate from unshorted linked list in o(1) Auxullary space will no extra space
# code

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None    
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def remove_duplicates(self):
        current = self.head
        prev = None
        seen = set()
        
        while current:
            if current.data in seen:
                prev.next = current.next
            else:
                seen.add(current.data)
                prev = current
            current = current.next
            
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
# Example usage
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(2)
    ll.append(3)
    ll.append(3)
    ll.append(4)
    
    print("Original list:")
    ll.print_list()
    
    ll.remove_duplicates()
    
    print("List after removing duplicates:")
    ll.print_list()