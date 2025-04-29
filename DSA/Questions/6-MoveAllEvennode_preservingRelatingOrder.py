# Move all even nodes to the front of the linked list while preserving the relative order of odd nodes sagrigate function

# Approach
# 1. Initialize two pointers, even_head and odd_head, to None.
# 2. Traverse the linked list and for each node:
#    - If the node's value is even, add it to the even list.
#    - If the node's value is odd, add it to the odd list.
# 3. After traversing the list, connect the even list to the odd list.
# 4. Return the head of the new list, which is the head of the even list.
# 5. The time complexity of this approach is O(n), where n is the number of nodes in the linked list.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __str__(self):
        return str(self.data)
    def __repr__(self):
        return str(self.data)
class LinkedList:
    def __init__(self):
        self.head = None
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
    def segregate(self):
        even_head = None
        odd_head = None
        even_tail = None
        odd_tail = None

        current = self.head
        while current:
            if current.data % 2 == 0:
                if even_head is None:
                    even_head = current
                    even_tail = even_head
                else:
                    even_tail.next = current
                    even_tail = even_tail.next
            else:
                if odd_head is None:
                    odd_head = current
                    odd_tail = odd_head
                else:
                    odd_tail.next = current
                    odd_tail = odd_tail.next

            # Move to the next node and break the link to avoid cycles in the list.
            next_node = current.next
            current.next = None  # Break the link to avoid cycles.
            current = next_node

        # If there are no even nodes, return the head of the odd list.
        if even_head is None:
            return odd_head

        # Connect the end of the even list to the head of the odd list.
        even_tail.next = odd_head

        return even_head  # Return the head of the new list.
# Example usage
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)

    print("Original list:")
    ll.print_list()

    new_head = ll.segregate()

    print("List after segregating even and odd nodes:")
    current = new_head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")
    


'''

'''