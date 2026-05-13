#Ejercicio 24 - Pila de personajes

pila = []

def push(personaje):
    pila.append(personaje)

def pop():
    if not pila_vacia():
        return pila.pop()
    else:
        print("La pila está vacía")

def pila_vacia():
    return len(pila) == 0

def peek():
    if not pila_vacia():
        return pila[-1]

#CARGA DE PERSONAJES (nombre, cantidad de películas)
personajes = [
    ("Iron Man", 10),
    ("Capitán América", 9),
    ("Thor", 8),
    ("Hulk", 7),
    ("Viuda Negra", 7),
    ("Ojo de Halcón", 6),
    ("Doctor Strange", 5),
    ("Groot", 5),
    ("Gamora", 6),
    ("Star-Lord", 5),
    ("Drax", 5),
    ("Rocket Raccoon", 6),
    ("Visión", 4),
    ("Wanda", 6),
    ("Cull Obsidian", 2),
]

for p in personajes:
    push(p)

# a. Posición de Rocket Raccoon y Groot (cima = posición 1)
def buscar_posicion(nombres_buscados):
    temp = []
    posiciones = {}
    posicion = 1

    while not pila_vacia():
        personaje = pop()
        temp.append(personaje)
        if personaje[0] in nombres_buscados:
            posiciones[personaje[0]] = posicion
        posicion += 1

    # Restaurar pila
    while temp:
        push(temp.pop())

    return posiciones

print("=== a. Posición de Rocket Raccoon y Groot ===")
buscados = ["Rocket Raccoon", "Groot"]
posiciones = buscar_posicion(buscados)
for nombre, pos in posiciones.items():
    print(f"  {nombre} está en la posición {pos}")

# b. Personajes con más de 5 películas

def mas_de_cinco_peliculas():
    temp = []
    resultado = []

    while not pila_vacia():
        personaje = pop()
        temp.append(personaje)
        if personaje[1] > 5:
            resultado.append(personaje)

    while temp:
        push(temp.pop())

    return resultado

print("\n=== b. Personajes con más de 5 películas ===")
lista = mas_de_cinco_peliculas()
for nombre, cantidad in lista:
    print(f"  {nombre}: {cantidad} películas")

# c. Películas de Viuda Negra
def peliculas_viuda_negra():
    temp = []
    cantidad = 0

    while not pila_vacia():
        personaje = pop()
        temp.append(personaje)
        if personaje[0] == "Viuda Negra":
            cantidad = personaje[1]

    while temp:
        push(temp.pop())

    return cantidad

print("\n=== c. Películas de Viuda Negra ===")
cantidad = peliculas_viuda_negra()
if cantidad > 0:
    print(f"  Viuda Negra participó en {cantidad} películas")
else:
    print("  Viuda Negra no está en la pila")

# d. Personajes cuyo nombre empieza con C, D o G
def nombres_con_letras(letras):
    temp = []
    resultado = []

    while not pila_vacia():
        personaje = pop()
        temp.append(personaje)
        if personaje[0][0].upper() in letras:
            resultado.append(personaje[0])

    while temp:
        push(temp.pop())

    return resultado

print("\n=== d. Personajes que empiezan con C, D o G ===")
letras = ["C", "D", "G"]
encontrados = nombres_con_letras(letras)
for nombre in encontrados:
    print(f"  {nombre}")
