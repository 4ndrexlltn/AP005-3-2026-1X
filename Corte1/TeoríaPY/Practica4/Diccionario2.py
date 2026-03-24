################# Diccionarios Parte 2 - Ingeniería ####################

# Acceder a valores por medio de la clave
voltajes = {"Sensor1": 5, "Sensor2": 3.3, "Sensor3": 12, "Sensor4": 9}
print(voltajes["Sensor1"])
print(voltajes["Sensor3"])
# print(voltajes["Sensor5"]) # Error si no existe la clave

# Diccionario con listas como valores
componentes = {
    "resistencias": [100, 220, 330],
    "capacitores": [10, 100, 1000],
    "inductores": [1, 5, 10]
}

print(componentes["resistencias"])
print(componentes["capacitores"])

# Verificar si una clave existe
buscar = "Sensor5"

if buscar in voltajes:
    print(voltajes[buscar])
else:
    print("No se encontró la clave Sensor5")

# Agregar nueva clave
componentes["diodos"] = ["1N4007", "LED"]
if "diodos" in componentes:
    print(componentes["diodos"])

# Forma segura con get()
print(voltajes.get("Sensor2"))
print(voltajes.get("Sensor10"))  # None si no existe

# Ejemplo práctico
ids_dispositivos = {"Arduino": 101, "Raspberry": 202, "ESP32": 303}
print(ids_dispositivos.get("Arduino"))

if ids_dispositivos.get("Arduino") == None:
    arduino_id = 0
else:
    arduino_id = ids_dispositivos.get("Arduino")

print(arduino_id)

if ids_dispositivos.get("PIC") == None:
    pic_id = 999

print(pic_id)

# Eliminar elementos con pop()
equipos = {1: "Osciloscopio", 2: "Multimetro", 3: "Fuente", 4: "Generador"}
print(equipos.pop(3, "No existe"))
print(equipos)

# Caso donde no existe la clave
print(equipos.pop(10, "No existe"))

# Uso práctico de pop
energia = {"bateria": 50, "panel": 30, "generador": 100}
cargaTotal = 0

cargaTotal += energia.pop("panel", 0)
cargaTotal += energia.pop("generador", 0)
cargaTotal += energia.pop("red", 0)

print(energia)
print(cargaTotal)

# Obtener claves
notas = {"Juan":[4.0, 3.5, 4.5], "Ana":[5.0, 4.8, 4.9], "Luis":[3.0, 3.2, 3.8]}
print(list(notas))

listaEstudiantes = list(notas)
print(listaEstudiantes)

# Otra forma
for estudiante in notas.keys():
    print(estudiante)

# keys()
modulos = {"Circuitos": 10, "Programacion": 15, "Control": 12}
claves = modulos.keys()
print(claves)
print(type(claves))

print("###########################")

# values()
for listaNotas in notas.values():
    print(listaNotas)

valores = notas.values()
print(valores)
print(type(valores))

# Operar valores
total = 0
for horas in modulos.values():
    total += horas
    print(total)

print("Total horas:", total)

# items()
dispositivos = {"Arduino": 50, "Raspberry": 70, "ESP32": 30}
items = dispositivos.items()
print(items)
print(type(items))

for nombre, precio in dispositivos.items():
    print(nombre + " cuesta " + str(precio) + " dolares.")

# Otro ejemplo con items
uso_tecnologia = {"Ingeniero": 20, "Tecnico": 35, "Estudiante": 45}

for rol, porcentaje in uso_tecnologia.items():
    print("El " + str(porcentaje) + "% de los usuarios son " + rol)
