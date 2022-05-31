fruits = ['apple', 'pears', 'strawberrys', 3, 8, 90]

# iteration by item
for fruit in fruits:
    print(fruit)
    
    if fruit == 'pears':
        print('==fruit==')
    else:
        print('==not pears==')
print('=========')

# iteration by position
for x in range(0, 6):
    if fruits[x] == 'pears':
        print(fruits[x]) 
    else:
        print('not a pear')
print('=========')

# iteration by position with len()
for x in range(len(fruits)):
    if fruits[x] == 'pears':
        print(fruits[x])
    else:
        print('not a pear')
print('=========')