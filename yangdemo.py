# https://www.youtube.com/watch?v=kESU4Y8DJ2A
# https://devnetsandbox.cisco.com/RM/Topology
# Lab: IOS-XR 9000v Always On:
# Model Driven Programmability with YANG Data Models and NETCONF
# https://developer.cisco.com/site/standard-network-devices/

from ncclient import manager
import xml.etree.ElementTree as ET

router = {"host": "ios-xe-mgmt.cisco.com", "port": "10000", "username": "developer", "password": "C1sco12345"}
          
with manager.connect(host=router['host'], port=router['port'], username=router['username'], \
        password=router['password'], hostkey_verify=False) as m:
    # we want to grab a yang data model called ietf-ip for how IP addresses are structured
    # by the IETF
    # ip_schema = m.get_schema('ietf-ip')
    # ip_schema = m.get_schema('ietf-interfaces')
    # ip_schema = m.get_schema('ietf-inet-types')
    ip_schema = m.get_schema('ietf-yang-types')
    root = ET.fromstring(ip_schema.xml)
    # converting a root object into a list
    yang_tree = list(root)[0].text
    # writing into a file ietf-ip.yang
    # the file will contain a yang data model
    # leaf, container, modiles, enums, types, and others are explained in the Cisco definite course on CBT Nuggets
    '''
    ...
    list address {
      key "ip";
      description
        "The list of configured IPv4 addresses on the interface.";
      leaf ip {
        type inet:ipv4-address-no-zone;
        description
          "The IPv4 address on the interface.";
      }
    ...
    '''
    # f = open('ietf-ip.yang', 'w')
    # f = open('ietf-interfaces.yang', 'w')
    # f = open('ietf-inet-types.yang', 'w')
    f = open('ietf-yang-types.yang', 'w')
    f.write(yang_tree)
    f.close()