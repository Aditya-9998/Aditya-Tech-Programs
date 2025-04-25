class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insertAfterValue(self, targetValue, newValue):
        if self.head is None:
            print("List is empty.")
            return

        currentNode = self.head
        while currentNode and currentNode.data != targetValue:
            currentNode = currentNode.next

        if currentNode is None:
            print(f"Value {targetValue} not found in the list.")
            return

        newNode = Node(newValue)
        newNode.next = currentNode.next
        currentNode.next = newNode

    def insertAtEnd(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            return
        currentNode = self.head
        while currentNode.next:
            currentNode = currentNode.next
        currentNode.next = newNode

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

linkedList.insertAfterValue(30, 35)  # Insert 35 after value 30

linkedList.display()
