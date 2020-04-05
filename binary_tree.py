class Node(object):
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
class BinaryTree(object):
    def __init__(self,root):
        self.root = Node(root)

    def search(self,find_val):
        return self.preorder_search(node.root,find_val)

    def print_tree(self):
        return self.preorder_print(node.root,"")[:-1]

    def preorder_search(self,start,find_val):
        if start:
            if start.value == find_val:
                return True
            else:
                return self.preorder_search(start.left,find_val) or self.preorder_search(start.right,find_val)
        return False

    def preorder_print(self,start,traversal):
        if start:
            traversal += (str(start.value)+"-")
            traversal = self.preorder_print(start.left,traversal)
            traversal = self.preorder_print(start.right,traversal)
        return traversal

node = BinaryTree(1)
node.root.left= Node(2)
node.root.right=Node(3)
node.root.left.left=Node(4)
node.root.left.right=Node(5)
node.root.right.left=Node(6)
node.root.right.right=Node(7)

print(node.print_tree())
print(node.search(3))


