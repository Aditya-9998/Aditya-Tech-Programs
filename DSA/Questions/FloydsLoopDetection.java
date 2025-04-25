/*

problem : check if loop exists in linked list,remove loop if exists

1. Floyd's Cycle Detection Algorithm
2. Detect the start of the loop
3. Remove the loop(last_node)
4.last_node.next=null

create a linked list with a loop
detect and remove the loop

 */




class Node {
    int data;
    Node next;

    Node(int data) {
        this.data = data;
        this.next = null;
    }
}
class LinkedList {
    Node head;

    // Function to detect and remove loop in the linked list
    public void detectAndRemoveLoop() {
        Node slow = head;
        Node fast = head;

        // Detect loop using Floyd's Cycle Detection Algorithm
        while (slow != null && fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;

            // If slow and fast meet, there is a loop
            if (slow == fast) {
                System.out.println("Loop detected");
                break;
            }
        }

        // If loop exists, find the start of the loop
        if (slow == fast) {
            slow = head;
            while (slow != fast) {
                slow = slow.next;
                fast = fast.next;
            }
            System.out.println("Start of loop: " + slow.data);

            // Remove the loop
            Node lastNode = slow;
            while (lastNode.next != slow) {
                lastNode = lastNode.next;
            }
            lastNode.next = null; // Remove the loop
            System.out.println("Loop removed");
        } else {
            System.out.println("No loop detected");
        }
    }

    // Function to add a new node at the end of the linked list
    public void add(int data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = newNode;
            return;
        }
        Node current = head;
        while (current.next != null) {
            current = current.next;
        }
        current.next = newNode;
    }
    // Function to create a loop in the linked list for testing purposes
    public void createLoop(int position) {
        if (position == 0) return; // No loop to create

        Node loopNode = head;
        for (int i = 1; i < position && loopNode != null; i++) {
            loopNode = loopNode.next;
        }
        if (loopNode == null) return; // Position is out of bounds

        Node lastNode = head;
        while (lastNode.next != null) {
            lastNode = lastNode.next;
        }
        lastNode.next = loopNode; // Create the loop
    }   

    // Function to print the linked list
    public void printList() {
        Node current = head;
        while (current != null) {
            System.out.print(current.data + " -> ");
            current = current.next;
        }
        System.out.println("null");
    }   
}
public class FloydsLoopDetection {
    public static void main(String[] args) {
        LinkedList list = new LinkedList();
        list.add(1);
        list.add(2);
        list.add(3);
        list.add(4);
        list.add(5);

        // Create a loop for testing
        list.createLoop(2); // Loop starts at node with value 3

        // Detect and remove the loop
        list.detectAndRemoveLoop();

        // Print the linked list after removing the loop
        System.out.println("Linked List after removing loop:");
        list.printList();
    }
}
// Output:  