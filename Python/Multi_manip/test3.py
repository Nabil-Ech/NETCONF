import ipaddress

def allocate_subnets(network, num_ips_list):
    sorted_ips_list = sorted(num_ips_list, reverse=True)
    subnets = []
    dhcp_networks = []
    default_routers = []
    dhcp_servers = []

    for num_ips in sorted_ips_list:
        subnet_prefix = network.prefixlen
        while 2 ** (32 - subnet_prefix) < num_ips:
            subnet_prefix += 1
        
        subnet = ipaddress.IPv4Network((network.network_address, subnet_prefix))
        subnets.append(subnet)

        dhcp_networks.append(str(subnet.network_address) + '/' + str(subnet_prefix))
        default_routers.append(str(subnet.network_address + 1))
        dhcp_servers.append(str(subnet.network_address + 2))

        network = ipaddress.IPv4Network((subnet.network_address + subnet.num_addresses, network.prefixlen))

    return subnets, dhcp_networks, default_routers, dhcp_servers

def main():
    network = ipaddress.IPv4Network("10.10.0.0/24")
    num_ips_router1 = 100
    num_ips_router2 = 50
    num_ips_router3 = 50

    subnets, dhcp_networks, default_routers, dhcp_servers = allocate_subnets(network, [num_ips_router1, num_ips_router2, num_ips_router3])

    print("Router 1 - Subnet:", subnets[0])
    print("        - DHCP Network:", dhcp_networks[0])
    print("        - Default Router:", default_routers[0])
    print("        - DHCP Server:", dhcp_servers[0])

    print("Router 2 - Subnet:", subnets[1])
    print("        - DHCP Network:", dhcp_networks[1])
    print("        - Default Router:", default_routers[1])
    print("        - DHCP Server:", dhcp_servers[1])

    print("Router 3 - Subnet:", subnets[2])
    print("        - DHCP Network:", dhcp_networks[2])
    print("        - Default Router:", default_routers[2])
    print("        - DHCP Server:", dhcp_servers[2])

if __name__ == '__main__':
    main()
