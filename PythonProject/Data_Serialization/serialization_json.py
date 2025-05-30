import json
friends = {"Dan":[20, 'London', 32323232], "Maria":[25,'Paris',424242444], "Boo":[40,'India',0]}
friends2 = {"Sam":[20, 'London', 32323232], "Boo":[25,'India',424242444]}
friend = (friends2, friends) #tuple of dict

#dumps - python object to json encoded string
with open('friends.json','w') as f:
    json.dump(friends, f, indent=4)

json_string = json.dumps(friends, indent=4)
print(json_string)