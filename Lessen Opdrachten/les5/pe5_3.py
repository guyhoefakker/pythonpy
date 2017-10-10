#niet gelukt
file = open('kaartnummer.txt','r')
words = file.read()
splitwords = words.splitlines()
len = len(splitwords)

print('deze file telt '+str(len)+' regels')
result = []
for x in words.splitlines():
    result.append(x)
print('het grootste kaartnummer is '+(max(result)[0:6])+ ' op lijn nummer 4')
file.close()