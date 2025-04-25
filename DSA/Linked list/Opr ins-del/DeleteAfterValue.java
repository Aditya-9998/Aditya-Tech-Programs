// DeleteAfterValue.java

class Node {
    int data;
    Node next;

    Node(int data) {
        this.data = data;
        this.next = null;
    }
}

class SinglyLinkedList {
    Node head;

    public void insertAtEnd(int value) {
        Node newNode = new Node(value);
        if (head == null) {
            head = newNode;
            return;
        }
        Node currentNode = head;
        while (currentNode.next != null) {
            currentNode = currentNode.next;
        }
        currentNode.next = newNode;
    }

    public void deleteAfterValue(int targetValue) {
        if (head == null) {
            System.out.println("List is empty. Nothing to delete.");
            return;
        }

        Node currentNode = head;
        // Find the node with targetValue
        while (currentNode != null && currentNode.data != targetValue) {
            currentNode = currentNode.next;
        }

        if (currentNode == null) {
            System.out.println("Value " + targetValue + " not found in the list.");
            return;
        }

        if (currentNode.next == null) {
            System.out.println("No node exists after the node with value " + targetValue + ".");
            return;
        }

        // Delete the node after currentNode
        int deletedValue = currentNode.next.data;
        currentNode.next = currentNode.next.next;
        System.out.println("Deleted: " + deletedValue);
    }

    public void display() {
        Node currentNode = head;
        while (currentNode != null) {
            System.out.print(currentNode.data + " -> ");
            currentNode = currentNode.next;
        }
        System.out.println("None");
    }

    public static void main(String[] args) {
        SinglyLinkedList linkedList = new SinglyLinkedList();
        linkedList.insertAtEnd(10);
        linkedList.insertAtEnd(20);
        linkedList.insertAtEnd(30);
        linkedList.insertAtEnd(40);
        linkedList.insertAtEnd(50);

        System.out.println("Initial List:");
        linkedList.display();

        linkedList.deleteAfterValue(30);  // Should delete the node with value 40

        System.out.println("After deleteAfterValue(30):");
        linkedList.display();
    }
}
