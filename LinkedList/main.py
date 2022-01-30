"""
Node
    data - value to be stored in node
    next - contains the reference/ address of the next node
"""

from locale import currency


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

"""
Linked list - chain of Nodes.
"""

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if self.head is None:
            self.head = node
            return 
        
        currentNode = self.head
        while currentNode.next is not None:
            currentNode = currentNode.next
        currentNode.next = node
    
    def add_after(self, targetNodeValue, node):
        if self.head is None:
            print('Linked List is Empty')
            return

        current = self.head
        while current is not None:
            if current.data == targetNodeValue:
                break
            current = current.next
        if current is None:
            print(f"{targetNodeValue} not found")
        else:
            node.next = current.next
            current.next = node

    def add_before(self, targetNodeValue, node):
        if self.head is None:
            print('Linked List is Empty')
            return

        if self.head.data == targetNodeValue:
            return self.add_first(node)
            
        current = self.head
        while current is not None:
            if current.next.data == targetNodeValue:
                break
            current = current.next
        if current is None:
            print(f'{targetNodeValue} not found')
        else:
            node.next = current.next
            current.next = node

    def remove(self, targetNodeValue):
        if self.head is None:
            print('Linked List is Empty')
            return

        if self.head.data == targetNodeValue:
            self.head = self.head.next
            return
        
        current = self.head
        while current is not None:
            if current.next.data == targetNodeValue:
                break
            current = current.next
        if current is None:
            print(f'{targetNodeValue} not found')
        else:
            current.next = current.next.next

    def display(self):
        if self.head is None:
            print('Linked List is Empty')
            return
       
        currentNode = self.head
        while currentNode is not None:
            print(f'{currentNode.data} -> ', end='')
            currentNode = currentNode.next
        print('None')

if __name__ == "__main__":
    
    # ll = LinkedList()
    # # ll.display() - linked list empty
    
    # Node1 = Node(100)
    # ll.head = Node1

    # # ll.display() - 100

    # Node2 = Node(200)
    # Node3 = Node(300)
    
    # # linking above two nodes with head i.e Node1
    # Node1.next = Node2
    # Node2.next = Node3

    # ll.display()

    # print('adding new node (0) in the begining')
    # ll.add_first(Node(0))
    # ll.display()

    # print('adding new node (400) at the last')
    # ll.add_last(Node(400))
    # ll.display()

    # print('adding after node (200)')
    # ll.add_after(200, Node(10000))
    # ll.display()

    # print('adding before node (200)')
    # ll.add_before(0, Node(-150))
    # ll.display()

    ll = LinkedList()

    run = True
    while run:
        print('1. Add Node at begining\n2. Add node at last\n3. Add after node\n4. Add before node\n5. Remove node\n6. Display Linked List\n10. Exit\n\n')
        
        try:
            ch = int(input(":> "))
            if ch == 1:
                data = input("value: ")
                ll.add_first(Node(data))
                print('')
            elif ch == 2:
                data = input("value: ")
                ll.add_last(Node(data))
                print('')
            elif ch == 3:
                targetValue = input('target value: ')
                data = input("value: ")
                ll.add_after(targetValue, Node(data))
                print('')
            elif ch == 4:
                targetValue = input('target value: ')
                data = input("value: ")
                ll.add_before(targetValue, Node(data))
                print('')
            elif ch == 5:
                targetValue = input('target value: ')
                ll.remove(targetValue)
                print('')
            elif ch == 6:
                print('===================')
                ll.display()
                print('===================')
            elif ch == 10:
                run = False

            else:
                print('Not an Valid Input')
        except:
            print('Please enter integer')

        
        
