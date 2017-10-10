lst = ['a', 'b', 'c']


def wijzig(x):
    x.clear()
    x.append('d')
    x.append('e')
    x.append('f')

print(lst)
print(wijzig(lst))
print(lst)