from ncclient import manager
import xmltodict
import xml.dom.minidom

with manager.connect(
        host="192.168.1.1",
        port=830,
        username="admin",
        password="nabil",
        hostkey_verify=False
        ) as m:


        
    for c in m.server_capabilities:
        print (c)