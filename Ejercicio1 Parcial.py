# Ejercicio 1: Dado una lista simple de python (array) de 15 superheroes realizar dos funciones recursivas:
   #funcion recursiva  para buscar, determinar si Capitan America esta en la lista.
   #funcion recursiva para listar los superheroes de la lista.


# Lista simple de 15 superhéroes 
superheroes = [
    "Iron Man",
    "Thor",
    "Hulk",
    "Black Widow",
    "Hawkeye",
    "Spider-Man",
    "Doctor Strange",
    "Black Panther",
    "Captain Marvel",
    "Ant-Man",
    "Scarlet Witch",
    "Vision",
    "Falcon",
    "Capitán América",
    "Star-Lord",
]


def buscar_superheroe(lista, objetivo, indice=0):

        # Caso base: recorrimos toda la lista y no se encontró
    if indice == len(lista):
        return False

    # Caso base: encontramos el elemento buscado
    if lista[indice] == objetivo:
        return True

    # Caso recursivo: seguir buscando en el resto de la lista
    return buscar_superheroe(lista, objetivo, indice + 1)


def listar_superheroes(lista, indice=0):
    
    # Caso base: ya recorrimos toda la lista
    if indice == len(lista):
        return

    # Imprime el superhéroe actual
    print(f"{indice + 1}. {lista[indice]}")

    # Llamada recursiva para el siguiente elemento
    listar_superheroes(lista, indice + 1)


# ---------- PROGRAMA PRINCIPAL ----------
if __name__ == "__main__":
    print("=== Lista de los 15 superhéroes ===")
    listar_superheroes(superheroes)

    print("\n=== Búsqueda de 'Capitán América' ===")
    encontrado = buscar_superheroe(superheroes, "Capitán América")

    if encontrado:
        print("Capitán América SÍ está en la lista.")
    else:
        print("Capitán América NO está en la lista.")