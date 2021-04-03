class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def lca(root, n1, n2):
    while root:
        if root.data > n1 and root.data > n2:
            root = root.left
        elif root.data < n1 and root.data < n2:
            root = root.right
        else:
            break

    return root


root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)

n1 = 10
n2 = 14
t = lca(root, n1, n2)
print("LCA of %d and %d is %d" % (n1, n2, t.data))

n1 = 14
n2 = 8
t = lca(root, n1, n2)
print("LCA of %d and %d is %d" % (n1, n2, t.data))

n1 = 10
n2 = 22
t = lca(root, n1, n2)
print("LCA of %d and %d is %d" % (n1, n2, t.data))
