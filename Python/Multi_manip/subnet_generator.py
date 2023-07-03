class TreeNode:
    def __init__(self, prefix):
        self.prefix = prefix
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def remove_child(self, prefix):
        for child in self.children:
            if child.prefix == prefix:
                self.children.remove(child)
                return

    def __iter__(self):
        return iter(self.children)

    def create_subnets(self, mask):
        if mask > 32 or mask <= 0:
            return
        for i in range(2):
            subnet_prefix = f"/{mask}"
            subnet = TreeNode(subnet_prefix)
            self.add_child(subnet)
            subnet.create_subnets(mask + 1)

    def delete_subnet(self, mask):
        if self.prefix == f"/{mask}":
                self.parent.remove_child(self)
                return self

        for child in self.children:
                deleted_node = child.delete_subnet(mask)
                if deleted_node:
                    return deleted_node
            
        return None

    """def delete_subnet(self, mask):
        if self.prefix == f"/{mask}":
            #self.remove_child(self.prefix)
            self.create_subnets(self.prefix)
            
        self.children = [child for child in self.children if child.prefix != f"/{mask}"]
        for child in self.children:
            child.delete_subnet(mask)
            break
            
        return self"""
    

    """    def find_node_path(self, mask, path=None):
        if path is None:
            path = []

        if self.prefix == f"/{mask}":
            return path + [self.prefix]

        for child in self.children:
            child_path = child.find_node_path(mask, path + [self.prefix])
            if child_path:
                return child_path

        return None
    
    def delete_node(self, mask):
        path = self.find_node_path(mask)
        if path:
            current_node = self
            for prefix in path[:-1]:
                for child in current_node.children:
                    if child.prefix == prefix:
                        current_node = child
                        break
            for child in current_node.children:
                if child.prefix == path[-1]:
                    current_node.remove_child(child)
                    break"""
    """def delete_subnet(self, mask):
        path = []
        current_node = self
        while current_node:
            path.append(current_node.prefix)
            if current_node.prefix == f"/{mask}":
                break
            current_node = next((child for child in current_node.children if child.prefix == f"/{mask}"), None)
        
        if current_node and current_node == self:
            return None

        if current_node:
            parent = current_node.parent
            if parent:
                parent.remove_child(current_node)
        
        return self"""




    def __str__(self, level=0):
        result = "  " * level + f"Subnet: {self.prefix}\n"
        for child in self.children:
            result += child.__str__(level + 1)
        return result


# Prompt for the subnet mask
mask = input("Enter the subnet mask (1-32): ")
try:
    mask = int(mask)
    subnet_tree = TreeNode(f"/{mask}")
    subnet_tree.create_subnets(mask + 1)
    print("Subnet tree created:")
    print(subnet_tree)

    the_mask = input("Enter the subnet mask to delete (1-32): ")
    the_mask = int(the_mask)
    if the_mask <= mask:
        print("Invalid input. The mask to delete must be greater than the original mask.")
    else:
        subnet_tree.delete_subnet(the_mask)
        
    print("Updated subnet tree:")
    print(subnet_tree)

except ValueError:
    print("Invalid mask value. Please provide a valid integer between 1 and 32.")
