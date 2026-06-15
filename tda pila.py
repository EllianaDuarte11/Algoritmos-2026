class nodoPila:
    def __init__(self):
        self.informacion = None
        self.siguiente = None


class Pila:
    def __init__(self):
        self.cima = None
        self.tamanio = 0


def apilar(pila, elemento):
    nuevo_nodo = nodoPila()
    nuevo_nodo.informacion = elemento
    nuevo_nodo.siguiente = pila.cima
    pila.cima = nuevo_nodo
    pila.tamanio += 1


def desapilar(pila):
    if pila_vacia(pila):
        return None
    elemento = pila.cima.informacion
    pila.cima = pila.cima.siguiente
    pila.tamanio -= 1
    return elemento


def pila_vacia(pila):
    return pila.cima is None


def cima(pila):
    if pila_vacia(pila):
        return None
    return pila.cima.informacion


def tamanio(pila):
    return pila.tamanio
