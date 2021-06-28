from jnpr.junos import Device
from lxml import etree
import xml.dom.minidom


xpath_physical_interface_names = '//physical-interface/name/text()'
xpath_logical_interface_names = '//physical-interface/logical-interface/name/text()'
xpath_physical_and_logical_interface_names = '//physical-interface/name/text()|//physical-interface/logical-interface/name/text()'
xpath_physical_and_logical_interface_xml = '//physical-interface|//physical-interface/logical-interface'
xpath_physical_logical_interface_names_irb = 'physical-interface/logical-interface[contains(name, "irb")]/name/text()'
xpath_physical_logical_interface_names_ge = 'physical-interface/logical-interface[contains(name, "ge")]/name/text()'

with Device(host='ce1', user='automation', password='juniper123') as network_device:
    rpc = network_device.rpc.get_interface_information(extensive=True)
    physical_logical_interface_names_ge = rpc.xpath(xpath_physical_logical_interface_names_ge)

    for each in physical_logical_interface_names_ge:
        each = each.rstrip('\n')
        print(each)

    # physical_interface_names = rpc.xpath(xpath_physical_interface_names)
    # logical_interface_names = rpc.xpath(xpath_logical_interface_names)
    # physical_and_logical_interface_names = rpc.xpath(xpath_physical_and_logical_interface_names)
    # physical_and_logical_interface_xml = rpc.xpath(xpath_physical_and_logical_interface_xml)
    # physical_logical_interface_names_irb = rpc.xpath(xpath_physical_logical_interface_names_irb)
    # for each in rpc.xpath(xpath_physical_and_logical_interface_xml):
    #     xml_minidom = xml.dom.minidom.parseString(etree.tostring(each))
    #     interface_xml_pretty = xml_minidom.toprettyxml()
    #     print(interface_xml_pretty)
