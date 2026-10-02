class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# ==============================
# Create the Tree
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
# DFS Traversals
# ==============================

# Preorder (Root -> Left -> Right)
def preorder(node):
    if node is None:
        return
    print(node.value, end=" ")
    preorder(node.left)
    preorder(node.right)


# Inorder (Left -> Root -> Right)
def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.value, end=" ")
    inorder(node.right)


# Postorder (Left -> Right -> Root)
def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.value, end=" ")


# ==============================
# Run
# ==============================

if __name__ == "__main__":
    print("Preorder (DFS):")
    preorder(root)

    print("\n\nInorder (DFS):")
    inorder(root)

    print("\n\nPostorder (DFS):")
    postorder(root)