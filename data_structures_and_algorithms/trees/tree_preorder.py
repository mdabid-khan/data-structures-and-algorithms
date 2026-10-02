class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# ==============================
# Create Tree
# ==============================

root = TreeNode('A')
root.left = TreeNode('B')
root.right = TreeNode('C')

root.left.left = TreeNode('D')
root.left.right = TreeNode('E')
root.left.right.left = TreeNode('G')
root.left.right.right = TreeNode('H')

root.right.right = TreeNode('F')


# ==============================
# Preorder DFS (Root -> Left -> Right)
# ==============================

def preorder(node):
    if node is None:
        return
    
    print(node.value, end=" ")
    preorder(node.left)
    preorder(node.right)


# ==============================
# Run
# ==============================

if __name__ == "__main__":
    print("Preorder DFS:")
    preorder(root)