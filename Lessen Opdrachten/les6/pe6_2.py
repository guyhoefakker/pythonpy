#['croissant', 'koffie', 'chocolade', 'chips', 'frisdrank', 'soep', 'aardappel', 'friet', 'vlees', 'pindakaas']
lst = eval(input("10 strings: "))
lst2 =[]
for item in lst:
    if len(item) == 4:
        lst2.append(item)

print(lst2)

