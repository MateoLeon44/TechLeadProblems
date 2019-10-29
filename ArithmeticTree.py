from queue import Queue

class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

PLUS = "+"
MINUS = "-"
TIMES = "*"
DIVIDE = "/"

def isOperator(string):
  if string == PLUS or string == MINUS or string == TIMES or string == DIVIDE:
    return True
  else:
    return False 


def evaluate(root):
  if root is None:
    return 0
  if not isOperator(root.val) and root.left == None and root.right == None:
    return root
  if isOperator(root.val) and root.left == None and root.right == None:
    return False
  left = evaluate(root.left)
  right = evaluate(root.right)
  if root.val == TIMES:
    return left*right 
  if root.val == DIVIDE:
    return left.val/right.val
  if root.val == PLUS:
    return left.val+right.val
  if root.val == MINUS:
    return left.val-right.val


tree = Node(TIMES)
tree.left = Node(PLUS)
tree.left.left = Node(3)
tree.left.right = Node(2)
tree.right = Node(PLUS)
tree.right.left = Node(4)
tree.right.right = Node(5)
print(evaluate(tree))