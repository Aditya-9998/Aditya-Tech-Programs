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

    public SinglyLinkedList() {
        this.head = null;
    }

    public void insertAfterValue(int targetValue, int newValue) {
        if (head == null) {
            System.out.println("List is empty.");
            return;
        }

        Node currentNode = head;
        while (currentNode != null && currentNode.data != targetValue) {
            currentNode = currentNode.next;
        }

        if (currentNode == null) {
            System.out.println("Value " + targetValue + " not found in the list.");
            return;
        }

        Node newNode = new Node(newValue);
        newNode.next = currentNode.next;
        currentNode.next = newNode;
    }

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

    public void display() {
        Node currentNode = head;
        while (currentNode != null) {
            System.out.print(currentNode.data + " -> ");
            currentNode = currentNode.next;
        }
        System.out.println("None");
    }
}

public class InsertAfterValue {
    public static void main(String[] args) {
        SinglyLinkedList linkedList = new SinglyLinkedList();

        linkedList.insertAtEnd(10);
        linkedList.insertAtEnd(20);
        linkedList.insertAtEnd(30);
        linkedList.insertAtEnd(40);

        linkedList.insertAfterValue(30, 35);  // Insert 35 after value 30

        linkedList.display();
    }
}
