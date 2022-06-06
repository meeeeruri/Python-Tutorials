x = 'string'
y =23
boo = True
print(type(x))
print(x.count('1')) # method .count is not available for class int or bool

# example of a class

class number():
    def __init__(self):
        self.var = 0
    def __init__(self, x):
        self.var = x
        
#    def display(self):
#        print(self.var)
    def display(self, x):
        print(x)

num = number(22)
num2 = number(23)
num.display(num.var)
num2.display(num2.var)