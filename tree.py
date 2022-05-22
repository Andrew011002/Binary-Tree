class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Tree:

    def __init__(self):
        self.root = None

    # creates tree from array
    def create(self, array):
        # valid array
        if not array:
            return None
        
        self.root = Node(array.pop(0)) # set root
        queue = [self.root] # init queue
        # iterate while both queue nodes and array values exist
        while queue and array:      
            node = queue.pop(0) # grab node to give children
            # grab and set children if they exist
            for i in range(2):
                # left child value
                if array and not i:
                    left = array.pop(0)
                    # left child exist
                    if left:
                        l_node = Node(left)
                        queue.append(l_node)
                        node.left = l_node

                # right child value
                elif array:
                    right = array.pop(0)
                    # right child exist
                    if right:
                        r_node = Node(right)
                        queue.append(r_node)
                        node.right = r_node
    
    # adds node to first avalible spot using bfs
    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            queue = [self.root]
            # iterate while nodes
            while queue:
                node = queue.pop(0) # grab node
                # check for left and right spots (add children if not)
                if node.left:
                    queue.append(node.left)
                else:
                    node.left = Node(value) # open spot so add and break
                    break
                if node.right:
                    queue.append(node.right)
                else:
                    node.right = Node(value) # open spot so add and break
                    break

    # deletes node from tree if it exist
    def remove(self, value):
        # make sure node exist in tree
        if self.contains(value):
            queue = [self.root] # init queue for bfs

            # grab leaf object and value (to replace and delete deepest node)
            leaf = self.leaf() 
            val = leaf.val 
            # loop while nodes in queue:
            while queue:
                node = queue.pop(0)

                # delete the child if it's the deepest leaf (otherwise add it)
                if node.left:
                    if node.left is leaf:
                        node.left = None
                    else:
                        queue.append(node.left)
                
                if node.right:
                    if node.right is leaf:
                        node.right = None
                    else:
                        queue.append(node.right)

                # swap the deleted value with leafs value
                if val and node.val == value:
                    node.val = val
                    val = None
    
    # returns the deepest right-most leaf
    def leaf(self):
        if self.root is None:
            return None
        
        queue = [self.root] # init queue for bfs

        # loop while there's nodes
        while queue:
            node = queue.pop(0) # grab node
            # add possible children
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return node # return the leaf (node to delete)


    # checks if value is in a tree
    def contains(self, value, node=None, i=0):
        # first iteration case
        if not i:
            node = self.root
        # if we have a node check to see if the values much (return True)
        if node:
            if node.val == value:
                return True
            # try again for the left subtree and right subtree
            return self.contains(value, node.left, i=1) or self.contains(value, node.right, i=1)
                        
        return False # node was not found

    # copies tree w/o reference to one another
    def copy(self):
        # check for root
        if self.root is None:
            return None
        
        # copies tree
        tree = Tree() # init tree and queue for bfs
        queue = [self.root]
        in_order = []
        while queue:
            node = queue.pop(0) # grab node
            # add children (even if None) to queue and add node value or None to order
            if node:
                in_order.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                in_order.append(None)

        tree.create(in_order) # create tree from array and return it
        return tree

        
            
    # uses iterative dfs to find a node based on value or returns None
    def dfs(self, value):
        # check if there's a root (None if not)
        if self.root is None:
            return None

        stack = [self.root] # init stack for dfs
        # iterate while we have nodes on the stack
        while stack:
            # grab the value and check and see if it's our target, if it is return it
            node = stack.pop() 
            if node.val == value:
                return node
            # otherwise add the children
            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)
        
        return None # value not in tree
    
    # uses iterative bfs to find a node based on value or returns None
    def bfs(self, value):
        # check if there's a root (None if not)
        if self.root is None:
            return None

        queue = [self.root] # init queue for bfs
        # iterate while there's nodes in the queue
        while queue:
            # grab node and check if it's target it (return it if it is)
            node = queue.pop(0)
            if node.val == value:
                return node
            # otherwise add its children and check again
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return None # value not in tree

    # returns list of tree by pre-order traversal
    def pre_order(self, node=None, i=0):
        # check for root
        if self.root is None:
            return None

        order = [] # init list
        if not i: # case of first iteration
            node = self.root
        # traverse if there's a node
        if node: 
            order.append(node.val) # add root
            order += self.pre_order(node.left, i=1) # recur on left subtree
            order += self.pre_order(node.right, i=1) # recur on right subtree

        return order # return order after last node
            
    # returns list of tree by post-order traversal
    def post_order(self, node=None, i=0):
        # check for root
        if self.root is None:
            return None

        order = [] # init list for nodes
        if not i: # case of first iteration
            node = self.root
        # traverse if there's a node
        if node:
            order += self.post_order(node.left, i=1) # traverse left subtree
            order += self.post_order(node.right, i=1) # traverse right subtree
            order.append(node.val) # add root 

        return order # return order after last node
    
    # returns list of tree by in-order traversal
    def in_order(self, node=None, i=0):
        # check for root
        if self.root is None:
            return None
        order = [] # init list for nodes

        if not i: # case of first iteration
            node = self.root
        # traverse if there's a node
        if node:
            order = self.in_order(node.left, i=1) # recur on left and store
            order.append(node.val) # add root
            order += self.in_order(node.right, i=1) # recur on right
        
        return order # return order after last node

    # returns the depth of the tree using recursive dfs
    def __len__(self, node=None, i=0):
        if self.root is None:
            return None

        if not i: # case of first iteration
            node = self.root
        # no child
        if node is None:
            return 0
        # since we have a root we return 1 plus the max between the depth of children and their children
        return 1 + max(self.__len__(node.left, i=1), self.__len__(node.right, i=1)) 
        
    # prints the tree (credit to this posting: https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python @J.V.)
    def __str__(self, val="val", left="left", right="right"):
        def display(root, val=val, left=left, right=right):

            # No child.
            if getattr(root, right) is None and getattr(root, left) is None:
                line = f"{getattr(root, val)}"
                width = len(line)
                height = 1
                middle = width // 2
                return [line], width, height, middle

            # Only left child.
            if getattr(root, right) is None:
                lines, n, p, x = display(getattr(root, left))
                s = f"{getattr(root, val)}"
                u = len(s)
                first_line = (x + 1) * " " + (n - x - 1) * "_" + s
                second_line = x * " " + "/" + (n - x - 1 + u) * " "
                shifted_lines = [line + u * " " for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

            # Only right child.
            if getattr(root, left) is None:
                lines, n, p, x = display(getattr(root, right))
                s = f"{getattr(root, val)}"
                u = len(s)
                first_line = s + x * "_" + (n - x) * " "
                second_line = (u + x) * " " + "\\" + (n - x - 1) * " "
                shifted_lines = [u * " " + line for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

            # Two children.
            left, n, p, x = display(getattr(root, left))
            right, m, q, y = display(getattr(root, right))
            s = f"{getattr(root, val)}"
            u = len(s)
            first_line = (x + 1) * " " + (n - x - 1) * "_" + s + y * "_" + (m - y) * " "
            second_line = x * " " + "/" + (n - x - 1 + u + y) * " " + "\\" + (m - y - 1) * " "
            if p < q:
                left += [n * " "] * (q - p)
            elif q < p:
                right += [m * " "] * (p - q)
            zipped_lines = zip(left, right)
            lines = [first_line, second_line] + [a + u * " " + b for a, b in zipped_lines]
            return lines, n + m + u, max(p, q) + 2, n + u // 2

        tree = ""
        if self.root:
            lines, *_ = display(self.root, val, left, right)
            for line in lines:
                tree += f"{line}\n"
        
        return tree
        
if __name__ == "__main__":
    array = [1, 2, 3, None, 20, 21] # root = i left = 2 * i + 1 right = 2 * i + 2
    tree = Tree()
    tree.create(array)
    tree_2 = tree.copy()
    print(tree)
    print(tree.pre_order())
    tree.add(10)
    print(tree.dfs(10))
    print(tree)
    print(tree.in_order())
    tree.remove(21)
    print(tree)
    print(tree_2)
    print(tree.contains(2))
    print(tree_2.post_order())
    print(tree.bfs(3))