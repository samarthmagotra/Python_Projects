import json
import pprint
import requests

r = requests.get('https://jsonplaceholder.typicode.com/todos')
print(type(r))
print(r)
pprint.pprint(r.json())

pythion_obj = json.loads(r.text)
print(type(pythion_obj))
#print(obj)

for item in pythion_obj:
    if item['completed'] == True:
        print(item)