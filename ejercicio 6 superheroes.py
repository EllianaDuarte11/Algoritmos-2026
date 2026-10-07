"""Ejercicio 6 - Superhéroes de comics (TDA lista simplemente enlazada)."""

class nodoLista(object):
    """Clase nodo lista."""
    info, sig = None, None


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


def lista_vacia(lista):
    """Devuelve True si la lista está vacía."""
    return lista.inicio is None


def eliminar(lista, clave, campo=None):
    """Elimina un elemento de la lista y lo devuelve si lo encuentra."""
    dato = None
    if lista.inicio is not None and criterio(lista.inicio.info, campo) == criterio(clave, campo):
        dato = lista.inicio.info
        lista.inicio = lista.inicio.sig
        lista.tamanio -= 1
    elif lista.inicio is not None:
        anterior = lista.inicio
        actual = lista.inicio.sig
        while actual is not None and criterio(actual.info, campo) != criterio(clave, campo):
            anterior = anterior.sig
            actual = actual.sig
        if actual is not None:
            dato = actual.info
            anterior.sig = actual.sig
            lista.tamanio -= 1
    return dato


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
# Registro del superhéroe
# ---------------------------------------------------------------
class Superheroe(object):
    """Registro de un superhéroe de comics."""

    def __init__(self, nombre, anio_aparicion, casa, biografia):
        self.nombre = nombre
        self.anio_aparicion = anio_aparicion
        self.casa = casa
        self.biografia = biografia

    def __str__(self):
        return (f"Nombre: {self.nombre} | Año de aparición: {self.anio_aparicion} | "
                f"Casa: {self.casa} | Biografía: {self.biografia}")


# ---------------------------------------------------------------
# Funciones del ejercicio
# ---------------------------------------------------------------
def eliminar_superheroe(lista, nombre):
    """a. Elimina el nodo del superhéroe indicado."""
    return eliminar(lista, nombre, 'nombre')


def mostrar_anio_aparicion(lista, nombre):
    """b. Muestra el año de aparición del superhéroe indicado."""
    pos = buscar(lista, nombre, 'nombre')
    if pos is not None:
        print(f"{pos.info.nombre} apareció en {pos.info.anio_aparicion}")
    else:
        print(f"{nombre} no está en la lista")


def cambiar_casa(lista, nombre, nueva_casa):
    """c. Cambia la casa de comic del superhéroe indicado."""
    pos = buscar(lista, nombre, 'nombre')
    if pos is not None:
        pos.info.casa = nueva_casa
    else:
        print(f"{nombre} no está en la lista")


def mostrar_por_biografia(lista, palabras):
    """d. Muestra el nombre de los superhéroes cuya biografía menciona alguna de las palabras."""
    aux = lista.inicio
    while aux is not None:
        bio = aux.info.biografia.lower()
        if any(palabra in bio for palabra in palabras):
            print(aux.info.nombre)
        aux = aux.sig


def mostrar_anteriores_a(lista, anio):
    """e. Muestra nombre y casa de los superhéroes con año de aparición anterior al indicado."""
    aux = lista.inicio
    while aux is not None:
        if aux.info.anio_aparicion < anio:
            print(f"{aux.info.nombre} - {aux.info.casa}")
        aux = aux.sig


def mostrar_casa(lista, nombre):
    """f. Muestra la casa a la que pertenece el superhéroe indicado."""
    pos = buscar(lista, nombre, 'nombre')
    if pos is not None:
        print(f"{pos.info.nombre} pertenece a {pos.info.casa}")
    else:
        print(f"{nombre} no está en la lista")


def mostrar_informacion(lista, nombre):
    """g. Muestra toda la información del superhéroe indicado."""
    pos = buscar(lista, nombre, 'nombre')
    if pos is not None:
        print(pos.info)
    else:
        print(f"{nombre} no está en la lista")


def listar_por_iniciales(lista, letras):
    """h. Lista los superhéroes cuyo nombre comienza con alguna de las letras indicadas."""
    aux = lista.inicio
    while aux is not None:
        if aux.info.nombre[0].upper() in letras:
            print(aux.info.nombre)
        aux = aux.sig


def contar_por_casa(lista):
    """i. Determina cuántos superhéroes hay de cada casa de comic."""
    cantidad = {}
    aux = lista.inicio
    while aux is not None:
        cantidad[aux.info.casa] = cantidad.get(aux.info.casa, 0) + 1
        aux = aux.sig
    for casa, total in cantidad.items():
        print(f"{casa}: {total}")


# ---------------------------------------------------------------
# Programa principal
# ---------------------------------------------------------------
if __name__ == '__main__':
    lista = Lista()

    datos = [
        Superheroe("Linterna Verde", 1940, "DC",
                   "Posee un anillo de poder que crea construcciones con su voluntad."),
        Superheroe("Wolverine", 1974, "Marvel",
                   "Mutante con garras de adamantium y factor de curación."),
        Superheroe("Dr. Strange", 1963, "DC",
                   "Hechicero supremo que protege la Tierra de amenazas místicas."),
        Superheroe("Iron Man", 1963, "Marvel",
                   "Genio millonario que construyó una armadura para proteger al mundo."),
        Superheroe("Capitán América", 1941, "Marvel",
                   "Soldado mejorado con un traje de colores patrios y un escudo."),
        Superheroe("Capitana Marvel", 1968, "Marvel",
                   "Piloto con poderes cósmicos y gran fuerza."),
        Superheroe("Mujer Maravilla", 1941, "DC",
                   "Princesa amazona con un lazo de la verdad."),
        Superheroe("Flash", 1940, "DC",
                   "Velocista que se mueve a velocidades increíbles."),
        Superheroe("Star-Lord", 1976, "Marvel",
                   "Mitad humano y mitad celestial, líder de los Guardianes de la Galaxia."),
        Superheroe("Batman", 1939, "DC",
                   "Detective de Gotham que usa un traje con forma de murciélago."),
        Superheroe("Spider-Man", 1962, "Marvel",
                   "Joven con habilidades arácnidas y un traje rojo y azul."),
        Superheroe("Superman", 1938, "DC",
                   "Último hijo de Krypton con superfuerza y vuelo."),
        Superheroe("Black Widow", 1964, "Marvel",
                   "Espía experta en combate, ex agente rusa."),
    ]

    # Se inserta ordenando por nombre (criterio de inserción)
    for heroe in datos:
        insertar(lista, heroe, 'nombre')

    print("a. Eliminar a Linterna Verde")
    eliminado = eliminar_superheroe(lista, "Linterna Verde")
    print("Eliminado:", eliminado.nombre if eliminado else "no se encontró")

    print("\nb. Año de aparición de Wolverine")
    mostrar_anio_aparicion(lista, "Wolverine")

    print("\nc. Cambiar la casa de Dr. Strange a Marvel")
    cambiar_casa(lista, "Dr. Strange", "Marvel")
    mostrar_casa(lista, "Dr. Strange")

    print("\nd. Biografía con 'traje' o 'armadura'")
    mostrar_por_biografia(lista, ["traje", "armadura"])

    print("\ne. Aparición anterior a 1963")
    mostrar_anteriores_a(lista, 1963)

    print("\nf. Casa de Capitana Marvel y Mujer Maravilla")
    mostrar_casa(lista, "Capitana Marvel")
    mostrar_casa(lista, "Mujer Maravilla")

    print("\ng. Información de Flash y Star-Lord")
    mostrar_informacion(lista, "Flash")
    mostrar_informacion(lista, "Star-Lord")

    print("\nh. Superhéroes que comienzan con B, M o S")
    listar_por_iniciales(lista, ["B", "M", "S"])

    print("\ni. Cantidad de superhéroes por casa")
    contar_por_casa(lista)
