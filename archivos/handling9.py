f = open("Archivo.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()
#sobre escribir en el archivo

f = open("Archivo.txt", "r")
print(f.read())
