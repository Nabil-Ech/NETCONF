import ipaddress
network = ipaddress.IPv4Network("10.10.0.0/24")
def generate_subnets(network, num_ips_list):
    sorted_ips_list = sorted(num_ips_list, reverse=True) # sorting the list if ip_num
    subnets = []
    power = 0
    for num_ips in sorted_ips_list:
        for x in range(32-ipaddress.IPv4Network("192.168.0.0/" + str(network.netmask)).prefixlen-1):
            if (pow(2, x)<= num_ips and num_ips < pow(2, x+1)):
                power = x+1
        print(num_ips, power, pow(2, power))
        subnet_prefix = network.prefixlen + (num_ips_router1 - 1).bit_length()




"""     subnet_prefix = network.prefixlen + (num_ips - 1).bit_length()
        subnet = ipaddress.IPv4Network((network.network_address, subnet_prefix))
        subnets.append(subnet)
        network = ipaddress.IPv4Network((subnet.network_address + subnet.num_addresses, network.prefixlen))
    
    return subnets"""

def generate_dhcp_server(network, subnet):
    dhcp_network = subnet.network_address
    dhcp_router = subnet.network_address + 1
    return dhcp_network, dhcp_router


num_ips_router1 = 50
num_ips_router2 = 100
num_ips_router3 = 49


network = ipaddress.IPv4Network("10.10.0.0/24")
print(network)
print("Network address:", network.network_address)
print("Subnet mask:", network.netmask)
print( num_ips_router2.bit_length() )

subnet_mask_ip = "255.255.255.0"

num_ips_list=[num_ips_router1, num_ips_router2, num_ips_router3]
subnet_prefix = network.prefixlen + (num_ips_router1 - 1).bit_length()
subnet = ipaddress.IPv4Network((network.network_address, subnet_prefix))
print("mio", network.prefixlen)
print(subnet)
print(32-ipaddress.IPv4Network(network.netmask).prefixlen)

burgir=generate_subnets(network, num_ips_list)
network = ipaddress.IPv4Network("10.10.0.0/24")

print("burgir", ipaddress.IPv4Network("192.168.0.0/" + str(network.netmask)).prefixlen)

"""def main():
    network = ipaddress.IPv4Network("10.10.0.0/24")
    num_ips_router1 = 100
    num_ips_router2 = 50
    num_ips_router3 = 49

    subnets = generate_subnets(network, [num_ips_router1, num_ips_router2, num_ips_router3])

    router1_subnet = subnets[0]
    router2_subnet = subnets[1]
    router3_subnet = subnets[2]

    router1_dhcp_network, router1_dhcp_router = generate_dhcp_server(network, router1_subnet)
    router2_dhcp_network, router2_dhcp_router = generate_dhcp_server(network, router2_subnet)
    router3_dhcp_network, router3_dhcp_router = generate_dhcp_server(network, router3_subnet)

    print("Router 1:")
    print("Interface IP:", router1_subnet.network_address)
    print("Subnet Mask:", router1_subnet.netmask)
    print("DHCP Server Network:", router1_dhcp_network)
    print("DHCP Server Default Router:", router1_dhcp_router)
    print()

    print("Router 2:")
    print("Interface IP:", router2_subnet.network_address)
    print("Subnet Mask:", router2_subnet.netmask)
    print("DHCP Server Network:", router2_dhcp_network)
    print("DHCP Server Default Router:", router2_dhcp_router)
    print()

    print("Router 3:")
    print("Interface IP:", router3_subnet.network_address)
    print("Subnet Mask:", router3_subnet.netmask)
    print("DHCP Server Network:", router3_dhcp_network)
    print("DHCP Server Default Router:", router3_dhcp_router)

if __name__ == "__main__":
    main()
"""