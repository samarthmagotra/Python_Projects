
with open('devices 2.txt', 'r') as f:
    content = f.read().splitlines()
    print(content)

    device_list = []
    for elem in content:
        device_list.append(elem.split(':'))

    print(device_list)

print('##########'*10)
for device in device_list:
    print(f'Device name is {device[0]} with Ip address {device[1]}')