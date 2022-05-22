

class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
# traversal algorithm for deleting a node from a binary tree 
def post_order(root):
    order = []
    if root:
        order += post_order(root.left) # traverse left subtree
        order += post_order(root.right) # traverse right subtree
        order.append(root.val) # obtain the value of the current node

    return order

if __name__ == "__main__":
    root = Node(11)
    root.left = Node(55)
    root.right = Node(18)
    root.left.left = Node(2)
    root.left.right = Node(99)
    root.right.left = Node(101)
    root.right.right = Node(8)

    print(post_order(root)) # [2, 99, 55, 101, 8, 18, 11]