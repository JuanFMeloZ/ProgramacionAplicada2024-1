import os
if os.path.exists("Archivo2.txt"):
  os.remove("Archivo2.txt")
else:
  print("The file does not exist")

#si existe el archivo eliminalo
