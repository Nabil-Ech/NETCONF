from ncclient import manager

device = {
    "host": "192.168.1.30",   # Replace with the IP address or hostname of your device
    "port": 830,               # NETCONF port (default is 830)
    "username": "admin",       # Replace with your device's username
    "password": "nabil",       # Replace with your device's password
}

old_pool_name = "pool1"

config_xml = f"""
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <ip>
            <dhcp>
                <pool xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-dhcp" nc:operation="delete" xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
                    <id>{old_pool_name}</id>
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
