# classes nessesary to make linked list

'''
A linked list is a type of linear data structure similar to arrays. It is a collection of nodes
that are linked with each other. A node contains two things first is data and second is a link that
connects it with another node. Our first node is where head points and we can access all the elements
of the linked list using the head.
'''


class Node:
    '''
    We have created a Node class, to initialize the node with the data passed as an argument and
    a reference with None because if we have only one node then there is nothing in its reference.
    '''
    def __init__(self, data):
        self.data = data
        self.next = None



class LinkedList:

    def __init__(self):
        self.head = None
    
    def insert_at_begin(self, data):
        '''
        This method inserts the node at the beginning of the linked list. In this method,
        we create a new_node with the given data
        '''
        new_node = Node(data)
        if self.head is None:
            # if the head is empty then we make the new_node as head
            self.head = new_node
            return
        else:
            # we insert the head at the next new_node and make the head equal to new_node
            new_node.next = self.head
            self.head = new_node
    
    def insert_at_index(self, data, index):
        '''
        This method inserts the node at the given index in the linked list
        '''
        new_node = Node(data)
        current_node = self.head
        position = 0
        if position == index:
            # Now, if the index is equal to zero it means the node is to be inserted at begin so we called insertAtBegin() method
            self.insertAtBegin(data)
        else:
            while(current_node != None and position+1 != index):
                position = position+1
                current_node = current_node.next
            '''
            When the loop breaks and if current_node is not equal to None we insert new_node at after to
            the current_node. If current_node is equal to None it means that the index is not present in
            the list and we print “Index not present”
            '''
            if current_node != None:
 
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("Index not present")
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            # if the head is empty then we make the new_node as head
            self.head = new_node
            return
        '''
        we make a current_node equal to the head traverse to the last node of the linked list and when we
        get None after the current_node the while loop breaks and insert the new_node in the next of
        current_node which is the last node of linked list
        '''
        current_node = self.head
        while(current_node.next):
            current_node = current_node.next
    
        current_node.next = new_node

    def update_node(self, val, index):
        '''
        used to update the value of a node at a given position in the linked list
        '''
        current_node = self.head
        position = 0
        if position == index:
            current_node.data = val
        else:
            while(current_node != None and position != index):
                position = position+1
                current_node = current_node.next
    
            if current_node != None:
                current_node.data = val
            else:
                print("Index not present")
    
    def remove_first_node(self):
        '''
        method removes the first node of the linked list simply by making
        the second node head of the linked list
        '''
        if(self.head == None):
            return
        
        self.head = self.head.next
    
    def remove_last_node(self):
        '''
        delete the last node
        first, we traverse to the second last node using the while loop, and then we make the next of
        that node None and last node will be removed
        '''
        if self.head is None:
            return
    
        current_node = self.head
        while(current_node.next.next):
            current_node = current_node.next
    
        current_node.next = None

    def remove_at_index(self, index):
        '''
        remove the node at the given index
        '''
        if self.head == None:
            return
 
        current_node = self.head
        position = 0
        if position == index:
            # If the position is equal to the index we called the remove_first_node() method
            self.remove_first_node()
        else:
            # else we traverse to the one node before that we want to remove using the while loop
            while(current_node != None and position+1 != index):
                position = position+1
                current_node = current_node.next
 
            if current_node != None:
                # we check that current_node is equal to None if not then we make the next of
                # current_node equal to the next of node that we want to remove
                current_node.next = current_node.next.next
            else:
                # current_node is equal to None
                print("Index not present")
    
    def remove_node(self, data):
        '''
        removes the node with the given data from the linked list
        '''
        current_node = self.head
    
        # Check if the head node contains the specified data
        if current_node.data == data:
            self.remove_first_node()
            return

        # while loop breaks when current_node becomes None or the data next to the current
        # node is equal to the data given in the argument
        while current_node is not None and current_node.next.data != data:
            current_node = current_node.next
    
        if current_node is None:
            # After coming out of the loop if the current_node is equal to None it means that
            # the node is not present in the data and we just return
            return
        else:
            # if the data next to the current_node is equal to the data given then we remove that
            # node by making next of that removed_node to the next of current_node
            current_node.next = current_node.next.next

    def print_LL(self):
        '''
        we made a current_node equal to the head and iterate through the linked list using a while loop
        until the current_node become None and print the data of current_node in each iteration and make
        the current_node next to it
        '''
        current_node = self.head
        while(current_node):
            print(current_node.data)
            current_node = current_node.next
    
    def size_of_LL(self):
        '''
        we have initialized a counter "size" with 0, and then if the head is not equal to None we traverse
        the linked list using a while loop and increment the size with 1 in each iteration and return the
        size when current_node becomes None else we return 0
        '''
        size = 0
        if(self.head):
            current_node = self.head
            while(current_node):
                size = size+1
                current_node = current_node.next
            return size
        else:
            return 0