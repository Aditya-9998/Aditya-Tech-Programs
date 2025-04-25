/*
In stack implemtation insert at end and also delete
 Node class
 */

class Node {
    int data;
    Node next;

    Node(int data) {
        this.data = data;
        this.next = null;
    
    }
}
class Stack {
    Node top;

    Stack() {
        this.top = null;
    }

    // Insert at end
    public void insertAtEnd(int data) {
        Node newNode = new Node(data);
        if (top == null) {
            top = newNode;
        } else {
            Node temp = top;
            while (temp.next != null) {
                temp = temp.next;
            }
            temp.next = newNode;
        }
    }

    // Delete from end
    public void deleteFromEnd() {
        if (top == null) {
            System.out.println("Stack is empty");
            return;
        }
        if (top.next == null) {
            top = null;
            return;
        }
        Node temp = top;
        while (temp.next.next != null) {
            temp = temp.next;
        }
        temp.next = null;
    }
    // Display stack
    public void display() {
        if (top == null) {
            System.out.println("Stack is empty");
            return;
        }
        Node temp = top;
        while (temp != null) {
            System.out.print(temp.data + " ");
            temp = temp.next;
        }
        System.out.println();
    }
}
// next step
public class InsertAtEndAndDel {
    public static void main(String[] args) {
        Stack stack = new Stack();
        stack.insertAtEnd(10);
        stack.insertAtEnd(20);
        stack.insertAtEnd(30);
        System.out.println("Stack after inserting elements:");
        stack.display();

        stack.deleteFromEnd();
        System.out.println("Stack after deleting from end:");
        stack.display();
    }
}