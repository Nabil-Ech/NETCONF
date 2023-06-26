// Step 1: Configure the interface 0/0 in the Inside Global as

conf t
int FastEthernet 0/0
ip nat inside
exit

//Step 2: Configure the interface 1/0 in the Inside Local as

int FastEthernet 1/0
ip nat outside
exit

//Step 3: Create a pool of Global IP addresses:

ip nat pool <pool-name = POOL> <starting-IP = 192.168.2.1> <ending-IP = 192.168.2.100> netmask 255.255.255.0 

//0Step 4: Create an access list to permit a certain network of IP addresses:

access-list <acl-number = 1>
permit <source-ip-network = 192.168.1.0> <wildcard-mask = 0.0.0.255>

//NOTE:The access list configured above matches all hosts from the 192.168.1.0/24 subnet.*

//Step 5: Lastly, enable Dynamic NAT by using the command:

ip nat inside source
list <acl-number = 1> pool <pool-name = POOL>
exit
end 

//Step 6: Login into one the host and ping an address from the POOL (ex = 192.168.2.5)

ping 192.168.2.5

//Now, and at the same time, verify the NAT translations (to show the translations done by NAT):

show ip nat translations
