
with open('devices.txt', 'r+') as f:
    content = f.read().splitlines()
    print(content)
    print(content[1])
    devices = list()
    for line in content[1:]:
        print(line.split(':'))
        devices.append(line.split(':'))
    print(devices)

for device in devices:
    print(f'pinging: ',device[1])