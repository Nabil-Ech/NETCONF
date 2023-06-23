def write_values_to_file(values, filename):
    with open(filename, 'w') as file:
        file.write(','.join(map(str, values)))
def read_values_from_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
    values = data.split(',')
    return values

new_ip_address = ["10.10.0.1", "10.10.0.65", "10.10.0.129"]  
new_subnet_mask = ["255.255.255.192"]
old_ip_address = ["192.168.100.1", "10.10.0.65", "192.168.2.2"]
old_subnet_mask = ["255.255.255.0", "255.255.255.192", "255.255.255.0"]
old_pool_name = ["server1","server3","server2"]


# Write the old IP addresses to a file
write_values_to_file(old_pool_name,'old_pool.txt')


# Read the values from the file
"""read_values = read_values_from_file('old_ip.txt')
for i in range (3):
    print(read_values[i])  # Print the read values from the file"""
