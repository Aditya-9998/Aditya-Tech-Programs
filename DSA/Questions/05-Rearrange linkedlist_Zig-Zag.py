# code for Rearrange the linkedlist in zig-zag fashion
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
        self.head.prev = None

    def zigzag(self):
        flag = True
        current = self.head

        while current and current.next:
            if flag:
                if current.data > current.next.data:
                    current.data, current.next.data = current.next.data, current.data
            else:
                if current.data < current.next.data:
                    current.data, current.next.data = current.next.data, current.data
            flag = not flag
            current = current.next
        return self.head
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()
# Example usage
if __name__ == "__main__":
    llist = LinkedList()
    llist.push(1)
    llist.push(2)
    llist.push(3)
    llist.push(4)
    llist.push(5)
    llist.push(6)

    print("Original Linked List:")
    llist.printList()

    llist.zigzag()

    print("Zig-Zag Linked List:")
    llist.printList()