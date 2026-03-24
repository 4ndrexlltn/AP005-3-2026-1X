#################LISTAS####################
'''
Las listas en Python son estructuras de datos ordenadas, mutables y
versátiles, definidas mediante corchetes [] para almacenar conjuntos 
arbitrarios de elementos (números, textos, o mezcla de tipos). Son fundamentales
por su dinamismo, permitiendo añadir (append), eliminar (pop, remove) y modificar
elementos, usando índices que comienzan en 0.
Características Principales:
-Ordenadas: Mantienen el orden de inserción.
-Mutables: Se pueden cambiar, añadir o eliminar elementos.
-Indexables: Acceso por índice, ej. lista[0] es el primer elemento.
-Heterogéneas: Pueden contener distintos tipos de datos simultáneamente.
'''

miLista = ['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde'] #Creación de una lista
print(miLista) #Impresión de todos los datos de la lista creada anteriormente
print(type(miLista)) #Imprime que tipo de dato es la lista ==> class list

print(miLista[2]) #El [2] indica que se esta seleccionando el tercer elemento de la lista 'Amarillo' (Indice)
print("Longitud de miLista: ", len(miLista)) #Imprime la cantidad de elementos que estan guardados en la lista
print(miLista[0:2]) #Imprime desde el indice 0 (primer elemento) hasta el indice 1 (Segundo elemento)
print(miLista[:2]) #Variación de la anterior instrucción pero realiza la misma acción

miLista.append('Blanco') #Agrega un nuevo elemento que se ubica en la ultima posición de la lista
print(miLista)
miLista.insert(3, 'Negro') #Agrega en el indice 3 (Posición 4) el string 'Negro'
print(miLista)
miLista.extend(['Marron', 'Gris']) #Concatena, combina, une dos listas, los elementos de la lista que se quiere agregar van a las ultimas posiciones
print(miLista)
print(miLista.index('Azul')) #Imprime el indice (Entero) asociado al elemento
miLista.remove('Marron') #Busca y elimina el elemento, si no existe genera error
print(miLista)
miLista.insert(8, 'Marron')
print(miLista)
print("Instruccion .pop")
print(miLista.pop()) #Elimina y retorna el ultimo elemento. Se puede indicar un elemento específico agregando el indice entre los paréntesis
print("Longitud miLista: ", len(miLista))
miLista3 = miLista*3 #Incrementa 3 veces los elementos de la lista concatenando la misma lista tres veces
print("miLista3: ", miLista3)
print("Instruccion .sort")
miListaOrdenada = miLista.sort() #Ordena de forma ascendente la lista original, sin la necesidad de crear una nueva. Para los strings ordena segun la primera letra del elemento
print(miListaOrdenada)
print(miLista)

miListaNum = [10, 9, 8, 7, 6 , 5 , 4, 3, 2, 1]
print("Ordenando lista numeros.")
miListaNum.sort()
print(miListaNum)

miListaNum.sort(reverse=True) #Altera la forma en que se ordena la lista, ahora de mayor a menor
print("De mayor a menor: ", miListaNum)



#################TUPLAS####################
'''
Las tuplas son  estructuras de datos ordenadas e inmutables (no se 
pueden modificar, añadir o eliminar elementos tras su creación). Se 
definen mediante paréntesis () y comas, siendo ideales para agrupar 
datos relacionados que no deben cambiar, como coordenadas o registros, 
ofreciendo mayor seguridad y rendimiento.
'''
miTupla = tuple(miLista) #Convierte una lista a una tupla
print("miTupla: ", miTupla)
print(miTupla[0]) #Manejo de indices para acceder a los elementos de la tupla
print(miTupla[2])


print('Rojo' in miTupla) #Evaluar si un elemento está contenido en la tupla (Devuelve un valor booleano)
print(miTupla.count('Rojo')) #Retorna el numero  de elementos 'Rojo' almacenados en la tupla


miTuplaUnitaria = ('Blanco') #Tupla con un solo elemento
print(miTuplaUnitaria)


miTuplaDos = 'Gaspar', 4, 5, 1999 #Empaquetado de tupla, tupla sin paréntesis
print(miTuplaDos)

nombre, dia, mes, año = miTuplaDos #Desempaquetado de tupla, se guardan los valores en orden de las variables
print(nombre)
print(dia)
print(mes)
print(año)

print("Nombre: ", nombre, " - Dia:", dia, " - Mes: ", mes, "- Año: ", año)

miLista2 = list(miTupla) #Convertir una tupla en una lista
print(miLista2)
