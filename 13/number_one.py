from linked_list import LinkedList

# create a new linked list
llist = LinkedList()
 
# add nodes to the linked list
llist.insert_at_end('a')
llist.insert_at_end('b')
llist.insert_at_begin('c')
llist.insert_at_end('d')
llist.insert_at_index('g', 2)
 
# print the linked list
print("Node Data")
llist.print_LL()
 
# remove a nodes from the linked list
print("\nRemove First Node")
llist.remove_first_node()
print("Remove Last Node")
llist.remove_last_node()
print("Remove Node at Index 1")
llist.remove_at_index(1)
 
 
# print the linked list again
print("\nLinked list after removing a node:")
llist.print_LL()
 
print("\nUpdate node Value")
llist.update_node('z', 0)
llist.print_LL()
 
print("\nSize of linked list :", end=" ")
print(llist.size_of_LL())