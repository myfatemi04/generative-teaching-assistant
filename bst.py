class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(data, node.right)

def generate_mermaid_diagram(node):
    if node is None:
        return ""

    mermaid_str = ""
    if node.left:
        mermaid_str += f"{node.data}(( {node.data} )) --> {node.left.data}(( {node.left.data} ))\n"
        mermaid_str += generate_mermaid_diagram(node.left)
    if node.right:
        mermaid_str += f"{node.data}(( {node.data} )) --> {node.right.data}(( {node.right.data} ))\n"
        mermaid_str += generate_mermaid_diagram(node.right)
    return mermaid_str
