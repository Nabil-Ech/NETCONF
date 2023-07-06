import ipaddress

def generate_subnets(network, num_routers):
    num_ips_list=[]
    devices = {}
    for i in range(1, num_routers + 1):
        key = int(input(f"Enter the num_ips_router for Device{i}: "))
        num_ips_list.append(key)
        value = f"Device{i}"
        devices[key] = value
    sorted_ips_list = sorted(num_ips_list, reverse=True)
    subnets = []
    mask = []
    mask_dec = []
    power_list=[]
    default_router = []
    power = 0
    index = -1
    left_add=pow(2, 32-ipaddress.IPv4Network("192.168.0.0/" + str(network.netmask)).prefixlen)
    for num_ips in sorted_ips_list:
        for x in range(32-ipaddress.IPv4Network("192.168.0.0/" + str(network.netmask)).prefixlen-1):
            if (pow(2, x)<= num_ips and num_ips < pow(2, x+1)):
                power = x+1
        power_list.append(power)
    for i in range (num_routers):
        if left_add >= pow(2, power_list[i]):
            if i > 0 and power_list[i]==power_list[i-1] :
                subnet_prefix = network.prefixlen + (32-ipaddress.IPv4Network("192.168.0.0/" + str(network.netmask)).prefixlen-power_list[i])
                subnet = ipaddress.IPv4Network((network.network_address , subnet_prefix))
                new_subnet = subnets[-1]+pow(2, power_list[i]) 
                subnets.append(new_subnet)
                mask.append(subnet.netmask)
                mask_dec.append(subnet_prefix)
                default_router.append(new_subnet + 1)
                left_add = left_add - pow(2, power_list[i])
                print(devices[sorted_ips_list[i]])
                print("Interface IP:", default_router[index])
                print("Subnet Mask:", mask[index], "(",mask_dec[index],")")
                print("DHCP Server Network:", subnets[index])
                print("DHCP Server Default Router:", default_router[index])
                print()
            
            else: 
                subnet_prefix = network.prefixlen + (32-ipaddress.IPv4Network("192.168.0.0/" + str(network.netmask)).prefixlen-power_list[i])
                subnet = ipaddress.IPv4Network((network.network_address , subnet_prefix))
                new_subnet = subnet.network_address 
                subnets.append(new_subnet)
                mask.append(subnet.netmask)
                mask_dec.append(subnet_prefix)
                default_router.append(new_subnet + 1)
                left_add = left_add - pow(2, power_list[i])
                print(devices[sorted_ips_list[i]])
                print("Interface IP:", default_router[index])
                print("Subnet Mask:", mask[index], "(",mask_dec[index],")")
                print("DHCP Server Network:", subnets[index])
                print("DHCP Server Default Router:", default_router[index])
                print()
        else:
            print("No ip left for", devices[sorted_ips_list[i]])



network_input = input("Enter the network and subnet in CIDR notation (e.g., 10.10.0.0/23): ")
num_routers = int(input("Enter the number of routers: "))
network = ipaddress.IPv4Network(network_input)
generate_subnets(network, num_routers)

