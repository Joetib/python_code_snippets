# To check if a string is a valid XML document, we can use the `xml.etree.ElementTree` module in Python's standard library.

# Here's a code snippet that demonstrates how to check if a string is a valid XML document:

import xml.etree.ElementTree as ET

def is_valid_xml(xml_string):
    try:
        ET.fromstring(xml_string)
        return True
    except ET.ParseError:
        return False

# Example usage:
xml_string = "<root><element>Value</element></root>"
print(is_valid_xml(xml_string))
# Output: True

xml_string = "<root><element>Value</element>"
print(is_valid_xml(xml_string))
# Output: False

xml_string = "This is not a valid XML document"
print(is_valid_xml(xml_string))
# Output: False


# Please Like and Subscribe