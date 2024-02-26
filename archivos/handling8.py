f = open("Archivo.txt", "a")
f.write("Now the file has more content!")
f.close()
#Agregar al final del archivo

f = open("Archivo.txt", "r")
print(f.read())
