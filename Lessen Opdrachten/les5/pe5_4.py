import time
with open('hardlopers.txt', 'a') as myfile:
    myfile.write('\n' + str(time.strftime('%a %d %b %Y, %H:%M:%S;', time.gmtime()) + ' Kemal'))

myfile.close()