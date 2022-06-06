text = input('username: ')
try:
    number = int(text)
    print(number)
except:
    print('Error: Invalid Username.')