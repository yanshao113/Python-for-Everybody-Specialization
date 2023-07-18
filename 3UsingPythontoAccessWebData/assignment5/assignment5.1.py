import json
import urllib.request, urllib.parse, urllib.error

url = "http://py4e-data.dr-chuck.net/comments_1718585.json"
uh = urllib.request.urlopen(url)
data = uh.read()
js = json.loads(data)
results = js["comments"]
Sum = 0
for item in results:
    Sum += item["count"]
print(Sum)