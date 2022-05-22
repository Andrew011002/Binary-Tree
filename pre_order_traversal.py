
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# traverse root, left subtree, then right subtree
def pre_order(root):
    order = []

    if root:

        order.append(root.val)
        order += pre_order(root.left)
        order += pre_order(root.right)

    return order


root = Node(88)
root.left = Node(5)
root.right = Node(100)
root.left.left = Node(2)
root.left.right = Node(7)
root.right.left = Node(90)
root.right.right = Node(200)
root.left.left.right = Node(6)
root.right.right.right = Node(201)

print(pre_order(root)) # [88, 5, 2, 6, 7, 100, 90, 200, 201]