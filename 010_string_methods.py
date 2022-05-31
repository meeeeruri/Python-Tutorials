# .strp(), len(), .lower(), .upper(), .split()

text = '    HELLO    world    '
print(text)
print(text.strip())
print(len(text))
print(len(text.strip()))
print(text.upper())
print(text.lower())

text2 = 'hello.tim.bye.hi'
print(text2)
print(text2.split('.')) # split(delimiter)