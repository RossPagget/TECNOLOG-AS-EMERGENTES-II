#Ejercicio 9
#Nombre: Rosmery Aruni Paye
#CI: 9244293        RU:200075568       
#Materia: Tecnologias Emergentes II

#metodos de listas
numeros=[1, 2, 3, 4, 5]
#adiccionar elementos a la lista
numeros.append(6)
print(numeros)
#insertar elementos a una posicion determinada de la lista
numeros.insert(0, -1)
print(numeros)

numeros.insert(1, 0)
print(numeros)

#eliminar elementos de la lista
numeros.remove(0)
print(numeros)  

#elimina un elementoi en su primera aparicion
numeros.remove(1)
print(numeros)  

#verificar si un elemento esta en la lista
print(3 in numeros)

#tamaño de la lista
print(len(numeros))

#eliminar el contenido de la lista
numeros.clear()
print(numeros)