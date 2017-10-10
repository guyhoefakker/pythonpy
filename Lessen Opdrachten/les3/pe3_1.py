score = int(input('geef je score:'))
lne1 = ('met een score van  ' + str(score) + '  ben je geslaagd')
lne2 = ('met een score van  ' + str(score) + '  ben je niet geslaagd')
if score >= 15:
    print(lne1)
else:
    print(lne2)