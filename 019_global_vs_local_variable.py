var = 9 # global variable
loop = True # global variable

def func(x):
    newVar = 7 # local variable

    if newVar == 5:
        return newVar

try:
    print(newVar) # return error since newVar is only reacheable locally in func
except:
    print('newVar is not available')

def func_print(x):
    print(var)

def func_modify():
    global loop 
    loop = 1 # will modify the global variable loop

def func_modify2():

    loop = 1 # create a local variable loop instead of the global variable loop

func_print(1) # func_print can reach globle variable var

func_modify2()
print(loop)

func_modify()
print(loop)