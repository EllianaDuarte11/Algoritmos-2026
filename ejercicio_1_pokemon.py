from arbol_base import ArbolBase      
from pokemon_data import pokemons     # lista con los datos de los Pokémons


# ---------------------------------------------------------------
# Tres árboles, uno por cada índice pedido
# ---------------------------------------------------------------
arbol_nombres = ArbolBase()   # clave: nombre   -> datos del Pokémon
arbol_numeros = ArbolBase()   # clave: número   -> datos del Pokémon
arbol_tipos = ArbolBase()     # clave: tipo     -> lista con los nombres de los Pokémons de ese tipo

for poke in pokemons:
    arbol_nombres.insert_node(poke['nombre'], poke)
    arbol_numeros.insert_node(poke['numero'], poke)
    for tipo in poke['tipos']:
        nodo = arbol_tipos.search(tipo)
        if nodo is None:                                  
            arbol_tipos.insert_node(tipo, [poke['nombre']])
        else:                                           
            nodo.other_values.append(poke['nombre'])


# ---------------------------------------------------------------
# Funciones
# ---------------------------------------------------------------
def mostrar_datos(poke):
    print('Nombre:', poke['nombre'])
    print('Número:', poke['numero'])
    print('Tipos:', ', '.join(poke['tipos']))
    print('Debilidades:', ', '.join(poke['debilidades']))
    print('Mega evolución:', 'Sí' if poke['mega'] else 'No')
    print('Gigamax:', 'Sí' if poke['gigamax'] else 'No')
    print()


def buscar_por_numero(arbol, numero):
    nodo = arbol.search(numero)
    if nodo is not None:
        mostrar_datos(nodo.other_values)
    else:
        print('No hay un Pokémon con el número', numero)


def buscar_por_proximidad(arbol, texto):
    # muestra los Pokémons cuyo nombre comienza o contiene el texto
    def recorrer(root):
        if root is not None:
            recorrer(root.left)
            if texto.lower() in root.value.lower():
                mostrar_datos(root.other_values)
            recorrer(root.right)
    recorrer(arbol.root)


def nombres_por_tipo(arbol, tipo):
    nodo = arbol.search(tipo)
    if nodo is not None:
        for nombre in sorted(nodo.other_values):
            print(nombre)
    else:
        print('No hay Pokémons de tipo', tipo)


def listar_ascendente(arbol):
    # sirve para el árbol de números y para el de nombres (recorrido inorden)
    def recorrer(root):
        if root is not None:
            recorrer(root.left)
            print(root.other_values['numero'], '-', root.other_values['nombre'])
            recorrer(root.right)
    recorrer(arbol.root)


def debiles_frente_a(arbol, nombre):
    # busca el Pokémon, toma sus tipos y muestra los que son débiles a alguno de esos tipos
    nodo = arbol.search(nombre)
    if nodo is None:
        print('No se encontró a', nombre)
        return
    tipos_ataque = nodo.other_values['tipos']

    def recorrer(root):
        if root is not None:
            recorrer(root.left)
            for tipo in tipos_ataque:
                if tipo in root.other_values['debilidades']:
                    print(root.value)
                    break
            recorrer(root.right)
    print('Débiles frente a', nombre, '(' + ', '.join(tipos_ataque) + '):')
    recorrer(arbol.root)


def mostrar_tipos_y_cantidad(arbol):
    def recorrer(root):
        if root is not None:
            recorrer(root.left)
            print(root.value, ':', len(root.other_values))
            recorrer(root.right)
    recorrer(arbol.root)


def contar(arbol, campo):
    # cuenta los Pokémons donde el campo ('mega' o 'gigamax') es True
    def recorrer(root):
        if root is None:
            return 0
        cantidad = recorrer(root.left) + recorrer(root.right)
        if root.other_values[campo]:
            cantidad += 1
        return cantidad
    return recorrer(arbol.root)


# ---------------------------------------------------------------
# Programa principal
# ---------------------------------------------------------------
print('Pokémons cargados:', len(pokemons))

print('\n--- Datos de un Pokémon por número (25) ---')
buscar_por_numero(arbol_numeros, 25)

print('--- Datos por nombre, búsqueda por proximidad ("bul") ---')
buscar_por_proximidad(arbol_nombres, 'bul')

print('--- Datos por nombre, búsqueda por proximidad ("char") ---')
buscar_por_proximidad(arbol_nombres, 'char')

for tipo in ['fantasma', 'fuego', 'acero', 'eléctrico']:
    print('\n--- Pokémons de tipo', tipo, '---')
    nombres_por_tipo(arbol_tipos, tipo)

print('\n--- Listado ascendente por número ---')
listar_ascendente(arbol_numeros)

print('\n--- Listado ascendente por nombre ---')
listar_ascendente(arbol_nombres)

print('\n--- Listado por nivel (por nombre) ---')
arbol_nombres.by_level()

for atacante in ['Jolteon', 'Lycanroc', 'Tyrantrum']:
    print()
    debiles_frente_a(arbol_nombres, atacante)

print('\n--- Tipos y cantidad de Pokémons de cada tipo ---')
mostrar_tipos_y_cantidad(arbol_tipos)

print('\nPokémons con mega evolución:', contar(arbol_nombres, 'mega'))
print('Pokémons con forma gigamax:', contar(arbol_nombres, 'gigamax'))
