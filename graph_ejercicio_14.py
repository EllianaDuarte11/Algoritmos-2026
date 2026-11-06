import contextlib
import io
from math import inf

# graph.py ejecuta código de prueba cuando se importa (imprime cosas), por eso se silencia
with contextlib.redirect_stdout(io.StringIO()):
    from graph import Graph          
from heap import HeapMin             

# ---------------------------------------------------------------
# a. Ambientes de la casa (vértices)
# ---------------------------------------------------------------
ambientes = [
    'cocina', 'comedor', 'cochera', 'quincho', 'baño 1', 'baño 2',
    'habitación 1', 'habitación 2', 'sala de estar', 'terraza', 'patio',
]

# b. (ambiente 1, ambiente 2, distancia en metros)
# Todos los ambientes tienen al menos 3 conexiones; la sala de estar y el patio tienen 5.
conexiones = [
    ('cocina', 'comedor', 4), ('cocina', 'sala de estar', 6), ('cocina', 'patio', 5),
    ('cocina', 'cochera', 9),
    ('comedor', 'sala de estar', 5), ('comedor', 'terraza', 7), ('comedor', 'patio', 8),
    ('sala de estar', 'habitación 1', 9), ('sala de estar', 'habitación 2', 8),
    ('sala de estar', 'baño 1', 4),
    ('habitación 1', 'habitación 2', 4), ('habitación 1', 'baño 1', 3), ('habitación 1', 'baño 2', 6),
    ('habitación 2', 'baño 2', 3), ('baño 1', 'baño 2', 4),
    ('cochera', 'patio', 7), ('cochera', 'quincho', 12),
    ('quincho', 'patio', 6), ('quincho', 'terraza', 10),
    ('terraza', 'patio', 4),
]


# ---------------------------------------------------------------
# Grafo no dirigido
# ---------------------------------------------------------------
casa = Graph(is_dir=False)

for ambiente in ambientes:
    casa.add_vertex(ambiente)

for ambiente1, ambiente2, metros in conexiones:
    casa.add_edge(metros, ambiente1, ambiente2)


# ---------------------------------------------------------------
# Funciones
# ---------------------------------------------------------------
def camino_mas_corto(casa, origen, destino):
    distancia = {}                                
    anterior = {}                                
    for vertice in casa:
        distancia[vertice.value] = inf
        anterior[vertice.value] = None
    distancia[origen] = 0

    pendientes = HeapMin()                        # el heap entrega siempre el de menor distancia
    pendientes.arrive(origen, 0)
    while pendientes.size() > 0:
        costo, actual = pendientes.attention()    # el heap devuelve [distancia, ambiente]
        if costo == distancia[actual]:            # si el costo es viejo (ya se mejoró) se ignora
            posicion = casa.search(actual, 'value')
            for conexion in casa[posicion].edges:
                nuevo_costo = costo + conexion.weight
                if nuevo_costo < distancia[conexion.destination]:
                    distancia[conexion.destination] = nuevo_costo
                    anterior[conexion.destination] = actual
                    pendientes.arrive(conexion.destination, nuevo_costo)

    camino = []
    if distancia[destino] != inf:
        ambiente = destino
        while ambiente is not None:               # se arma el camino de atrás para adelante
            camino.append(ambiente)
            ambiente = anterior[ambiente]
        camino.reverse()
    return camino, distancia[destino]


# ---------------------------------------------------------------
# Programa principal
# ---------------------------------------------------------------
print('--- a y b. Ambientes y sus conexiones (distancia en metros) ---')
for vertice in casa:
    print(vertice.value, '-', len(vertice.edges), 'conexiones:')
    for conexion in vertice.edges:
        print('    ', conexion.destination, ':', conexion.weight, 'm')

print('\n--- c. Árbol de expansión mínimo ---')
arbol = casa.kruskal('cocina')           # texto con las aristas: "origen-destino-peso;origen-destino-peso;..."
metros_cable = 0
for arista in arbol.split(';'):
    origen, destino, metros = arista.split('-')
    print(origen, '<->', destino, ':', metros, 'm')
    metros_cable += int(metros)
print('Metros de cable necesarios para conectar todos los ambientes:', metros_cable)

print('\n--- d. Camino más corto de habitación 1 a sala de estar ---')
camino, metros = camino_mas_corto(casa, 'habitación 1', 'sala de estar')
print('Camino:', ' -> '.join(camino))
print('Metros de cable de red entre el router y el Smart TV:', metros)
