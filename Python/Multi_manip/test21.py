import ipaddress

"""subnet_mask_ip = "255.255.255.0"

prefix_length = ipaddress.IPv4Network("192.168.0.0/" + subnet_mask_ip).prefixlen

print("Prefix length:", prefix_length)"""






def generate_subnets(network, num_ips_list):
    sorted_ips_list = sorted(num_ips_list, reverse=True) # sorting the list if ip_num
    subnets = []
    power_list=[]
    power = 0
    for num_ips in sorted_ips_list:
        for x in range(32-ipaddress.IPv4Network("192.168.0.0/" + str(network.netmask)).prefixlen-1):
            if (pow(2, x)<= num_ips and num_ips < pow(2, x+1)):
                power = x+1
        power_list.append(power)
        print(num_ips, power, pow(2, power))
    #print(power_list)
    if (power_list[0]<32-ipaddress.IPv4Network("192.168.0.0/" + str(network.netmask)).prefixlen):
        if (power_list[1] == power_list[2] and power_list[0] > power_list[1]):
            L=[0,0,pow(2, power_list[2])]
            for i in range (3):
                subnet_prefix = network.prefixlen + (32-ipaddress.IPv4Network("192.168.0.0/" + str(network.netmask)).prefixlen-power_list[i])
                subnet = ipaddress.IPv4Network((network.network_address , subnet_prefix))
                x=subnet.network_address + L[i], str("/"), subnet_prefix
                print (subnet.network_address + L[i], subnet_prefix)
                print (x)
                #network = ipaddress.IPv4Network((subnet.network_address + subnet.num_addresses, network.prefixlen))
        elif (power_list[0]>power_list[1] and power_list[1]>power_list[2]):
            for i in range (3):
                subnet_prefix = network.prefixlen + (32-ipaddress.IPv4Network("192.168.0.0/" + str(network.netmask)).prefixlen-power_list[i])
                subnet = ipaddress.IPv4Network((network.network_address , subnet_prefix))
                x=subnet.network_address, str("/"), subnet_prefix
                print (subnet.network_address, subnet_prefix)
                print (x)
        elif (32-ipaddress.IPv4Network("192.168.0.0/" + str(network.netmask)).prefixlen-1>power_list[0] and power_list[0]==power_list[1] and power_list[1]>power_list[2]):
            L=[0,pow(2, power_list[1]),0]
            for i in range (3):
                subnet_prefix = network.prefixlen + (32-ipaddress.IPv4Network("192.168.0.0/" + str(network.netmask)).prefixlen-power_list[i])
                subnet = ipaddress.IPv4Network((network.network_address , subnet_prefix))
                x=subnet.network_address + L[i], str("/"), subnet_prefix
                print (subnet.network_address + L[i], subnet_prefix)
                print (x)    
        elif (32-ipaddress.IPv4Network("192.168.0.0/" + str(network.netmask)).prefixlen-1>power_list[0] and power_list[0]==power_list[1] and power_list[1]==power_list[2]):
            L=[0,pow(2, power_list[1]),2*pow(2, power_list[1])]
            for i in range (3):
                subnet_prefix = network.prefixlen + (32-ipaddress.IPv4Network("192.168.0.0/" + str(network.netmask)).prefixlen-power_list[i])
                subnet = ipaddress.IPv4Network((network.network_address , subnet_prefix))
                x=subnet.network_address + L[i], str("/"), subnet_prefix
                print (subnet.network_address + L[i], subnet_prefix)
                print (x)      
        else :
            print("This combination is impossible")     
    else :
        print("This combination is impossible") 
   





    


num_ips_router1 = 50
num_ips_router2 = 40
num_ips_router3 = 35


num_ips_list=[num_ips_router1, num_ips_router2, num_ips_router3]
network = ipaddress.IPv4Network("10.10.0.0/24")

generate_subnets(network, num_ips_list)