// DeleteAtPosition.java

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

    public void deleteFromBegin() {
        if (head == null) {
            System.out.println("List is empty. Nothing to delete.");
            return;
        }
        int deletedValue = head.data;
        head = head.next;
        System.out.println("Deleted: " + deletedValue);
    }

    public void deleteAtPosition(int position) {
        if (head == null) {
            System.out.println("List is empty. Nothing to delete.");
            return;
        }

        if (position <= 0) {
            deleteFromBegin();
            return;
        }

        Node currentNode = head;
        Node prevNode = null;
        int count = 0;

        while (currentNode != null && count < position) {
            prevNode = currentNode;
            currentNode = currentNode.next;
            count++;
        }

        if (currentNode == null) {
            System.out.println("Position out of range.");
            return;
        }

        prevNode.next = currentNode.next;
        System.out.println("Deleted: " + currentNode.data);
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
        linkedList.insertAtEnd(0);
        linkedList.insertAtEnd(20);
        linkedList.insertAtEnd(30);
        linkedList.insertAtEnd(40);
        linkedList.insertAtEnd(50);

        System.out.println("Initial List:");
        linkedList.display();

        linkedList.deleteAtPosition(2);  // Should delete the element at index 2 (30)
        System.out.println("After deleteAtPosition(2):");
        linkedList.display();
    }
}
