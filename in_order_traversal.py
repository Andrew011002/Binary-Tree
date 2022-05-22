class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def in_order(root):
    order = []

    if root:

        order = in_order(root.left)
        order.append(root.val)
        order += in_order(root.right)

    return order

if __name__ == "__main__":
    root = Node(99)
    root.left = Node(7)
    root.right = Node(120)
    root.left.left = Node(4)
    root.left.right = Node(11)
    root.right.left = Node(67)
    root.right.right = Node(121)

    print(in_order(root)) # [4, 7, 11, 99, 67, 120, 121]


                    
                    