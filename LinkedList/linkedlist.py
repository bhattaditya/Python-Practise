"""
Each element of a linked list is called a node. It has two fields.
fields
    data - contains the value to be stored in Node
    next - contains the reference/address of the next node
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return self.data

"""
linked list - collection of nodes. 
The first node is called the head, and it is used as the starting point for any iteration through the list. 
The last node must have its next reference pointing to None to determine the end of the list
"""

class LinkedList:
    # def __init__(self, nodes=None):
    #     self.head = None
    #     if nodes is not None:
    #         node = Node(data=nodes.pop(0))
    #         self.head = node
    #         for elem in nodes:
    #             node.next = Node(data=elem)
    #             node = node.next

    def __init__(self):
        self.head = None
        
    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception(f"Node with data {target_node_data} not found" )

    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception(f"Node with data {target_node_data} not found" )

    def add_last(self, node):

        # if linkedlist is empty
        if self.head is None:
            self.head = node
            return 

        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next

        current_node.next = node
    
    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = node.next
                return
            prev_node = node

        raise Exception(f"Node with data {target_node_data} not found")

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append('None')

        return " -> ".join(nodes)

    # traversing
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
        
if __name__ == "__main__":

    # creating  LinkedList class object
    linked = LinkedList()

    # Node objects 
    Node1 = Node('x')
    Node2 = Node('y')
    Node3 = Node('z')

    # making node1 as head/starting
    linked.head= Node1

    # linked list stores the address of the next node 
    Node1.next = Node2
    Node2.next = Node3

    # 100 -> 200 -> 300 -> None
    print(linked)

    print('Traversing linked list:')
    for node in linked:
        print(node)

    print('Add Node at start of linked list:')
    linked.add_first(Node('B'))
    linked.add_first(Node('A'))
    print(linked)

    print('Add Node at end of linked list:')
    linked.add_last(Node('YY'))
    linked.add_last(Node('ZZ'))
    print(linked)

    print('Adding after \'x\'')
    linked.add_after("x", Node("b"))
    print(linked)

    print('Adding before \'x\'')
    linked.add_before("x", Node("C"))
    print(linked)

    print('Removing \'x\'')
    linked.remove_node("x")
    print(linked)