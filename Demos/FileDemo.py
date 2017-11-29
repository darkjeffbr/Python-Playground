import os

try:
    fob = open('next_topic.txt')
    print('File name : ', fob.name)
    print('File state closed : ', fob.closed)
    print('Opening mode : ', fob.mode)
finally:
    fob.close()
print('File state closed : ', fob.closed)

print("Using with clause in Python")
with open('next_topic.txt', encoding='utf-8') as f:
    print('File name : ', f.name)
    print('File state closed : ', f.closed)
    print('Opening mode : ', f.mode)
print('File state closed : ', f.closed)

print(' Read/Write to a file in python '.title().center(40,'#'))
with open('logfile.txt','w',encoding='utf-8') as f:
    f.write('my first line\n')
    f.write('a second line\n')
    f.write('the last line')

with open('logfile.txt') as f:
    content = f.readlines()

for line in content:
    print(line)

f = open('logfile.txt', 'r+')
data = f.read(19)
print('Read String is : ',data)

position = f.tell()
print('Current file position : ',position)

position = f.seek(0, 0)
data = f.read(19)
print('Again read String is : ',data)


f.close()

print('Renaming and deleting file')
f = open('new.txt', 'w')
f.close()
print(os.listdir())

os.rename('new.txt', 'newChanged.txt')
print(os.listdir())

os.remove('newChanged.txt')
print(os.listdir())