#Si deseo importar solo la propiedad array de NumPy 
#cuando se utilizan vectores o matrices utilizare Numpy
import numpy as np
import random
import time

#defino el tamaño del arreglo de forma directa
#a=np.array([0,0,0])

#defino el tamaño del arreglo de forma automática
a=np.arange(3)

#defino el tamaño del arreglo desde un rango con incrementable
arreglo_rango=np.arange(1,1000,1)

#Solicito la captura de los valores del rango
for posicion in range(0,3,1):
	numero=int(input("escribe el valor del arreglo de la posición: " ))
	a[posicion]=numero

for posicion in range(0,3,1):
	print("El valor del arreglo en la posición: ", posicion ," es: ", a[posicion])

#for posicion in range(0,a.size):
#	numero=int(input("escribe el valor del arreglo de la posición: "))
#	a[posicion]=numero

print("En 1 segundos se mostrará el tamaño del arreglo")
time.sleep(1)
print(a.size)

print("En 1 segundos se mostrará el arreglo")
time.sleep(1)
print(a)

print("En 1 segundos se ordenará el arreglo")
time.sleep(1)
a.sort()
print(a)

print("En 1 segundos se mostrará el arreglo de 1000 valores")
time.sleep(1)
print(arreglo_rango)

print("En 1 segundos se mostrará el arreglo de 1000 valores pero ordenado")
time.sleep(1)
arreglo_rango.sort()
print(arreglo_rango)

arreglo_aleatorio=np.arange(1000)
for x in range(1,1000,1):
	numeroAleatorio=random.uniform(1,10000)
	arreglo_aleatorio[x]=numeroAleatorio
print(arreglo_aleatorio)

#genere una pausa y ordene el arreglo e imprima el arreglo