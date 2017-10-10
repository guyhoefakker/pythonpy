def kwadraten_som():
    grondgetallen = [2,4,-1,8,7,6]
    result = []
    for x in grondgetallen:
        if x >= 0:
            x = x**2
            result.append(x)
    return sum(result)

print(kwadraten_som())



