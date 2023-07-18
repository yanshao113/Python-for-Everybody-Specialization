
import ssl
import urllib.request

from bs4 import BeautifulSoup

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL: ")
count = input("Enter count: ")
position = input("Enter position: ")
count_int = int(count)
position_int = int(position)
for i in range(count_int):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    target = tags[position_int-1].contents[0]
    url = 'http://py4e-data.dr-chuck.net/known_by_{}.html'.format(target)
print(target)

