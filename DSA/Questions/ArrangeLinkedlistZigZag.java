// ArrangeLinkedlistZigZag.java file name

// code for Rearrange the linkedlist in zig-zag fashion

//code
class Node {
    int data;
    Node next;

    Node(int d) {
        data = d;
        next = null;
    }
}
class LinkedList {
    Node head;

    void zigZag() {
        boolean flag = true;
        Node current = head;

        while (current != null && current.next != null) {
            if (flag) {
                // "<" relation expected
                if (current.data > current.next.data) {
                    swap(current, current.next);
                }
            } else {
                // ">" relation expected
                if (current.data < current.next.data) {
                    swap(current, current.next);
                }
            }
            flag = !flag;
            current = current.next;
        }
    }
    void swap(Node a, Node b) {
        int temp = a.data;
        a.data = b.data;
        b.data = temp;
    }
    void push(int new_data) {
        Node new_node = new Node(new_data);
        new_node.next = head;
        head = new_node;
    }
    void printList() {
        Node temp = head;
        while (temp != null) {
            System.out.print(temp.data + " ");
            temp = temp.next;
        }
    }
    public static void main(String[] args) {
        LinkedList list = new LinkedList();
        list.push(4);
        list.push(3);
        list.push(7);
        list.push(8);
        list.push(6);
        list.push(2);
        list.push(1);

        System.out.println("Original Linked List:");
        list.printList();

        list.zigZag();

        System.out.println("\nZig-Zag Linked List:");
        list.printList();
    }
}