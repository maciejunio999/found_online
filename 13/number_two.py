class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = cur = ListNode(0)
        carry = 0

        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry % 10)
            cur = cur.next
            carry //= 10

        return dummy.next

# Example linked list class
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = ListNode(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def insert_at_begin(self, data):
        new_node = ListNode(data)
        new_node.next = self.head
        self.head = new_node

# Example usage
llist_1 = LinkedList()
llist_1.insert_at_end(1)
llist_1.insert_at_end(2)
llist_1.insert_at_begin(3)
llist_1.insert_at_end(4)

llist_2 = LinkedList()
llist_2.insert_at_end(2)
llist_2.insert_at_end(1)
llist_2.insert_at_begin(0)
llist_2.insert_at_end(3)

s = Solution()
result = s.addTwoNumbers(llist_1.head, llist_2.head)

# Print the result
while result:
    print(result.val, end=" ")
    result = result.next
