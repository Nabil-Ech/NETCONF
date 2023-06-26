configure terminal
ip dhcp pool MyPool // define the pool, the name 
network 192.168.1.0 255.255.255.0 // add the subnet 192.168.2.0/24
default-router 192.168.2.1 // configure the default gateway for this subnet 
exit 
ip dhcp excluded-address 192.168.2.10 192.168.2.20 //to exclud some addresses from 10 to 20


// you might as well add some a DNS server and the domain (before line 5)
dns-server "address" "address"
domain "your domain"