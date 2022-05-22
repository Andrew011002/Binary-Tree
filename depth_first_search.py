
class Node:

    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def dfs(root):

    if root is None:
        return None

    order = ""
    stack = [root]
    visited = set()

    while stack:

        node = stack.pop()
        order += f"{node.val} -> "
        visited.add(node)

        
        if node.right:
            if node.right not in visited:
                stack.append(node.right)
        
        if node.left:
            if node.left not in visited:
                stack.append(node.left)
    
    return order + "/"

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)

    print(dfs(root)) # 1 -> 2 -> 4 -> 5 -> 3 -> 6 -> /



    

    


    
