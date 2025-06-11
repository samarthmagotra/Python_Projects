import sys

a = [1,2,3,4,55,55,33,2,1]
print(f'System Version: {sys.version}\nSystem Env: {sys.implementation}\nSystem Platform: {sys.platform}\nPath: {sys.path}' )
print(f'size: {sys.getsizeof(set(a)), sys.getsizeof(a), sys.getsizeof(tuple(a))}')

#sys.stdout --> to redirect output to a file
stdout = sys.stdout
with open('/Users/samarthmagotra/Upskill/Python/PythonProject/sys_shutil_OS_subprocess/a.txt', 'a') as sys.stdout:
    print('Output')
    help('sys')

sys.stdout = stdout
with open('/Users/samarthmagotra/Upskill/Python/PythonProject/sys_shutil_OS_subprocess/a.txt', 'r') as f:
    print(f.read())

# sys.argv -- command line argument
#e.g for 'pip install ansible', sys.argv[0],sys.argv[1],sys.argv[2] are pip, install and ansible

print(len(sys.argv))
print(sys.argv[0])
print(sys.argv)