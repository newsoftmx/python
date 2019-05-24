import random#permite trabajar numeros aleatorios
import time#permite trabajar las propiedades de tiempo
mi_lista=list()#crea mi lista, la lista no esta limita, es dinámica

#con el siguiente ciclo, determino que mi lista tendra 10 valores
for posicionLista in range(0,5,1):
	numero=int(input("escribe el valor del arreglo: "))
	mi_lista.append(numero)
	#La siguiente linea hace lo mismo pero en una sola instrucción
	#mi_lista.append(int(input("escribe el valor del arreglo de la posición: ")))

time.sleep(2)#esta linea hace que el programa espere dos segundos

#ahora imprimo mi lista(arreglo)
for posicionLista in range(0,5,1):
	print ("El valor de lista  en la posicion: ", posicionLista, " es: ", mi_lista[posicionLista])

#ahora ordeno la lista(arreglo)
mi_lista.sort()
print("En 2 segundos aparecerá la lista ordenada")
time.sleep(2)#esta linea hace que el programa espere dos segundos

#ahora vuelvo a mostrar la lista(arreglo)
for posicionLista in range(0,5,1):
	print ("El valor de lista  en la posicion: ", posicionLista, " es: ", mi_lista[posicionLista])

#imprimo mi lista sin ciclo
print(mi_lista)

#ahora eliminare valores de la lista
#elimino el primer valor de la lista y la muestro
mi_lista.pop(0)
print(mi_lista)

#elimino el ultimo valor de la lista
mi_lista.pop()
print(mi_lista)

#ordena de forma inversa la lista
mi_lista.reverse()
print(mi_lista)

#cuenta el numero de veces que aparece un número y la muestra
print(mi_lista.count(3))
print(mi_lista)

#limpia la lista y la muestra
mi_lista.clear()
print(mi_lista)