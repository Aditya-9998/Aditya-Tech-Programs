/*
create node class

    create node
    create linkedlist 
public class Reversesll

reverse list
print list     

 */

class Node {
    int data;
    Node next;

    Node(int data) {
        this.data = data;
        this.next = null;
    }
}
public class Reverses {
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

    // reverse method
    public void reverse() {
        Node previous = null;
        Node current = head;
        Node next = null;

        while (current != null) {
            next = current.next;
            current.next = previous;
            previous = current;
            current = next;
        }
        head = previous;
    }

    // print method
    public void printList() {
        Node current = head;
        while (current != null) {
            System.out.print(current.data + " ");
            current = current.next;
        }
        System.out.println();
    }

    // main method
    public static void main(String[] args) {
        Reverses list = new Reverses();

        // Insert elements into the linked list
        list.insert(1);
        list.insert(2);
        list.insert(3);
        list.insert(4);
        list.insert(5);

        System.out.println("Original list:");
        list.printList();

        // Reverse the linked list
        list.reverse();

        System.out.println("Reversed list:");
        list.printList();
    }
}