################# Diccionarios - Ejemplo Videojuegos ####################

# Definición de diccionarios
jugadores = {"Andres": 1500, "Laura": 2300, "Carlos": 1800, "Sofia": 2000}
niveles = {"Bosque": 5, "Desierto": 8, "Ciudad": 10}

print(jugadores)
print(niveles)
print(type(jugadores))

# Diccionario tipo traducción
items = {"sword": "espada", "shield": "escudo", "potion": "poción", "bow": "arco"}
print(items)

# Claves no pueden ser listas
# error_dic = {[1,2,3]: "nivel"}  # ERROR

# Listas como valores
poderes = {"fuego": [10, 20, 30], "hielo": [5, 15, 25]}
print(poderes)

# Diccionario con listas como valores
equipos = {"Equipo A": ["Andres", "Laura"], "Equipo B": ["Carlos", "Sofia"]}
print(equipos)

# Diccionario vacío
inventario = {}
print(inventario)

# Agregar elementos
tienda = {"espada": 100, "escudo": 150, "pocion": 50}
print("Before:", tienda)
tienda["armadura"] = 300
print("After:", tienda)

# Reemplazo de diccionario
enemigos = {"goblins": 10}
enemigos = {"dragones": 2}
print(enemigos)

# Update (agregar múltiples elementos)
mapa = {"nivel1": "Bosque", "nivel2": "Cueva"}
print("Before:", mapa)

mapa.update({"nivel3": "Castillo", "nivel4": "Volcan"})
print("After:", mapa)

# Actualizar valores
tienda["espada"] = 120
tienda["arco"] = 80
print("Actualizado:", tienda)

print("##################################")

# Otro ejemplo
logros = {"Primer nivel": "Completado", "Jefe final": "Pendiente"}
print("Before:", logros)

logros.update({"Modo difícil": "Desbloqueado"})
print("After1:", logros)

logros["Jefe final"] = "Completado"
print("After2:", logros)

# Combinar listas con zip
usuarios = ['Andres', 'Laura', 'Carlos', 'Sofia']
puntuaciones = [1500, 2300, 1800, 2000]

zipDatos = zip(usuarios, puntuaciones)
print(type(zipDatos))
print(zipDatos)

ranking = {key:value for key, value in zipDatos}
print(ranking)

# Otro ejemplo con zip
armas = ["espada", "arco", "lanza", "dagas"]
danio = [50, 35, 45, 25]

zipArmas = zip(armas, danio)
armasDanio = {key:value for key, value in zipArmas}
print(armasDanio)

print("###########################")

# Diccionario más grande
misiones = ["Rescatar princesa", "Derrotar dragón", "Explorar cueva"]
recompensas = [500, 1000, 300]

historial = {key:value for key, value in zip(misiones, recompensas)}
print(historial)

historial.update({"Buscar tesoro": 700})
historial.update({"Explorar cueva": 350})

print("After:", historial)

# Diccionario dentro de otro diccionario
juego = {"Misiones": historial, "Inventario": {}}
print(juego)
