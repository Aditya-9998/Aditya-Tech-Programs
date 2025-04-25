

//create a linked list and insert a node at the beginning of the list
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

    LinkedList() {
        head = null;
    }

    public void insertBeginning(int data) {  // Method name stays as insertBeginning
        Node newNode = new Node(data);
        newNode.next = head;
        this.head = newNode;
    }

    public void printList() {
        Node current = head;
        while (current != null) {
            System.out.print(current.data + " ");
            current = current.next;
        }
        System.out.println();
    }
}
// main class
public class AtBegning {
    public static void main(String[] args) {
        LinkedList list = new LinkedList();
        list.insertBeginning(10);  // Correct method name here
        list.insertBeginning(20);
        list.insertBeginning(30);
        list.printList();
    }
}
