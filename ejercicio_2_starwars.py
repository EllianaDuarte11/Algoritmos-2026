import contextlib
import io

# graph.py ejecuta código de prueba cuando se importa (imprime cosas), por eso se silencia
with contextlib.redirect_stdout(io.StringIO()):
    from graph import Graph          # el grafo del profe
from heap import HeapMin             # el heap del profe

from starwars_data import personajes, relaciones


# ---------------------------------------------------------------
# Carga del grafo no dirigido
# vértice = nombre del personaje, arista = episodios en los que aparecieron juntos
# ---------------------------------------------------------------
grafo = Graph(is_dir=False)

for nombre in personajes:
    grafo.add_vertex(nombre)

for personaje1, personaje2, episodios in relaciones:
    grafo.add_edge(episodios, personaje1, personaje2)


# ---------------------------------------------------------------
# Funciones
# ---------------------------------------------------------------
def buscar_arbol(bosque, nombre):
    # devuelve la posición del árbol del bosque que contiene al personaje
    for posicion in range(len(bosque)):
        if nombre in bosque[posicion]:
            return posicion


def arbol_expansion_minima(grafo, origen):
    # Kruskal. Se hace acá y no con grafo.kruskal() porque ese separa los nombres con "-"
    # y C-3PO, R2-D2 y BB-8 ya tienen guión en el nombre.
    bosque = []                                   # al principio cada vértice es un árbol
    for vertice in grafo:
        bosque.append([vertice.value])

    aristas = HeapMin()                           # heap con todas las aristas, la de menor peso sale primero
    for vertice in grafo:
        for arista in vertice.edges:
            aristas.arrive([vertice.value, arista.destination], arista.weight)

    elegidas = []                                 # aristas que quedan en el árbol: [origen, destino, peso]
    while aristas.size() > 0 and len(bosque) > 1:
        peso, par = aristas.attention()
        pos_origen = buscar_arbol(bosque, par[0])
        pos_destino = buscar_arbol(bosque, par[1])
        if pos_origen != pos_destino:             # si están en árboles distintos, se unen (así no hay ciclos)
            bosque[pos_origen] = bosque[pos_origen] + bosque[pos_destino]
            bosque.pop(pos_destino)
            elegidas.append([par[0], par[1], peso])

    # me quedo con las aristas del árbol que contiene al vértice de origen
    arbol = bosque[buscar_arbol(bosque, origen)]
    resultado = []
    for arista in elegidas:
        if arista[0] in arbol:
            resultado.append(arista)
    return resultado


def mostrar_arbol(arbol):
    peso_total = 0
    for origen, destino, peso in arbol:
        print(origen, '<->', destino, '| episodios:', peso)
        peso_total += peso
    print('Peso total:', peso_total)


def maximo_de_episodios(grafo):
    maximo = 0
    for vertice in grafo:
        for arista in vertice.edges:
            if arista.weight > maximo:
                maximo = arista.weight
    print('Máximo de episodios que comparten dos personajes:', maximo)
    print('Pares que lo comparten:')
    for vertice in grafo:
        for arista in vertice.edges:
            # la arista está en los dos vértices (grafo no dirigido), se muestra una sola vez
            if arista.weight == maximo and vertice.value < arista.destination:
                print(vertice.value, '-', arista.destination)


def camino_mas_corto(grafo, origen, destino):
    # usa dijkstra del profe y arma el camino igual que en su graph.py
    if not grafo.exist_path(origen, destino):
        print('No hay camino entre', origen, 'y', destino)
        return
    caminos = grafo.dijkstra(origen)
    peso_total = None
    camino = []
    while caminos.size() > 0:
        valor = caminos.pop()                     # [vértice, costo, vértice anterior]
        if valor[0] == destino:
            if peso_total is None:
                peso_total = valor[1]
            camino.append(valor[0])
            destino = valor[2]
    camino.reverse()
    print('Camino:', ' -> '.join(camino))
    print('Costo total:', peso_total)


def personajes_en_todos_los_episodios(grafo, cantidad=9):
    # si dos personajes comparten los 9 episodios, los dos aparecieron en los 9
    for vertice in grafo:
        for arista in vertice.edges:
            if arista.weight == cantidad:
                print(vertice.value)
                break


# ---------------------------------------------------------------
# Programa principal
# ---------------------------------------------------------------
print('Personajes cargados:', len(grafo))

for personaje in ['C-3PO', 'Yoda', 'Leia']:
    print('\n--- Árbol de expansión mínimo desde', personaje, '---')
    mostrar_arbol(arbol_expansion_minima(grafo, personaje))

print('\n--- Máximo de episodios compartidos ---')
maximo_de_episodios(grafo)

print('\n--- Camino más corto de C-3PO a R2-D2 ---')
camino_mas_corto(grafo, 'C-3PO', 'R2-D2')

print('\n--- Camino más corto de Yoda a Darth Vader ---')
camino_mas_corto(grafo, 'Yoda', 'Darth Vader')

print('\n--- Personajes que aparecieron en los 9 episodios ---')
personajes_en_todos_los_episodios(grafo)
