import ipaddress

"""subnet_mask_ip = "255.255.255.0"

prefix_length = ipaddress.IPv4Network("192.168.0.0/" + subnet_mask_ip).prefixlen

print("Prefix length:", prefix_length)"""






def generate_subnets(network, num_ips_list):
    sorted_ips_list = sorted(num_ips_list, reverse=True) # sorting the list if ip_num
    subnets = []
    power = 0
    for num_ips in sorted_ips_list:
        for x in range(32-ipaddress.IPv4Network("192.168.0.0/" + str(network.netmask)).prefixlen-1):
            if (pow(2, x)<= num_ips and num_ips < pow(2, x+1)):
                power = x+1
        print(num_ips, power, pow(2, power))

num_ips_router1 = 50
num_ips_router2 = 100
num_ips_router3 = 49


num_ips_list=[num_ips_router1, num_ips_router2, num_ips_router3]
network = ipaddress.IPv4Network("10.10.0.0/24")

generate_subnets(network, num_ips_list)