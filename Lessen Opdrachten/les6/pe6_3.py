invoer = "6-8-3-3-5-7-3-1-9-6-4-8"
lst = invoer.split('-')
print('gesorteerde list van ints: ' + str(lst)+'\ngrootste getal: ' + str(max(lst)) + ' kleinste getal: '+ str(min(lst)))
print('aantal getallen: ' + str(len(lst)))
lst2 =[]
for x in lst:
    lst2.append(int(x))
print('gemiddelde: ' + str(sum(lst2)/(len(lst2))))