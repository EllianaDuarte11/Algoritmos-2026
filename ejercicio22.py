from tda_cola import (Cola, arribo, atencion,
                      cola_vacia, tamanio, mover_al_final)


# Cada personaje se representa como una tupla: (nombre_personaje, superheroe, genero)
# Ejemplo: ("Tony Stark", "Iron Man", "M")


# a) Determinar el nombre del personaje de la superhéroe Capitana Marvel
def buscar_por_superheroe(cola, nombre_superheroe):
    resultado = None
    cantidad = tamanio(cola)
    for _ in range(cantidad):
        personaje = atencion(cola)
        if personaje[1] == nombre_superheroe:
            resultado = personaje[0]
        arribo(cola, personaje)
    return resultado


# b) Mostrar los nombres de los superhéroes femeninos
def mostrar_superheroes_femeninos(cola):
    cantidad = tamanio(cola)
    encontro = False
    for _ in range(cantidad):
        personaje = atencion(cola)
        if personaje[2] == "F":
            print(f"  {personaje[1]}")
            encontro = True
        arribo(cola, personaje)
    if not encontro:
        print("  No hay superhéroes femeninos en la cola.")


# c) Mostrar los nombres de los personajes masculinos
def mostrar_personajes_masculinos(cola):
    cantidad = tamanio(cola)
    encontro = False
    for _ in range(cantidad):
        personaje = atencion(cola)
        if personaje[2] == "M":
            print(f"  {personaje[0]}")
            encontro = True
        arribo(cola, personaje)
    if not encontro:
        print("  No hay personajes masculinos en la cola.")


# d) Determinar el nombre del superhéroe del personaje Scott Lang
def buscar_superheroe_por_personaje(cola, nombre_personaje):
    resultado = None
    cantidad = tamanio(cola)
    for _ in range(cantidad):
        personaje = atencion(cola)
        if personaje[0] == nombre_personaje:
            resultado = personaje[1]
        arribo(cola, personaje)
    return resultado


# e) Mostrar todos los datos de superhéroes o personajes cuyos nombres comienzan con S
def mostrar_comienzan_con_s(cola):
    cantidad = tamanio(cola)
    encontro = False
    for _ in range(cantidad):
        personaje = atencion(cola)
        if personaje[0].startswith("S") or personaje[1].startswith("S"):
            print(f"  Personaje: {personaje[0]} | Superhéroe: {personaje[1]} | Género: {personaje[2]}")
            encontro = True
        arribo(cola, personaje)
    if not encontro:
        print("  No hay personajes o superhéroes que comiencen con S.")


# f) Determinar si Carol Danvers está en la cola e indicar su nombre de superhéroe
def buscar_carol_danvers(cola):
    resultado = None
    cantidad = tamanio(cola)
    for _ in range(cantidad):
        personaje = atencion(cola)
        if personaje[0] == "Carol Danvers":
            resultado = personaje[1]
        arribo(cola, personaje)
    return resultado


# ---- Programa principal ----
if __name__ == "__main__":

    cola_mcu = Cola()

    # Datos de prueba: (nombre_personaje, superheroe, genero)
    personajes = [
        ("Tony Stark",        "Iron Man",         "M"),
        ("Steve Rogers",      "Capitán América",  "M"),
        ("Natasha Romanoff",  "Black Widow",      "F"),
        ("Thor Odinson",      "Thor",             "M"),
        ("Bruce Banner",      "Hulk",             "M"),
        ("Carol Danvers",     "Capitana Marvel",  "F"),
        ("Scott Lang",        "Ant-Man",          "M"),
        ("Wanda Maximoff",    "Scarlet Witch",    "F"),
        ("Sam Wilson",        "Falcon",           "M"),
        ("Peter Parker",      "Spider-Man",       "M"),
        ("Shuri",             "Shuri",            "F"),
        ("Stephen Strange",   "Doctor Strange",   "M"),
    ]

    for p in personajes:
        arribo(cola_mcu, p)

    print("=== Ejercicio 22: Personajes MCU ===\n")

    # --- Inciso a ---
    print("a) Nombre del personaje de la superhéroe Capitana Marvel:")
    resultado = buscar_por_superheroe(cola_mcu, "Capitana Marvel")
    if resultado:
        print(f"  {resultado}")
    else:
        print("  No encontrado.")

    # --- Inciso b ---
    print("\nb) Superhéroes femeninos:")
    mostrar_superheroes_femeninos(cola_mcu)

    # --- Inciso c ---
    print("\nc) Personajes masculinos:")
    mostrar_personajes_masculinos(cola_mcu)

    # --- Inciso d ---
    print("\nd) Superhéroe del personaje Scott Lang:")
    resultado = buscar_superheroe_por_personaje(cola_mcu, "Scott Lang")
    if resultado:
        print(f"  {resultado}")
    else:
        print("  No encontrado.")

    # --- Inciso e ---
    print("\ne) Personajes o superhéroes cuyos nombres comienzan con S:")
    mostrar_comienzan_con_s(cola_mcu)

    # --- Inciso f ---
    print("\nf) ¿Carol Danvers está en la cola?")
    resultado = buscar_carol_danvers(cola_mcu)
    if resultado:
        print(f"  Sí. Su nombre de superhéroe es: {resultado}")
    else:
        print("  No se encuentra en la cola.")
