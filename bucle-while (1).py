cantidad=int(input("Escribe el numero de repeticiones: "))
#esta variable solo va contando las repeticiones que se hacen
contador=1;
while contador<=cantidad:
	print(contador)
	contador+=1
	terminar=str(input("Desea terminar: s= si n =no"))
	if terminar=="s":
		contador=cantidad+1