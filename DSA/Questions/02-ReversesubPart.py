'''reverse sub part of linked list m, n '''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def reverse_between(self, m, n):
        if m == n:
            # If m and n are the same, no need to reverse
            return

        dummy = Node(0)
        dummy.next = self.head
        prev = dummy

        # Move `prev` to the node just before the `m`th position
        for i in range(1, m):
            if prev is None:
                # If `m` is out of bounds, do nothing
                return
            prev = prev.next

        # Start reversing the sublist
        reverse_start = prev.next
        curr = reverse_start.next

        for i in range(n - m):
            if curr is None:
                # If `n` is out of bounds, stop reversing
                break
            reverse_start.next = curr.next
            curr.next = prev.next
            prev.next = curr
            curr = reverse_start.next

        # Update the head in case the reversal starts at the first node
        self.head = dummy.next

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
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
    ll.append(3)
    ll.append(4)
    ll.append(5)

    print("Original list:")
    ll.print_list()

    m = 2
    n = 4
    ll.reverse_between(m, n)

    print(f"List after reversing between positions {m} and {n}:")
    ll.print_list()