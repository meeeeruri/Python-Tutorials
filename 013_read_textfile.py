
file = open('013text.txt', 'r')
file.close

f = file.readlines()
print(f)

print('=======')

newList = []
for line in f:
    newList.append(line[:-1])

print(newList)

print('=======')

newList = []
for line in f:
    if line [-1] == '\n':
        newList.append(line[:-1])
    else:
        newList.append(line)

print(newList)

print('=======')

newList = []
for line in f:
    newList.append(line.strip())

print(newList)

