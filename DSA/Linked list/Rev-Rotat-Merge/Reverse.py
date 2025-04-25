'''
create list
    create node
    create linkedlist 
reverse list
print list     

'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

   
    def create_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    
    def reverse_list(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


linked_list = LinkedList()
linked_list.create_node(1)
linked_list.create_node(2)
linked_list.create_node(3)
linked_list.create_node(4)

print("Original List:")
linked_list.print_list()

linked_list.reverse_list()

print("Reversed List:")
linked_list.print_list()