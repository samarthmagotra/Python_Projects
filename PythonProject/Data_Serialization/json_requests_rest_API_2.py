import pprint
import csv
import requests
import json

response = requests.get('https://jsonplaceholder.typicode.com/users')
print(response.text)

python_object = json.loads(response.text)
#pprint.pprint(python_object)

print(f'total number of users: {len(python_object)}')
for user in python_object:
    print(f'Name: {user["name"]}, City: {user["address"]["city"]}, '
          f'GPS coordinates: LAT:{user["address"]["geo"]["lat"]}, '
          f'LNG:{user["address"]["geo"]["lng"]}, '
          f'Company Name: {user["company"]["name"]}')

    csv_data = f'{user["name"]},{user["address"]["city"]},({user["address"]["geo"]["lat"]},{user["address"]["geo"]["lng"]}),{user["company"]["name"]}'


with open('user.csv','w') as f:
    writer=csv.writer(f)
    writer.writerow(("Name","City","GPS","Company"))
    for user in python_object:
        csv_data = (user["name"],user["address"]["city"],(user["address"]["geo"]["lat"],user["address"]["geo"]["lng"]),user["company"]["name"])
        writer.writerow(csv_data)

