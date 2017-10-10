def gemiddelde():
    zin = input('zin: ')
    words = zin.split()
    result = 0
    for x in words:
        result += len(x)
    print(result/len(words))


print(gemiddelde())
