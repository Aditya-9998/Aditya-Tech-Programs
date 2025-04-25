'''
problem : check if loop exists in linked list,remove loop if exists

1. Floyd's Cycle Detection Algorithm
2. Detect the start of the loop
3. Remove the loop(last_node)
4.last_node.next=null

create a linked list with a loop
detect and remove the loop


'''

class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.visited = False
        # self.next = next
    def __str__(self):
        return str(self.data)
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def create_loop(self, pos):
        if pos == 0:
            return
        loop_start = self.head
        for _ in range(1, pos):
            loop_start = loop_start.next
        self.tail.next = loop_start

    def detect_and_remove_loop(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return False  # No loop detected

        # Find the start of the loop
        slow = self.head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        # Remove the loop
        last_node = fast
        while last_node.next != slow:
            last_node = last_node.next
        last_node.next = None

        return True  # Loop detected and removed
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
# Example usage
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)