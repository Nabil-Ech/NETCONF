from ncclient import manager

device = {
    "host": "192.168.1.10",   # Replace with the IP address or hostname of your device
    "port": 830,               # NETCONF port (default is 830)
    "username": "admin",       # Replace with your device's username
    "password": "nabil",       # Replace with your device's password
}

interface_name = "GigabitEthernet2"  # Replace with the interface name you want to modify
old_ip_address = "192.168.100.1"
old_subnet_mask = "255.255.255.0"
new_ip_address = "10.10.0.1"
new_subnet_mask = "255.255.255.192"

config_xml = f"""
<config>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
            <name>{interface_name}</name>
            <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                <address nc:operation="delete" xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
                    <ip>{old_ip_address}</ip>
                    <netmask>{old_subnet_mask}</netmask>
                </address>
                <address nc:operation="merge" xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
                    <ip>{new_ip_address}</ip>
                    <netmask>{new_subnet_mask}</netmask>
                </address>
            </ipv4>
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





        