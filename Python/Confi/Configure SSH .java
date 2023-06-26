enable
configure terminal

//Setting up the device to run SSH & configure SSH server


hostname Router // configure hostname and domain name
ip domain-name Router-domain
crypto key generate rsa modulus 2048 // enter modulus length of at least 1024, longer is more secure
ip ssh version 2 // configure the device to run SSHv2

line vty 0 4 // configure the virtual terminal line settings
login local
transport input all // allow all transport connections, include telnet, ssh
end // return to EXEC mode
show ip ssh // show version and conf info SSH server
show ssh // show the status of SSH server connections
configure terminal
username admin password nabil // create user and password for SSH client to access
username kimdoanh89 privilege 15 // set privilege privilege level 15 to the username ‘admin’,
// therefore it can directly enter the privileged EXEC mode without an enable password (indicated by the ‘#’ sign next to the router hostname)
exit
show running-config // verify the entries
copy running-config startup-config // save the entries in the conf fil


// SSH to the router on the local machine (management server)
ssh admin@192.168.1.1 -p 830 -s netconf
password: nabil