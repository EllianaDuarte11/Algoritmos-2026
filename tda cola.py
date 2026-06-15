class nodoCola:
    def __init__(self):
        self.informacion = None
        self.siguiente = None


class Cola:
    def __init__(self):
        self.frente = None
        self.final = None
        self.tamanio = 0


def arribo(cola, elemento):
    nuevo_nodo = nodoCola()
    nuevo_nodo.informacion = elemento
    if cola_vacia(cola):
        cola.frente = nuevo_nodo
    else:
        cola.final.siguiente = nuevo_nodo
    cola.final = nuevo_nodo
    cola.tamanio += 1


def atencion(cola):
    if cola_vacia(cola):
        return None
    elemento = cola.frente.informacion
    cola.frente = cola.frente.siguiente
    if cola.frente is None:
        cola.final = None
    cola.tamanio -= 1
    return elemento


def cola_vacia(cola):
    return cola.frente is None


def en_frente(cola):
    if cola_vacia(cola):
        return None
    return cola.frente.informacion


def tamanio(cola):
    return cola.tamanio


def mover_al_final(cola):
    elemento = atencion(cola)
    arribo(cola, elemento)
