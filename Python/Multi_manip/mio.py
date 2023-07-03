class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def find_path_to_branch(self, branch_name, path=[]):
        if self.data == branch_name:
            return path + [self.data]

        for child in self.children:
            found_path = child.find_path_to_branch(branch_name, path + [self.data])
            if found_path:
                return found_path

        return None

    def access_branch_by_path(self, path):
        current_node = self
        for node_name in path:
            found_child = None
            for child in current_node.children:
                if child.data == node_name:
                    found_child = child
                    break
            if found_child:
                current_node = found_child
            else:
                return None
        return current_node

    def delete_branch_by_path(self, path):
        if len(path) == 0:
            return False

        node_name = path[0]
        for child in self.children:
            if child.data == node_name:
                if len(path) == 1:
                    self.remove_child(child)
                    return True
                else:
                    return child.delete_branch_by_path(path[1:])
        
        return False

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

mio = TreeNode("mio")

subbranch1.add_child(mio)
subbranch1.add_child(mio)

# Add sub-branches to Branch 2
subbranch3 = TreeNode("Sub-branch 3")

branch2.add_child(subbranch3)
subbranch2.add_child(mio)
subbranch2.add_child(mio)
subbranch3.add_child(mio)

# Print the tree structure
print("Tree structure:")
print(root)

# Find the path to the first occurrence of "mio"
path_to_mio = root.find_path_to_branch("mio")
print("Path to mio branch:", path_to_mio)

# Delete the mio branch using the obtained path
deleted = root.delete_branch_by_path(path_to_mio)
if deleted:
    print("mio branch deleted.")
else:
    print("mio branch not found or cannot be deleted.")

# Print the updated tree structure
print("\nUpdated tree structure:")
print(root)
