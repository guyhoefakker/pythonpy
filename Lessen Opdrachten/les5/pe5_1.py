def convert(x):
    return x*1.8+32

def table():
    for z in range(-30,41,10):
        print('{:5}    {:5}'.format(convert(float(z)),float(z)))
print('  F         C')
print(table())