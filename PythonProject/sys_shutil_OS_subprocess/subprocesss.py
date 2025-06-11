import subprocess

from OS import output

#better error handling than OS module

cmd = ['ifconfig', '-a']
print(subprocess.check_output(cmd))

cmd = ['ping', '-c', '2', '8.8.8.8']
out = subprocess.check_output(cmd)
print(type(out))
str_output = out.decode()
print(str_output)