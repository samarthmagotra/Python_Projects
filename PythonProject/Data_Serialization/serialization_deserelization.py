import csv
import json
import pickle
import requests

#Data -- dict and tuple
friends = {"Dan":[20, 'London', 32323232], "Maria":[25,'Paris',424242444], "Boo":[40,'India',0]}
friends2 = {"Sam":[20, 'London', 32323232], "Boo":[25,'India',424242444]}
friend = (friends2, friends) #tuple of dict

# serialization function
def serialize(python_object, file: str, serial_protocol:str = 'json'):
    if serial_protocol == 'pickle':
        with open(file,'wb') as f:
            pickle.dump(python_object,f)
    elif serial_protocol == 'json':
        with open(file, 'w') as f:
            json.dump(python_object,f)
    else:
        print(f"Incorrect serial protocol: {serial_protocol}, should be either json or pickle")

# deserialization function
def deserialize(serial_file:str, deserial_protocol:str):
    if deserial_protocol == 'pickle':
        with open(serial_file, 'rb') as f:
            obj = pickle.load(f)
            print(type(obj))
            return obj
    elif deserial_protocol == 'json':
        with open(serial_file, 'rt') as f:
            obj = json.load(f)
            print(type(obj))
            return obj

# calling functions
serialize(friends, 'serial.txt', 'json')
serialize(friend,'serial.dat', 'pickle')
mydict = deserialize('serial.txt','json')
print(f'json: {mydict}')
mytuple = deserialize('serial.dat', 'pickle')
print(f'pickle: {mytuple}')

#error case
serialize(friends, 'a.txt', 'python')

