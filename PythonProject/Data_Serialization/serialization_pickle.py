import pickle
friends = {"Dan":[20, 'London', 32323232], "Maria":[25,'Paris',424242444]}
friends2 = {"Sam":[20, 'London', 32323232], "Boo":[25,'India',424242444]}
friend = (friends2, friends) #tuple of dict

#with open('friends.txt', 'w') as f:
#    f.write(str(friends))

with open('friends.dat', 'wb') as f:
    pickle.dump(friend, f)

with open('friends.dat','rb') as f:
    obj = pickle.load(f)
    print(type(obj))
    print(obj)