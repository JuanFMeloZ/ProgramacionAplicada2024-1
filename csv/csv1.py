### Este codigo genera varios numeros aleatorios, los guarda en archivo y los gráfica
import csv
import random
from datetime import datetime
import matplotlib.pyplot as plt

with open('numero_tiempo.csv', mode = 'w') as csv_file:
	fieldname = ['Numero_Aleatorio', 'Tiempo']
	writer = csv.DictWriter(csv_file, fieldnames=fieldname)
	writer.writeheader()

	for _ in range(10):
		x = random.random()
		tiempo_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		writer.writerow({'Numero_Aleatorio': x, 'Tiempo':tiempo_actual})

with open('numero_tiempo.csv', mode='r') as csv_file:
	reader = csv.reader(csv_file)
	next(reader)

	lista_numeros = []
	lista_tiempos = []
	for row in reader:
		numero = float(row[0])
		tiempo = row[1]
		lista_numeros.append(numero)
		lista_tiempos.append(tiempo)

plt.scatter(lista_numeros, range(len(lista_numeros)))

plt.xlabel("Número aleatorio")
plt.ylaber("Índice")

plt.show()

print("Número:", lista_numeros)
print("Tiempos:", lista_tiempos)
