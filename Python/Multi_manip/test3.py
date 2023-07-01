class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def __str__(self, level=0):
        result = "  " * level + f"Node: {self.data}\n"
        for child in self.children:
            result += child.__str__(level + 1)
        return result


# Create the root node
root = TreeNode("Root")

# Add branches to the root node
branch1 = TreeNode("Branch 1")
branch2 = TreeNode("Branch 2")
branch3 = TreeNode("Branch 3")

root.add_child(branch1)
root.add_child(branch2)
root.add_child(branch3)

# Add sub-branches to Branch 1
subbranch1 = TreeNode("Sub-branch 1")
subbranch2 = TreeNode("Sub-branch 2")

branch1.add_child(subbranch1)
branch1.add_child(subbranch2)

# Add sub-branches to Branch 2
subbranch3 = TreeNode("Sub-branch 3")

branch2.add_child(subbranch3)

# Remove Branch 1 from the root node
root.remove_child(branch1)

# Print the tree structure
print("Tree structure:")
print(root)
