import ipaddress





def generate_subnets(network, num_ips_list):
    devices = {
    num_ips_router1: "Device1",
    num_ips_router2: "Device2",
    num_ips_router3: "Device3"
    }
    sorted_ips_list = sorted(num_ips_list, reverse=True)
    subnets = []
    mask = []
    mask_dec = []
    power_list=[]
    default_router = []
    power = 0
    index = 0
    for num_ips in sorted_ips_list:
        for x in range(32-ipaddress.IPv4Network("192.168.0.0/" + str(network.netmask)).prefixlen-1):
            if (pow(2, x)<= num_ips and num_ips < pow(2, x+1)):
                power = x+1
        power_list.append(power)
    #print(power_list)
    if (power_list[0]<32-ipaddress.IPv4Network("192.168.0.0/" + str(network.netmask)).prefixlen):
        if (power_list[1] == power_list[2] and power_list[0] > power_list[1]):
            L=[0,0,pow(2, power_list[2])]
            for i in range (3):
                subnet_prefix = network.prefixlen + (32-ipaddress.IPv4Network("192.168.0.0/" + str(network.netmask)).prefixlen-power_list[i])
                subnet = ipaddress.IPv4Network((network.network_address , subnet_prefix))
                new_subnet = subnet.network_address + L[i]
                subnets.append(new_subnet)
                mask.append(subnet.netmask)
                mask_dec.append(subnet_prefix)
                default_router.append(new_subnet + 1)
                
        elif (power_list[0]>power_list[1] and power_list[1]>power_list[2]):
            for i in range (3):
                subnet_prefix = network.prefixlen + (32-ipaddress.IPv4Network("192.168.0.0/" + str(network.netmask)).prefixlen-power_list[i])
                subnet = ipaddress.IPv4Network((network.network_address , subnet_prefix))
                new_subnet = subnet.network_address 
                subnets.append(new_subnet)
                mask.append(subnet.netmask)
                mask_dec.append(subnet_prefix)
                default_router.append(new_subnet + 1)
        elif (32-ipaddress.IPv4Network("192.168.0.0/" + str(network.netmask)).prefixlen-1>power_list[0] and power_list[0]==power_list[1] and power_list[1]>power_list[2]):
            L=[0,pow(2, power_list[1]),0]
            for i in range (3):
                subnet_prefix = network.prefixlen + (32-ipaddress.IPv4Network("192.168.0.0/" + str(network.netmask)).prefixlen-power_list[i])
                subnet = ipaddress.IPv4Network((network.network_address , subnet_prefix))
                new_subnet = subnet.network_address + L[i]
                subnets.append(new_subnet)
                mask.append(subnet.netmask)
                mask_dec.append(subnet_prefix)
                default_router.append(new_subnet + 1)    
        elif (32-ipaddress.IPv4Network("192.168.0.0/" + str(network.netmask)).prefixlen-1>power_list[0] and power_list[0]==power_list[1] and power_list[1]==power_list[2]):
            L=[0,pow(2, power_list[1]),2*pow(2, power_list[1])]
            for i in range (3):
                subnet_prefix = network.prefixlen + (32-ipaddress.IPv4Network("192.168.0.0/" + str(network.netmask)).prefixlen-power_list[i])
                subnet = ipaddress.IPv4Network((network.network_address , subnet_prefix))
                new_subnet = subnet.network_address + L[i]
                subnets.append(new_subnet)
                mask.append(subnet.netmask)
                mask_dec.append(subnet_prefix)
                default_router.append(new_subnet + 1)     
        else :
            print("This combination is impossible")     
    else :
        print("This combination is impossible") 
    for num_ips in sorted_ips_list:
        print(devices[num_ips])
        print("Interface IP:", default_router[index])
        print("Subnet Mask:", mask[index], "(",mask_dec[index],")")
        print("DHCP Server Network:", subnets[index])
        print("DHCP Server Default Router:", default_router[index])
        print()
        index = index +1


#nissrine



num_ips_router1 = int(input("Enter the number of IP adresses for Device1: "))
num_ips_router2 = int(input("Enter the number of IP adresses for Device2: "))
num_ips_router3 = int(input("Enter the number of IP adresses for Device3: "))



#big_network = input("Enter the subnet (X.X.X.X/Y): ")

num_ips_list=[num_ips_router1, num_ips_router2, num_ips_router3]


#network = ipaddress.IPv4Network(big_network)

network = ipaddress.IPv4Network("10.10.0.0/24")



generate_subnets(network, num_ips_list)

