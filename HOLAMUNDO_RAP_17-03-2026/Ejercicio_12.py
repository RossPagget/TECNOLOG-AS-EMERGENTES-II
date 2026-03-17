#Ejercicio 12
#Nombre: Rosmery Aruni Paye    RU:200075568       
#Materia: Tecnologias Emergentes II

#diccionarios -> almacenan datos en pares clave-valor
mi_diccionario={'nombre':'Rosmery Aruni Paye', 'edad':70, 'ciudad':'La Paz'}
print(mi_diccionario)

#acceder a un valor
print(mi_diccionario['nombre'])
print(mi_diccionario['ciudad'])

#agregar elementos
mi_diccionario['profesion']='Ingeniera'
print(mi_diccionario)   

#eliminar un elemento
del mi_diccionario['ciudad']
print(mi_diccionario)

#obtener claves de diccionario  
print(mi_diccionario.keys())

#obtener valores de diccionario
print(mi_diccionario.values())

#verificar si una clave existe en el diccionario
if 'ciudad' in mi_diccionario:
    print("clave encontrada")

#recorrido de un diccionario
for clave, valor in mi_diccionario.items():
    print("[Clave: ]", clave, "[Valor: ]", valor)
