from random import *
r=0
while r<=10:
    r+=1
    f = open("numeros.txt", "a")
    f.write(str(random()))
    f.close()
