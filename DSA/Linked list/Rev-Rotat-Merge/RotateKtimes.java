/*
create node class
 create linl class
    create insert methode and display
     create roatesKtimes methode
    create main methode

 */
// class node
class Node {
    int data;
    Node next;

    Node(int data) {
        this.data = data;
        this.next = null;
    }
}

// class linked list
class LinkedList {
    Node head;

    // insert method
    public void insert(int data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = newNode;
        } else {
            Node current = head;
            while (current.next != null) {
                current = current.next;
            }
            current.next = newNode;
        }
    }

    // rotateKtimes method
    public void rotateKtimes(int k) {
        if (head == null || k <= 0) {
            return;
        }

        Node current = head;
        int length = 1;

        // Find the length of the list
        while (current.next != null) {
            current = current.next;
            length++;
        }

        // Connect the last node to the head to make it circular
        current.next = head;
        k = k % length;
        // Find the new head after k rotations
        int stepsToNewHead = length - k;
        current = head;
        for (int i = 1; i < stepsToNewHead; i++) {
            current = current.next;
        }
        head = current.next;
        current.next = null;
    }

    // display method
    public void display() {
        Node current = head;
        while (current != null) {
            System.out.print(current.data + " ");
            current = current.next;
        }
        System.out.println();
    }
}

public class RotateKtimes {
    public static void main(String[] args) {
        LinkedList list = new LinkedList();

        // Insert elements into the linked list
        list.insert(1);
        list.insert(2);
        list.insert(3);
        list.insert(4);
        list.insert(5);

        System.out.println("Original list:");
        list.display();

        // Rotate the list k times
        int k = 2;
        list.rotateKtimes(k);

        System.out.println("List after rotating " + k + " times:");
        list.display();
    }
}