# merge two linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def merge(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.data < list2.data:
            list1.next = self.merge(list1.next, list2)
            return list1
        else:
            list2.next = self.merge(list1, list2.next)
            return list2
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()
# Driver code
if __name__ == "__main__":
    list1 = LinkedList()
    list2 = LinkedList()
    list1.push(15)
    list1.push(10)
    list1.push(5)
    list2.push(20)
    list2.push(3)
    list2.push(2)

    print("First Linked List:")
    list1.printList()

    print("Second Linked List:")
    list2.printList()

    merged_list = LinkedList()
    merged_list.head = merged_list.merge(list1.head, list2.head)

    print("Merged Linked List:")
    merged_list.printList()