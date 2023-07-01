class TreeNode:
    def __init__(self, prefix):
        self.prefix = prefix
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)


    def create_subnets(self, mask):
        if mask > 32 or mask <= 0:
            return
        for i in range(2):
            subnet_prefix = f"/{mask}"
            subnet = TreeNode(subnet_prefix)
            self.add_child(subnet)
            subnet.create_subnets(mask + 1)

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

except ValueError:
    print("Invalid mask value. Please provide a valid integer between 1 and 32.")
