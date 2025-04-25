// reverse sub part of linked list m, n 

public class ReverseSubLinked {
    Node head;

    // Function to reverse the linked list from position m to n
    public void reverseBetween(int m, int n) {
        if (head == null || m >= n) {
            return;
        }

        Node dummy = new Node(0);
        dummy.next = head;
        Node prev = dummy;

        // Move prev to the node before position m
        for (int i = 1; i < m; i++) {
            prev = prev.next;
        }

        Node start = prev.next; // The first node of the sublist to be reversed
        Node then = start.next; // The node that will be reversed

        // Reverse the sublist from m to n
        for (int i = 0; i < n - m; i++) {
            start.next = then.next;
            then.next = prev.next;
            prev.next = then;
            then = start.next;
        }

        head = dummy.next; // Update the head in case it was changed
    }
    // Function to push a new node at the end of the list
    public void push(int new_data) {
        Node new_node = new Node(new_data);
        if (head == null) {
            head = new_node;
            return;
        }
        Node last = head;
        while (last.next != null) {
            last = last.next;
        }
        last.next = new_node;
    }   
    // Function to print the linked list    
    public void printList() {
        Node temp = head;
        while (temp != null) {
            System.out.print(temp.data + " ");
            temp = temp.next;
        }
        System.out.println();
    }
    // Example usage    
    public static void main(String[] args) {
        ReverseSubLinked list = new ReverseSubLinked();
        list.push(1);
        list.push(2);
        list.push(3);
        list.push(4);
        list.push(5);

        System.out.println("Original List:");
        list.printList();

        int m = 2, n = 4;
        list.reverseBetween(m, n);

        System.out.println("Reversed List from position " + m + " to " + n + ":");
        list.printList();
    }
}