import os

print(os.popen('arp -a'))
output = os.popen('arp -a').read()
print(output)
output = os.popen('ls -l /etc').read()
print(output)
os.system('type > abc.txt') #-- create a file