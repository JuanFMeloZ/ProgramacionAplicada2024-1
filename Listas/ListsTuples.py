#################LISTAS####################
###########################################
my_lista = ['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde']
#input()
print(my_lista) #muestra los elementos dentro de la lista
print(type(my_lista)) #muestra el tipo de variable que es my_lista
print(my_lista[2]) #muestra el elemento en la posicion 2, o sea, el tercero

print("my_lista size: ", len(my_lista)) #muestra el tamaño de la lista, o sea el numero de elementos dentro de ella
print(my_lista[0:2]) #imprime desde la posicion 0 hasta la 2 sin imprimir la posicion 2
print(my_lista[:2]) #imprime hasta la posicion 2 sin imprimir la posicion 2

my_lista.append('Blanco')      #Agrega elemento al final de la lista
print(my_lista) #imprime la nueva lista

my_lista.insert(3, 'Negro')  #Agrega elemento en la posicion 3 de la lista
print(my_lista) #imprime la nueva lista


my_lista.extend(['Marron', 'Gris'])   #Concatena a otra lista
print(my_lista) #imprime la nueva lista

print(my_lista.index('Azul')) #imprime el número de la posicion del objeto 'azul'

#my_lista.remove('Magenta')
my_lista.remove('Marron') #Remueve el elemento entre parentesis
print(my_lista) #imprime la nueva lista

my_lista.insert(8, 'Marron')  #Agrega elemento en la posicion 8 de la lista
print(my_lista) #imprime la nueva lista

print(my_lista.pop()) #imprime el último elemento, y lo saca de la cadena
size = len(my_lista) #almacena el tamaño de la lista en una variable
print("size = ", size) #imprime la variable con el tamaño, o sea el número de elementos
#print(my_lista.pop(size))

my_lista_3 = my_lista*3 #almacena 3 veces la cadena my_lista en my_lista_3
print("my_lista_3: ", my_lista_3) #imprime la nueva lista

print("Sort:") #imprime el mensaje
print() #imprime una linea vacia 
my_listaSort = my_lista.sort() #Organiza la cadena y no devuelve ningún resultado
print(my_listaSort) #impreme la variable que no tiene asignado ningún resultado

my_NumList = [10, 9, 8, 7, 6 , 5 , 4, 3, 2, 1] #Crea una nueva lista
print("Ordering my_NumList: ") #imprime el mensaje
my_NumList.sort() #ordena la lista
print(my_NumList) #impreme la lista ordenada
#OrderedLList = my_NumList.sort() 
#print(my_listaSort)

#Ordenando lista de mayor a menor
my_NumList.sort(reverse = True) #organiza la lita de forma descendente
print("De menor a mayor: ", my_NumList) #imprime el mensaje y la lista organizada



#################TUPLAS####################
###########################################
# Corresponde a una estructura similar a las listas, la diferencia está
# en que no se pueden modificar una vez creadas, es decir que son inmutables:

#Convertir una lista a tupla:prin
print("###########################")
print("###########################")
print("###########################")
print("############TUPLAS#########")
my_tupla = tuple(my_lista) #convierte la lista en una tupla y la guarda en una variable
print()
print()
print("my_tuple: ", my_tupla) #imprime la tupla

print(my_tupla[0]) #imprime el elemento de la tupla en la posición 0
print(my_tupla[2]) #imprime el elemento de la tupla en la posición 2


#Evaluar si un elemento está contenido en la tupla (Devuelve un valor booleano)
print('Rojo' in my_tupla) #devuelve true en caso de que si exista el elemento 'Rojo' en la tupla
print(my_tupla.count('Rojo')) #devuelve el número de elementos 'Rojo'

#Tupla con un solo elemento
my_tupla_unitaria = ('Blanco') #Crea una tupla de un solo elemento
print(my_tupla_unitaria) #imprime la tupla

#Empaquetado de tupla, tupla sin paréntesis
my_tupla = 'Gaspar', 5, 8, 1999 #crea una tupla sin parentesis
print(my_tupla) #imprime la tupla

#Desempaquetado de tupla, se guardan los valores en orden de las variables
nombre, dia, mes, año = my_tupla #asignando variables a los valores ya establecidos
print(nombre) #imprime la variable nombre de la tupla
print(dia) #imprime la variable dia de la tupla
print(mes) #imprime la variable mes de la tupla
print(año) #imprime la variable año de la tupla

print("Nombre: ", nombre, " - Dia:", dia, " - Mes: ", mes, "- Año: ", año) #imprime las variables de la tupla

#Convertir una tupla en una lista
my_lista2=list(my_tupla)
print(my_lista2)
