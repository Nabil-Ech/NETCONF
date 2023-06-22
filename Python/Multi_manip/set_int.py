# The following code allow seting up the Gigaethernet interface for each DHCP server 

from ncclient import manager

device_IP_list=("192.168.1.10","192.168.1.20","192.168.1.30") #list of IP addresses for the 4 devices
int_IP_list=("10.10.0.1","10.10.0.65","10.10.0.129") # list of interface's Ip addresses

for i in range (0,3):
    # Define the device information
    device = {
        "host": device_IP_list[i],       # Replace with the IP address or hostname of your device
        "port": 830,             # NETCONF port (default is 830)
        "username": "admin",  # Replace with your device's username
        "password": "nabil",  # Replace with your device's password
    }

    # Define the new interface

    index = "GigabitEthernet2"
    ip_address= int_IP_list[i]
    mask = "255.255.255.192" # /26

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

        print("Interface of server", i+1 , "changed successfully.")