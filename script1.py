def start(style='-'):
    print(style * 76)
    word=' python_assignment '
    print(word * 4)
    print(style * 76)
start()

x = float(input('enter a number'))

def f(x):
    function = 2 * x + 3
    return(' 2 * {} + 3 = {}'.format(x,function))

fun= f(x)
print('Result : {}'.format(fun))