import ssl
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = "http://py4e-data.dr-chuck.net/comments_1718584.xml"

uh = urllib.request.urlopen(address, context=ctx)

data = uh.read()

tree = ET.fromstring(data)
counts = tree.findall(".//count")
Sum = 0
for i in counts:
    Sum += int(i.text)
print(Sum)
