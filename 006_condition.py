x = 1
y = 2

# chain condition
if not(x == y or x + y == 3):
    print('x = y or x + y = 3')

# nest
if x == y:
    if x + y == 3:
        print('x + y = 3')
    else:
        print('x = y')
else:
    print('x != y')