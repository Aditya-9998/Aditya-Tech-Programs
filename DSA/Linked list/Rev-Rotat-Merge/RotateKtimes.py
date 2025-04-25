'''
create node class
 create linl class
    create insert methode and display
     create roatesKtimes methode
    create main methode
    create linked list      
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def rotate_k_times(self, k):
        if k == 0 or self.head is None:
            return

        # Count the number of nodes in the list
        count = 1
        current = self.head
        while current.next:
            count += 1
            current = current.next

        # If k is greater than the number of nodes, reduce it
        k %= count

        if k == 0:
            return

        # Find the kth node from the end
        current = self.head
        for _ in range(count - k - 1):
            current = current.next

        # Set the new head and break the list
        new_head = current.next
        current.next = None

        # Find the last node and connect it to the old head
        last_node = new_head
        while last_node.next:
            last_node = last_node.next
        last_node.next = self.head

        # Update the head to point to the new head
        self.head = new_head
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)

    print("Original Linked List:")
    ll.display()

    k = 2
    ll.rotate_k_times(k)

    print(f"Linked List after rotating {k} times:")
    ll.display()
    