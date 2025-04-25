class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insertAtEnd(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            return
        currentNode = self.head
        while currentNode.next:
            currentNode = currentNode.next
        currentNode.next = newNode

    def deleteAfterValue(self, targetValue):
        if self.head is None:
            print("List is empty. Nothing to delete.")
            return
        
        currentNode = self.head
        # Find the node with targetValue
        while currentNode and currentNode.data != targetValue:
            currentNode = currentNode.next
        
        if currentNode is None:
            print(f"Value {targetValue} not found in the list.")
            return
        
        if currentNode.next is None:
            print(f"No node exists after the node with value {targetValue}.")
            return
        
        # Delete the node after currentNode
        deleted_value = currentNode.next.data
        currentNode.next = currentNode.next.next
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

linkedList.deleteAfterValue(30)  # Should delete the node with value 40 (after 30)

print("After deleteAfterValue(30):")
linkedList.display()
