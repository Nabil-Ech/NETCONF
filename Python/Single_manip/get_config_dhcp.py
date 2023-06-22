from ncclient import manager
import xmltodict
import xml.dom.minidom


with manager.connect(
        host="192.168.1.20",
        port=830,
        username="admin",
        password="nabil",
        hostkey_verify=False
        ) as m:
# Specify the filter to retrieve only the DHCP configuration
    filter_xml = '''
        <filter>
            <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                <ip>
                    <dhcp></dhcp>
                </ip>
            </native>
        </filter>
    '''

    # Retrieve the DHCP configuration
    result = m.get_config(source='running', filter=filter_xml)

    # Print the configuration
    print(result.xml)