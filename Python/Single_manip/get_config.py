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


        
    netconf_reply = m.get_config(source = 'running')
    print (netconf_reply)

