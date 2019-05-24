#ejemplo de switch
import os
import math

def circulo (r):
	print ("area circulo: ", math.pi*r*r)
def triangulo (base,altura):
	print ("area triangulo ", (base*altura)/2)
def cuadrado (base):
	print ("area cuadrado ", base*base)
def rectangulo (base,altura):
	print("area rectangulo", base*altura)
def menu (nom, edd, r, base, altura):
	if nom == 'Alumno':
		print("eres aplicado")
	else:
		print("estudia")
	if edd >=18:
		print("Eres mayor de edad")
	elif edd >=12:
		print("Eres adolescente")
	elif edd >=3:
		print ("Eres un nino")							
	else : 
		print("No te entiendo")
	os.system("Pause")
	os.system('cls')
	while True:
		
		print ("Menu")
		print("Selecciona una opcion")
		print ("a) circulo")
		print ("b) triangulo")
		print("c) cuadrado")
		print ("d) rectangulo")
		print ("e) salir")
		op=input()
		if op=='a':
			circulo(r)
		elif op == 'b':
			triangulo (base, altura)
		elif op == 'c':
			cuadrado(base)
		elif op == 'd':
			rectangulo(base, altura)
		elif op == 'e':
			break
		else:
			print("Opcion no valida")
		os.system("Pause")
		os.system('cls')
def mi_inicio ():
	base=int(input("base: "))
	altura =int(input("altura: "))
	radio = int(input("radio: "))
	nombre = input("nombre:")
	edad = int(input("edad: "))	
	menu (nombre, edad, radio, base, altura)
if __name__=='__main__':
	mi_inicio()	