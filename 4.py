'''Input: 4 -> 3 -> 2 -> 1 -> 0 -> NULL
Output: 0 -> 1 -> 2 -> 3 -> 4 -> NULL

Given a singly-linked list, reverse the list. This can be done iteratively or recursively. Can you get both solutions?


'''

class ListNode(object):
    stack = []

    def __init__(self, x):
        self.val = x
        self.next = None
  
  # Function to print the list
    def printList(self):
        node = self
        output = '' 
        while not self.stack:
            
        print(output)

  # Iterative Solution
    def reverseIteratively(self, head):
        while head.next is not None:
            self.stack.append(head.val)
        return self.stack
    # Implement this.

  # Recursive Solution      
    def reverseRecursively(self, head):
        return
    # Implement this.

# Test Program
# Initialize the test list: 
testHead = ListNode(4)
node1 = ListNode(3)
testHead.next = node1
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(1)
node2.next = node3
testTail = ListNode(0)
node3.next = testTail

print("Initial list: ")
testHead.printList()
# 4 3 2 1 0
testHead.reverseIteratively(testHead)
#testHead.reverseRecursively(testHead)
print("List after reversal: ")
testTail.printList()
# 0 1 2 3 4