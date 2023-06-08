from ncclient import manager

# Define the device information
device = {
    "host": "192.168.1.1",       # Replace with the IP address or hostname of your device
    "port": 830,             # NETCONF port (default is 830)
    "username": "admin",  # Replace with your device's username
    "password": "nabil",  # Replace with your device's password
}

# Define the new hostname
new_hostname = "Cisco_1000v"

# Define the NETCONF configuration payload to change the hostname
config_xml = f"""
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <hostname>{new_hostname}</hostname>
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

    print("Hostname changed successfully.")
