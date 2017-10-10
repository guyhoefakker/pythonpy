file2 = open('kaartnummer.txt','r')
words = file2.read()
splitwords = words.splitlines()
for x in splitwords:
    parts = x.split(',')
    print(str(parts[1]) + ' heeft kaartnummer: ' + str(parts[0]))
file2.close()


