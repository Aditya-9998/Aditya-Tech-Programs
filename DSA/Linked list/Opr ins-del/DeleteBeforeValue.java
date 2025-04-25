// DeleteBeforeValue.java

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

    public void deleteBeforeValue(int targetValue) {
        if (head == null || head.next == null) {
            System.out.println("Not enough nodes to perform deletion before value.");
            return;
        }

        if (head.next.data == targetValue) {
            int deletedValue = head.data;
            head = head.next;
            System.out.println("Deleted: " + deletedValue);
            return;
        }

        Node prev = head;
        Node current = head.next;

        while (current.next != null && current.next.data != targetValue) {
            prev = current;
            current = current.next;
        }

        if (current.next == null) {
            System.out.println("Value " + targetValue + " not found in the list.");
            return;
        }

        int deletedValue = current.data;
        prev.next = current.next;
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

        linkedList.deleteBeforeValue(30);  // Should delete 20
        System.out.println("After deleteBeforeValue(30):");
        linkedList.display();
    }
}
