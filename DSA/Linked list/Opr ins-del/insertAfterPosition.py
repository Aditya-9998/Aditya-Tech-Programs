class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insertAfterPosition(self, value, position):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            return

        currentNode = self.head
        count = 0

        while currentNode and count < position:
            currentNode = currentNode.next
            count += 1

        if currentNode is None:
            print("Position out of range.")
            return

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
linkedList.insertAtEnd(50)

linkedList.insertAfterPosition(40, 2)  # Insert after position 2 (after 30)

linkedList.display()
