# Let's use ElementTree to parse an XML file in Django
# No need to install any additional package

import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse('file.xml')
root = tree.getroot()

# Access elements in the XML file
for child in root:
    print(child.tag, child.attrib)

# Output
# >> element1 {'attribute': 'value'}
# >> element2 {'attribute': 'value'}
# Please Like and Subscribe