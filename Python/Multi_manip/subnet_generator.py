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

    """def delete_subnet(self, mask):
        if self.prefix == f"/{mask}":
            return None
        for i, child in enumerate(self.children):
            if child.prefix == f"/{mask}":
                self.remove_child(child)
                return self
            result = child.delete_subnet(mask)
            if result is None:
                self.remove_child(child)
                break
        return self"""
    def delete_subnet(self, mask):
        if self.prefix == f"/{mask}":
            return None
        self.children = [child for child in self.children if child.prefix != f"/{mask}"]
        for child in self.children:
            child.delete_subnet(mask)
            
        return self


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
