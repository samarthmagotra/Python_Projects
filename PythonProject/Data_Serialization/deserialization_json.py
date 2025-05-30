import json

with open('friends.json', 'rt') as f:
    obj = json.load(f)
    print(type(obj))
    print(obj)

json_string = """{
    "Dan": [
        20,
        "London",
        32323232
    ],
    "Maria": [
        25,
        "Paris",
        424242444
    ],
    "Boo": [
        40,
        "India",
        0
    ]
}"""

obj = json.loads(json_string)
print(type(obj))
print(obj)