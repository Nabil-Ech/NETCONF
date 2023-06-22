from ncclient import manager

device = {
    "host": "192.168.1.10",   # Replace with the IP address or hostname of your device
    "port": 830,               # NETCONF port (default is 830)
    "username": "admin",       # Replace with your device's username
    "password": "nabil",       # Replace with your device's password
}


interface_name = "GigabitEthernet2"  # Replace with the interface name you want to modify
device_IP_list=("192.168.1.10","192.168.1.20","192.168.1.30") #list of IP addresses for the 4 devices

new_ip_address=("10.10.0.1","10.10.0.65","10.10.0.129") # list of interface's Ip addresses
new_subnet_mask = ["255.255.255.192"]
old_ip_address=["192.168.100.1","10.10.0.65","192.168.2.2"]
old_subnet_mask=["255.255.255.0","255.255.255.192","255.255.255.0"]






config_xml = f"""
<config>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
            <name>{interface_name[i]}</name>
            <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                <address nc:operation="delete" xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
                    <ip>{old_ip_address[i]}</ip>
                    <netmask>{old_subnet_mask[i]}</netmask>
                </address>
                <address nc:operation="merge" xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
                    <ip>{new_ip_address[i]}</ip>
                    <netmask>{new_subnet_mask[i]}</netmask>
                </address>
            </ipv4>
                <enabled>true</enabled>
        </interface>
    </interfaces>
</config>
"""


    # Connect to the device and lock the candidate configuration datastore
with manager.connect(**device, hostkey_verify=False) as m:
        # Lock the candidate datastore
        m.lock('candidate')

        # Edit the configuration in the candidate datastore
        m.edit_config(target='candidate', config=config_xml)

        # Validate the candidate configuration
        m.validate()

        # Commit the candidate configuration to apply the changes
        m.commit()

        # Unlock the candidate datastore
        m.unlock('candidate')





        