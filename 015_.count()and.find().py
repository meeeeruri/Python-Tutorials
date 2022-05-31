# .find(), .count()

string = 'hello'
print(string.find('o'))
print(string.find('7'))

string = 'aswefasfjiavnjfawvfbdasfvasdfjnvjanjijn'
print(string.count('a'))
print(string.count('as'))
print(string.count('sa'))


if string.count('_') > 0:
    print('Not good!')
else:
    print('Good')


string = 'asdf_dafes'
if string.count('_') > 0:
    print('Not good!')
else:
    print('Good')