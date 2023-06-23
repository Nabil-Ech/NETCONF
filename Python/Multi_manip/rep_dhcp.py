# This code will allow to delete the old dhcp server and set a new one for each router 
from ncclient import manager



def write_values_to_file(values, filename):
    with open(filename, 'w') as file:
        file.write(','.join(map(str, values)))
def read_values_from_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
    values = data.split(',')
    return values


device_IP_list=("192.168.1.10","192.168.1.20","192.168.1.30") #list of IP addresses for the 4 devices
new_pool=[]
default_router=[]
old_pool_name = read_values_from_file("old_pool.txt")

for i in rang (3):
    device = {
        "host": device_IP_list[i],   # Replace with the IP address or hostname of your device
        "port": 830,               # NETCONF port (default is 830)
        "username": "admin",       # Replace with your device's username
        "password": "nabil",       # Replace with your device's password
    }
    config_xml = f"""
    <config>
        <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
            <ip>
                <dhcp>
                    <pool xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-dhcp" nc:operation="delete" xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
                        <id>{old_pool_name[i]}</id>
                    </pool>
                    <pool xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-dhcp">
                        <id>{new_pool[i]}</id>
                        <default-router>
                            <default-router-list>{default_router[i]}</default-router-list>
                        </default-router>
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

write_values_to_file(new_pool, "old_pool.txt")

