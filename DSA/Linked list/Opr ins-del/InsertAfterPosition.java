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

    public void insertAfterPosition(int value, int position) {
        Node newNode = new Node(value);

        if (head == null) {
            head = newNode;
            return;
        }

        Node currentNode = head;
        int count = 0;

        while (currentNode != null && count < position) {
            currentNode = currentNode.next;
            count++;
        }

        if (currentNode == null) {
            System.out.println("Position out of range.");
            return;
        }

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

public class InsertAfterPosition {
    public static void main(String[] args) {
        SinglyLinkedList linkedList = new SinglyLinkedList();

        linkedList.insertAtEnd(10);
        linkedList.insertAtEnd(20);
        linkedList.insertAtEnd(30);
        linkedList.insertAtEnd(50);

        linkedList.insertAfterPosition(40, 2); // Insert after position 2 (after 30)

        linkedList.display();
    }
}
