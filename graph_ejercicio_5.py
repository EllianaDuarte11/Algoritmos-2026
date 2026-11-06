import contextlib
import io
from math import inf

# graph.py ejecuta código de prueba cuando se importa (imprime cosas), por eso se silencia
with contextlib.redirect_stdout(io.StringIO()):
    from graph import Graph          # el grafo del profe
from heap import HeapMin             # el heap del profe


# ---------------------------------------------------------------
# Datos de la figura: (nombre del equipo, tipo)
# ---------------------------------------------------------------
equipos = [
    ('Red Hat', 'notebook'), ('Debian', 'notebook'), ('Arch', 'notebook'),
    ('Manjaro', 'pc'), ('Parrot', 'pc'), ('Fedora', 'pc'), ('Ubuntu', 'pc'), ('Mint', 'pc'),
    ('Guaraní', 'servidor'), ('MongoDB', 'servidor'),
    ('Impresora', 'impresora'),
    ('Switch 1', 'switch'), ('Switch 2', 'switch'),
    ('Router 1', 'router'), ('Router 2', 'router'), ('Router 3', 'router'),
]

# (equipo 1, equipo 2, peso de la conexión)
conexiones = [
    ('Manjaro', 'Switch 2', 40), ('Parrot', 'Switch 2', 12), ('MongoDB', 'Switch 2', 5),
    ('Fedora', 'Switch 2', 3), ('Arch', 'Switch 2', 56), ('Switch 2', 'Router 3', 61),
    ('Router 3', 'Router 2', 50), ('Router 3', 'Router 1', 43), ('Router 2', 'Router 1', 37),
    ('Router 2', 'Guaraní', 9), ('Router 2', 'Red Hat', 25), ('Router 1', 'Switch 1', 29),
    ('Switch 1', 'Debian', 17), ('Switch 1', 'Ubuntu', 18), ('Switch 1', 'Impresora', 22),
    ('Switch 1', 'Mint', 80),
]


# ---------------------------------------------------------------
# a y h. Grafo NO dirigido, cada vértice guarda el nombre y el tipo
# ---------------------------------------------------------------
red = Graph(is_dir=False)

for nombre, tipo in equipos:
    red.add_vertex(nombre, tipo)

for equipo1, equipo2, peso in conexiones:
    red.add_edge(peso, equipo1, equipo2)


# ---------------------------------------------------------------
# Funciones
# ---------------------------------------------------------------
def tipo_de(red, nombre):
    posicion = red.search(nombre, 'value')
    return red[posicion].other_values


def camino_mas_corto(red, origen, destino):
    # Dijkstra con el heap del profe. Se hace acá y no con red.dijkstra() porque ese método cambia el costo
    # a mano y después llama a change_priority, que ya no encuentra diferencia y no reordena el heap:
    # los costos pueden dar inf o resultados incorrectos.
    distancia = {}                                # menor costo conocido desde el origen a cada equipo
    anterior = {}                                 # de qué equipo se llega a cada uno por el camino más corto
    for vertice in red:
        distancia[vertice.value] = inf
        anterior[vertice.value] = None
    distancia[origen] = 0

    pendientes = HeapMin()                        # el heap entrega siempre el de menor costo
    pendientes.arrive(origen, 0)
    while pendientes.size() > 0:
        costo, actual = pendientes.attention()    # el heap devuelve [costo, equipo]
        if costo == distancia[actual]:            # si el costo es viejo (ya se mejoró) se ignora
            posicion = red.search(actual, 'value')
            for conexion in red[posicion].edges:
                nuevo_costo = costo + conexion.weight
                if nuevo_costo < distancia[conexion.destination]:
                    distancia[conexion.destination] = nuevo_costo
                    anterior[conexion.destination] = actual
                    pendientes.arrive(conexion.destination, nuevo_costo)

    camino = []
    if distancia[destino] != inf:
        equipo = destino
        while equipo is not None:                 # se arma el camino de atrás para adelante
            camino.append(equipo)
            equipo = anterior[equipo]
        camino.reverse()
    return camino, distancia[destino]


def resolver_b(red):
    # barridos del profe: deep_show (profundidad) y amplitude_show (amplitud)
    for notebook in ['Red Hat', 'Debian', 'Arch']:
        print('\nBarrido en profundidad desde', notebook)
        red.deep_show(notebook)
        print('\nBarrido en amplitud desde', notebook)
        red.amplitude_show(notebook)


def resolver_c(red):
    for pc in ['Manjaro', 'Red Hat', 'Fedora']:
        camino, costo = camino_mas_corto(red, pc, 'Impresora')
        print(pc, ':', ' -> '.join(camino), '| costo:', costo)


# ---------------------------------------------------------------
# Programa principal
# ---------------------------------------------------------------
print('--- a. Equipos cargados (nombre -> tipo) ---')
for vertice in red:
    print(vertice.value, '->', vertice.other_values)

print('\n--- b. Barridos desde los tres notebooks ---')
resolver_b(red)

print('\n--- c. Camino más corto para imprimir ---')
resolver_c(red)

print('\n--- d. Árbol de expansión mínimo ---')
arbol = red.kruskal('Router 1')          # texto con las aristas: "origen-destino-peso;origen-destino-peso;..."
peso_total = 0
for arista in arbol.split(';'):
    origen, destino, peso = arista.split('-')
    print(origen, '<->', destino, '| peso:', peso)
    peso_total += int(peso)
print('Peso total:', peso_total)

print('\n--- e. PC (no notebook) con el camino más corto al servidor Guaraní ---')
pcs = []
for vertice in red:
    if vertice.other_values == 'pc':
        pcs.append(vertice.value)
mejor_pc = None
mejor_camino = None
mejor_costo = None
for pc in pcs:
    camino, costo = camino_mas_corto(red, pc, 'Guaraní')
    if mejor_costo is None or costo < mejor_costo:
        mejor_pc = pc
        mejor_camino = camino
        mejor_costo = costo
print(mejor_pc, ':', ' -> '.join(mejor_camino), '| costo:', mejor_costo)

print('\n--- f. Computadora del Switch 1 con el camino más corto al servidor MongoDB ---')
pos_switch = red.search('Switch 1', 'value')
mejor_equipo = None
mejor_camino = None
mejor_costo = None
for conexion in red[pos_switch].edges:
    equipo = conexion.destination
    if tipo_de(red, equipo) in ['pc', 'notebook']:        # se descartan la impresora y el router
        camino, costo = camino_mas_corto(red, equipo, 'MongoDB')
        if mejor_costo is None or costo < mejor_costo:
            mejor_equipo = equipo
            mejor_camino = camino
            mejor_costo = costo
print(mejor_equipo, ':', ' -> '.join(mejor_camino), '| costo:', mejor_costo)

print('\n--- g. La impresora pasa al Router 2: se resuelve de nuevo ---')
red.delete_edge('Switch 1', 'Impresora')
red.add_edge(22, 'Router 2', 'Impresora')                # el enunciado no da el peso, se usa el mismo (22)
print('\nPunto b:')
resolver_b(red)
print('\nPunto c:')
resolver_c(red)
