class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        temp = self.head
        while(temp):
            print(temp.value)
            temp = temp.next

if __name__ == "__main__":

    # creating  LinkedList class object
    linked = LinkedList()

    # created two more objects of Node
    Node1 = Node(100)
    Node2 = Node(200)
    Node3 = Node(300)

    # making node1  as head
    linked.head = Node1

    # linked list stores the address of the next node 
    Node1.next = Node2
    Node2.next = Node3

    # 100 -> 200 -> 300 -> None
    linked.display()


