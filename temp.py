inp = eval(input('ENTER: '))
print(type(inp))
if isinstance(inp, tuple):
    print('Yess it is tuple')
else:
    print('No its not a tuple')