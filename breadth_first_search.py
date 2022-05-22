class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def bfs(root):

    if root is None:
        return None

    queue = [root]
    order = ""

    while queue:
        node = queue.pop(0)
        order += f"{node.val} -> "

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)
    
    return order + "/"

if __name__ == "__main__":
    root = Node(11)
    root.left = Node(21)
    root.right = Node(43)
    root.left.left = Node(10)
    root.left.right = Node(88)
    root.right.left = Node(6)
    root.right.right = Node(50)

    print(bfs(root)) # 11 -> 21 -> 43 -> 10 -> 88 -> 6 -> 50 -> /






