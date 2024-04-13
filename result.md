## Understanding Binary Tree Insertion

Hey there!  Inserting into a binary tree involves some key rules to maintain its structure and ordering.  Let's break it down step-by-step and visualize it along the way!

First, let's create a Binary Search Tree (BST) to work with:

```python
from bst import BinarySearchTree, generate_mermaid_diagram

bst = BinarySearchTree()  # Initialize an empty BST
```

Now, let's visualize our empty BST:

```python
print("Empty BST:")
display(generate_mermaid_diagram(bst.root))
```

### The Insertion Process

1. **Empty Tree:** If the tree is empty (the root is `None`), the inserted node becomes the root. 

2. **Non-Empty Tree:** 
    * **Comparison:** We compare the data of the new node with the root node's data.
    * **Navigation:**
        * If the data is **less** than the root's data, we move to the **left subtree** and repeat the comparison and navigation process.
        * If the data is **greater** than the root's data, we move to the **right subtree** and repeat the comparison and navigation process.
    * **Insertion:** We continue this process until we find an empty spot (a `None` child node) where we can insert the new node. 

Let's see this in action!

### Example: Inserting Values

Let's insert the value `8` into our BST:

```python
bst.insert(8)
print("Inserting 8:")
display(generate_mermaid_diagram(bst.root))
```

Now, let's insert `3` and then `10`: 

```python
bst.insert(3)
print("Inserting 3:")
display(generate_mermaid_diagram(bst.root))

bst.insert(10)
print("Inserting 10:")
display(generate_mermaid_diagram(bst.root))
```

As you can see, the `3` was inserted to the left of `8` because it's smaller, and `10` was inserted to the right because it's larger.  This maintains the **ordering property** of the BST, where the left subtree always contains smaller values and the right subtree contains larger values.

Let me know if you have any other questions or want to visualize more insertions! 