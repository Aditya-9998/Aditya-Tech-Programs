/*
 file name: Remove_Duplicate.java
Remove duplicate from unsorted linked list in O(n^2) time without using extra space.
*/

class Node {
    int data;
    Node next;

    Node(int data) {
        this.data = data;
        this.next = null;
    }
}

class Remove_Duplicate {
    Node head;

    // Remove duplicates from an unsorted linked list using for loops
    void removeDuplicates() {
        for (Node current = head; current != null; current = current.next) {
            Node prev = current;
            for (Node runner = current.next; runner != null; runner = runner.next) {
                if (runner.data == current.data) {
                    // Duplicate found, remove it
                    prev.next = runner.next;
                } else {
                    prev = runner;
                }
            }
        }
    }

    // Add a new node to the front of the list
    void push(int new_data) {
        Node new_node = new Node(new_data);
        new_node.next = head;
        head = new_node;
    }

    // Print the linked list
    void printList() {
        Node temp = head;
        while (temp != null) {
            System.out.print(temp.data + " ");
            temp = temp.next;
        }
        System.out.println();
    }

    // Example usage
    public static void main(String[] args) {
        Remove_Duplicate list = new Remove_Duplicate();
        list.push(20);
        list.push(13);
        list.push(13);
        list.push(11);
        list.push(11);
        list.push(20);

        System.out.println("Linked List before removing duplicates:");
        list.printList();

        list.removeDuplicates();
        System.out.println("Linked List after removing duplicates:");
        list.printList();
    }
}