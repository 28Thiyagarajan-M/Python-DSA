class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return Node(key)
        else:
            if root.val < key:
                root.right = self.insert(root.right, key)
            else:
                root.left = self.insert(root.left, key)
        return root

    def minValueNode(self, node):
        current = node
        while(current.left is not None):
            current = current.left
        return current

    def delete(self, root, key):
        if root is None:
            return root
        if key < root.val:
            root.left = self.delete(root.left, key)
        elif(key > root.val):
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.val = self.minValueNode(root.right).val
            root.right = self.delete(root.right, root.val)
        return root

    def search(self, root, key):
        if root is None or root.val == key:
            return root
        if root.val < key:
            return self.search(root.right, key)
        return self.search(root.left, key)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val),
            self.inorder(root.right)

tree = BinaryTree()
tree.root = Node(50)
tree.insert(tree.root, 30)
tree.insert(tree.root, 20)
tree.insert(tree.root, 40)
tree.insert(tree.root, 70)
tree.insert(tree.root, 60)
tree.insert(tree.root, 80)

print("Inorder traversal of the given tree")
tree.inorder(tree.root)

print("\nDelete 20")
tree.root = tree.delete(tree.root, 20)
print("Inorder traversal of the modified tree")
tree.inorder(tree.root)

print("\nDelete 30")
tree.root = tree.delete(tree.root, 30)
print("Inorder traversal of the modified tree")
tree.inorder(tree.root)

print("\nDelete 50")
tree.root = tree.delete(tree.root, 50)
print("Inorder traversal of the modified tree")
tree.inorder(tree.root)

node = tree.search(tree.root, 60)
if node is not None:
    print("\nFound 60 in the tree")
else:
    print("\nDid not find 60 in the tree")
    
            
