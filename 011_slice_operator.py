# slice operater

fruits = ['apple', 'pear', 'strawberrys']
text = 'Hello I like python'

print(fruits[1])
print(text[1])

# slice operater
# print(text[start])
# print(text[start:stop])
# print(text[start:stop:step])
# just like: for x in range(0, 10, 1)

print(text[0:5])
print(text[:5])
print(text[3:])
print(text[0:len(text)])
print(text[::])
print(text[::3])
print(text[3:3])

print(fruits[::])

# use slice operater to insert

fruits.append('bluberrys')
print(fruits)

fruits[0:0] = 'a'
print(fruits)
fruits[2:2] = 'b'
print(fruits)