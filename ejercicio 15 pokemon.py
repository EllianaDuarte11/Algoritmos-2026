"""Ejercicio 15 - Entrenadores Pokémon (TDA lista de lista)."""

class nodoLista(object):
    """Clase nodo lista."""
    info, sig = None, None

    def __init__(self):
        self.info = None
        self.sig = None
        self.sublista = Lista()


class Lista(object):
    """Clase lista simplemente enlazada."""

    def __init__(self):
        """Crea una lista vacía."""
        self.inicio = None
        self.tamanio = 0


def criterio(dato, campo=None):
    """Determina el campo por el cual se debe comparar el dato."""
    dic = {}
    if hasattr(dato, '__dict__'):
        dic = dato.__dict__
    if campo is None or campo not in dic:
        return dato
    else:
        return dic[campo]


def insertar(lista, dato, campo=None):
    """Inserta el dato pasado en la lista."""
    nodo = nodoLista()
    nodo.info = dato
    if (lista.inicio is None) or (criterio(lista.inicio.info, campo) > criterio(dato, campo)):
        nodo.sig = lista.inicio
        lista.inicio = nodo
    else:
        ant = lista.inicio
        act = lista.inicio.sig
        while act is not None and criterio(act.info, campo) < criterio(dato, campo):
            ant = ant.sig
            act = act.sig
        nodo.sig = act
        ant.sig = nodo
    lista.tamanio += 1


def buscar(lista, buscado, campo=None):
    """Devuelve la dirección del elemento buscado."""
    aux = lista.inicio
    while aux is not None and criterio(aux.info, campo) != criterio(buscado, campo):
        aux = aux.sig
    return aux


def barrido(lista):
    """Realiza un barrido de la lista mostrando sus valores."""
    aux = lista.inicio
    while aux is not None:
        print(aux.info)
        aux = aux.sig


# ---------------------------------------------------------------
# Registros
# ---------------------------------------------------------------
class Entrenador(object):
    """Registro de un entrenador Pokémon."""

    def __init__(self, nombre, torneos_ganados, batallas_perdidas, batallas_ganadas):
        self.nombre = nombre
        self.torneos_ganados = torneos_ganados
        self.batallas_perdidas = batallas_perdidas
        self.batallas_ganadas = batallas_ganadas

    def __str__(self):
        return (f"Entrenador: {self.nombre} | Torneos ganados: {self.torneos_ganados} | "
                f"Batallas perdidas: {self.batallas_perdidas} | "
                f"Batallas ganadas: {self.batallas_ganadas}")


class Pokemon(object):
    """Registro de un Pokémon."""

    def __init__(self, nombre, nivel, tipo, subtipo):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

    def __str__(self):
        return (f"Pokémon: {self.nombre} | Nivel: {self.nivel} | "
                f"Tipo: {self.tipo} | Subtipo: {self.subtipo}")


# ---------------------------------------------------------------
# Funciones del ejercicio
# ---------------------------------------------------------------
def cargar_entrenador(lista, entrenador, pokemons):
    """Inserta un entrenador (ordenado por nombre) y sus Pokémons en su sublista."""
    insertar(lista, entrenador, 'nombre')
    pos = buscar(lista, entrenador.nombre, 'nombre')
    for p in pokemons:
        insertar(pos.sublista, p, 'nombre')


def cantidad_pokemons(lista, nombre):
    """a. Cantidad de Pokémons de un entrenador."""
    pos = buscar(lista, nombre, 'nombre')
    if pos is not None:
        print(f"{pos.info.nombre} tiene {pos.sublista.tamanio} Pokémons")
    else:
        print(f"{nombre} no está en la lista")


def entrenadores_mas_de_tres_torneos(lista):
    """b. Lista los entrenadores que ganaron más de tres torneos."""
    aux = lista.inicio
    while aux is not None:
        if aux.info.torneos_ganados > 3:
            print(aux.info)
        aux = aux.sig


def pokemon_mayor_nivel(sublista):
    """Devuelve el Pokémon de mayor nivel de una sublista."""
    mayor = None
    aux = sublista.inicio
    while aux is not None:
        if mayor is None or aux.info.nivel > mayor.nivel:
            mayor = aux.info
        aux = aux.sig
    return mayor


def pokemon_mayor_nivel_del_mejor_entrenador(lista):
    """c. Pokémon de mayor nivel del entrenador con más torneos ganados."""
    mejor = lista.inicio
    aux = lista.inicio
    while aux is not None:
        if aux.info.torneos_ganados > mejor.info.torneos_ganados:
            mejor = aux
        aux = aux.sig
    if mejor is not None:
        print(f"Entrenador con más torneos: {mejor.info.nombre} ({mejor.info.torneos_ganados})")
        print(pokemon_mayor_nivel(mejor.sublista))


def mostrar_entrenador(lista, nombre):
    """d. Muestra todos los datos de un entrenador y sus Pokémons."""
    pos = buscar(lista, nombre, 'nombre')
    if pos is not None:
        print(pos.info)
        barrido(pos.sublista)
    else:
        print(f"{nombre} no está en la lista")


def porcentaje_ganadas(entrenador):
    """Porcentaje de batallas ganadas sobre el total de batallas."""
    total = entrenador.batallas_ganadas + entrenador.batallas_perdidas
    return entrenador.batallas_ganadas * 100 / total if total > 0 else 0


def entrenadores_por_porcentaje(lista, minimo=79):
    """e. Entrenadores cuyo porcentaje de batallas ganadas supera el mínimo."""
    aux = lista.inicio
    while aux is not None:
        pct = porcentaje_ganadas(aux.info)
        if pct > minimo:
            print(f"{aux.info.nombre} - {pct:.2f}% de batallas ganadas")
        aux = aux.sig


def tiene_tipo_subtipo(sublista, tipo, subtipo):
    """Indica si la sublista tiene un Pokémon con ese tipo y subtipo."""
    aux = sublista.inicio
    while aux is not None:
        if aux.info.tipo == tipo and aux.info.subtipo == subtipo:
            return True
        aux = aux.sig
    return False


def entrenadores_por_tipos(lista):
    """f. Entrenadores con Pokémons tipo fuego/planta o agua/volador (tipo/subtipo)."""
    aux = lista.inicio
    while aux is not None:
        if (tiene_tipo_subtipo(aux.sublista, "fuego", "planta")
                or tiene_tipo_subtipo(aux.sublista, "agua", "volador")):
            print(aux.info.nombre)
        aux = aux.sig


def promedio_nivel(lista, nombre):
    """g. Promedio de nivel de los Pokémons de un entrenador."""
    pos = buscar(lista, nombre, 'nombre')
    if pos is None:
        print(f"{nombre} no está en la lista")
    elif pos.sublista.tamanio == 0:
        print(f"{nombre} no tiene Pokémons")
    else:
        suma = 0
        aux = pos.sublista.inicio
        while aux is not None:
            suma += aux.info.nivel
            aux = aux.sig
        print(f"Promedio de nivel de {nombre}: {suma / pos.sublista.tamanio:.2f}")


def cuantos_tienen_pokemon(lista, nombre_pokemon):
    """h. Cuántos entrenadores tienen un determinado Pokémon."""
    cantidad = 0
    aux = lista.inicio
    while aux is not None:
        if buscar(aux.sublista, nombre_pokemon, 'nombre') is not None:
            cantidad += 1
        aux = aux.sig
    print(f"{cantidad} entrenador(es) tienen a {nombre_pokemon}")


def entrenadores_con_repetidos(lista):
    """i. Entrenadores con Pokémons repetidos (la sublista está ordenada por nombre)."""
    aux = lista.inicio
    while aux is not None:
        p = aux.sublista.inicio
        repetido = False
        while p is not None and p.sig is not None and not repetido:
            if p.info.nombre == p.sig.info.nombre:
                repetido = True
            p = p.sig
        if repetido:
            print(aux.info.nombre)
        aux = aux.sig


def entrenadores_con_pokemons(lista, nombres):
    """j. Entrenadores que tengan alguno de los Pokémons indicados."""
    aux = lista.inicio
    while aux is not None:
        for nombre in nombres:
            if buscar(aux.sublista, nombre, 'nombre') is not None:
                print(f"{aux.info.nombre} tiene a {nombre}")
        aux = aux.sig


def entrenador_tiene_pokemon(lista, nombre_entrenador, nombre_pokemon):
    """k. Determina si el entrenador X tiene al Pokémon Y y muestra los datos de ambos."""
    pos = buscar(lista, nombre_entrenador, 'nombre')
    if pos is None:
        print(f"{nombre_entrenador} no está en la lista")
        return
    pok = buscar(pos.sublista, nombre_pokemon, 'nombre')
    if pok is not None:
        print(f"{nombre_entrenador} tiene a {nombre_pokemon}:")
        print(pos.info)
        print(pok.info)
    else:
        print(f"{nombre_entrenador} no tiene a {nombre_pokemon}")


# ---------------------------------------------------------------
# Programa principal
# ---------------------------------------------------------------
if __name__ == '__main__':
    entrenadores = Lista()

    cargar_entrenador(entrenadores, Entrenador("Ash", 5, 20, 80), [
        Pokemon("Pikachu", 50, "electrico", "ninguno"),
        Pokemon("Charizard", 60, "fuego", "volador"),
        Pokemon("Bulbasaur", 30, "planta", "veneno"),
        Pokemon("Pikachu", 25, "electrico", "ninguno"),
    ])
    cargar_entrenador(entrenadores, Entrenador("Misty", 2, 30, 70), [
        Pokemon("Starmie", 40, "agua", "psiquico"),
        Pokemon("Wingull", 22, "agua", "volador"),
    ])
    cargar_entrenador(entrenadores, Entrenador("Brock", 4, 25, 75), [
        Pokemon("Onix", 35, "roca", "tierra"),
        Pokemon("Tyrantrum", 45, "roca", "dragon"),
    ])
    cargar_entrenador(entrenadores, Entrenador("Gary", 6, 10, 90), [
        Pokemon("Blastoise", 55, "agua", "ninguno"),
        Pokemon("Typhlosion", 52, "fuego", "planta"),
        Pokemon("Terrakion", 58, "roca", "lucha"),
    ])

    print("a. Cantidad de Pokémons de Ash")
    cantidad_pokemons(entrenadores, "Ash")

    print("\nb. Entrenadores con más de 3 torneos")
    entrenadores_mas_de_tres_torneos(entrenadores)

    print("\nc. Pokémon de mayor nivel del entrenador con más torneos")
    pokemon_mayor_nivel_del_mejor_entrenador(entrenadores)

    print("\nd. Datos de Ash y sus Pokémons")
    mostrar_entrenador(entrenadores, "Ash")

    print("\ne. Porcentaje de batallas ganadas > 79%")
    entrenadores_por_porcentaje(entrenadores)

    print("\nf. Pokémons fuego/planta o agua/volador")
    entrenadores_por_tipos(entrenadores)

    print("\ng. Promedio de nivel de Ash")
    promedio_nivel(entrenadores, "Ash")

    print("\nh. Cuántos entrenadores tienen a Pikachu")
    cuantos_tienen_pokemon(entrenadores, "Pikachu")

    print("\ni. Entrenadores con Pokémons repetidos")
    entrenadores_con_repetidos(entrenadores)

    print("\nj. Entrenadores con Tyrantrum, Terrakion o Wingull")
    entrenadores_con_pokemons(entrenadores, ["Tyrantrum", "Terrakion", "Wingull"])

    print("\nk. ¿Misty tiene a Wingull?")
    entrenador_tiene_pokemon(entrenadores, "Misty", "Wingull")
