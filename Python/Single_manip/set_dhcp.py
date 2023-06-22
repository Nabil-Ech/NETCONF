from ncclient import manager

device = {
    "host": "192.168.1.20",   # Replace with the IP address or hostname of your device
    "port": 830,               # NETCONF port (default is 830)
    "username": "admin",       # Replace with your device's username
    "password": "nabil",       # Replace with your device's password
}

dhcp_pool_name = "server2"  # Name of the DHCP pool
network = "10.10.0.64"         # Network address
subnet_mask = "255.255.255.192"   # Subnet mask
default_router = "10.10.0.65"  # Default gateway
#dns_servers = "8.8.8.8"  # DNS server addresses

config_xml = f"""
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <ip>
        <dhcp>
            <pool xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-dhcp">
                <id>{dhcp_pool_name}</id>
                <default-router>
                    <default-router-list>{default_router}</default-router-list>
                </default-router>
                <network>
                    <primary-network>
                    <number>{network}</number>
                    <mask>{subnet_mask}</mask>
                    </primary-network>
                </network>
            </pool>
        </dhcp>
        </ip>
    </native>
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
