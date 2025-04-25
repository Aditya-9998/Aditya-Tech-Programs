class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insertAtEnd(self, value):
        newNode = Node(value)
        if not self.head:
            self.head = newNode
            return
        currentNode = self.head
        while currentNode.next:
            currentNode = currentNode.next
        currentNode.next = newNode

    def deleteBeforeValue(self, targetValue):
        if self.head is None or self.head.next is None:
            print("Not enough nodes to perform deletion before value.")
            return

        # If the node before the head (i.e., head) is to be deleted,
        # that means head.next contains the target value.
        if self.head.next.data == targetValue:
            deleted_value = self.head.data
            self.head = self.head.next
            print(f"Deleted: {deleted_value}")
            return

        prev = self.head
        current = self.head.next

        # Traverse until current.next is the target, keeping track of previous node.
        while current.next and current.next.data != targetValue:
            prev = current
            current = current.next

        if current.next is None:
            print(f"Value {targetValue} not found in the list.")
            return

        # Delete the node before the target (i.e., 'current' node)
        deleted_value = current.data
        prev.next = current.next
        print(f"Deleted: {deleted_value}")

    def display(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.data, end=" -> ")
            currentNode = currentNode.next
        print("None")

# Example usage
linkedList = SinglyLinkedList()
linkedList.insertAtEnd(10)
linkedList.insertAtEnd(20)
linkedList.insertAtEnd(30)
linkedList.insertAtEnd(40)
linkedList.insertAtEnd(50)

print("Initial List:")
linkedList.display()

linkedList.deleteBeforeValue(30)  # Should delete 20, which is immediately before the node with value 30

print("After deleteBeforeValue(30):")
linkedList.display()
