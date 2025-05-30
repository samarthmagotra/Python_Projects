with open('macs.txt', 'r') as f:
    content = f.read().split()
    print(content)

    content = list(set(content))
    print(content)

with open('mac_unique.txt', 'w', newline='') as f:
    for mac in content:
        f.write(f'{mac}\n')



