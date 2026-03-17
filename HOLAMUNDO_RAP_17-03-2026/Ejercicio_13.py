#Ejercicio 13
#Nombre: Rosmery Aruni Paye
#CI: 9244293        RU:200075568       
#Materia: Tecnologias Emergentes II

#funciones - son bloques de codigo reutilizables
#funcion sin parametros- ni devolucion de valor
def saludar():
    print("Hola, bienvenidos al curso de python")
#Funcion con parametros
def saludo(nombre):
    print("Hola,", nombre, "bienvenido a clases")
#funcion con devolucion de valores
def sumar(a,b):
    return a+b  
#establecer valores por defecto
def bienvenida(nombre="estudiante"):
    print("Bienvenido,", nombre)
#funcion copn argumento variables
def sumador(*args):
    return sum(args)

#llamar a la funcion
saludar() 
#llamar a la funcion
saludo("Rosmery")
#llamar a la funcion
resultado=sumar(10,4) 
print("la suma es: ", resultado)
#llamar a la funcion con valor por defecto
bienvenida()
("Rosmery")
#llamar a la funcion
print(sumador(1,2,3,4,5))
print(sumador(4,5,6))