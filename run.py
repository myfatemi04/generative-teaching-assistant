class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

def to_mermaid(root):
    if root is None:
        return ""
    left_mermaid = to_mermaid(root.left)
    right_mermaid = to_mermaid(root.right)
    return f"{root.value} --> {left_mermaid}\n{root.value} --> {right_mermaid}"

if __name__ == "__main__":
    root = insert(None, 4)
    insert(root, 2)
    insert(root, 6)
    insert(root, 1)
    insert(root, 3)
    print(to_mermaid(root))
