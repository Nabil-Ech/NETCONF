from ncclient import manager

# Define the device information
device = {
    "host": "192.168.1.20",       # Replace with the IP address or hostname of your device
    "port": 830,             # NETCONF port (default is 830)
    "username": "admin",  # Replace with your device's username
    "password": "nabil",  # Replace with your device's password
}

# Define the new interface

index = "GigabitEthernet2"
ip_address= "10.10.0.65"
mask = "255.255.255.192"

# Define the NETCONF configuration payload to change the interface
config_xml = f"""
<config>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
            <name>{index}</name>
            <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                <address>
                    <ip>{ip_address}</ip>
                    <netmask>{mask}</netmask>
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
        
print("Interface changed successfully.")
    
