from tda_cola import (Cola, nodoCola, arribo, atencion,
                      cola_vacia, tamanio, mover_al_final)


# Una notificacion se representa como una tupla: (hora, aplicacion, mensaje)
# Ejemplo: ("10:30", "Facebook", "Juan te etiqueto en una foto")


# a) Eliminar de la cola todas las notificaciones de Facebook
def eliminar_facebook(cola):
    cantidad = tamanio(cola)
    for _ in range(cantidad):
        notificacion = atencion(cola)
        if notificacion[1] != "Facebook":
            arribo(cola, notificacion)


# b) Mostrar notificaciones de Twitter cuyo mensaje incluya 'Python',
#    sin perder datos en la cola
def mostrar_twitter_python(cola):
    cantidad = tamanio(cola)
    encontro = False
    for _ in range(cantidad):
        notificacion = atencion(cola)
        if notificacion[1] == "Twitter" and "Python" in notificacion[2]:
            print(f"  Hora: {notificacion[0]} | App: {notificacion[1]} | Mensaje: {notificacion[2]}")
            encontro = True
        arribo(cola, notificacion)
    if not encontro:
        print("  No se encontraron notificaciones de Twitter con la palabra 'Python'.")


# c) Usar una pila para almacenar temporalmente las notificaciones
#    producidas entre las 11:43 y las 15:57, y determinar cuantas son
def notificaciones_en_rango(cola):
    from tda_pila import Pila, apilar, desapilar, pila_vacia, tamanio as tamanio_pila

    pila_rango = Pila()
    cantidad = tamanio(cola)

    hora_inicio = "11:43"
    hora_fin = "15:57"

    for _ in range(cantidad):
        notificacion = atencion(cola)
        hora = notificacion[0]
        if hora_inicio <= hora <= hora_fin:
            apilar(pila_rango, notificacion)
        arribo(cola, notificacion)

    cantidad_rango = tamanio_pila(pila_rango)
    print(f"  Cantidad de notificaciones entre {hora_inicio} y {hora_fin}: {cantidad_rango}")

    print("  Notificaciones en la pila (de cima a fondo):")
    while not pila_vacia(pila_rango):
        notif = desapilar(pila_rango)
        print(f"    Hora: {notif[0]} | App: {notif[1]} | Mensaje: {notif[2]}")

    return cantidad_rango


# ---- Programa principal ----
if __name__ == "__main__":

    cola_notificaciones = Cola()

    # Datos de prueba: (hora, aplicacion, mensaje)
    notificaciones = [
        ("09:15", "Facebook",  "Maria te envio una solicitud de amistad"),
        ("10:05", "Twitter",   "Nuevo seguidor: @dev_arg"),
        ("11:43", "Instagram", "Carlos comento tu foto"),
        ("12:00", "Twitter",   "Tendencia: aprendiendo Python hoy"),
        ("13:30", "Facebook",  "Te etiquetaron en una publicacion"),
        ("14:10", "Twitter",   "RT de tu tweet sobre Python"),
        ("15:00", "WhatsApp",  "Mensaje de Ana"),
        ("15:57", "Twitter",   "Python 3.13 fue lanzado"),
        ("16:45", "Facebook",  "Juan comento tu foto"),
        ("17:20", "Instagram", "Nueva historia de Lucas"),
    ]

    for n in notificaciones:
        arribo(cola_notificaciones, n)

    print("=== Ejercicio 10: Notificaciones de Redes Sociales ===\n")

    # --- Inciso a ---
    print("a) Eliminando todas las notificaciones de Facebook...")
    eliminar_facebook(cola_notificaciones)
    print(f"   Cola luego de eliminar Facebook ({tamanio(cola_notificaciones)} notificaciones):")
    cant = tamanio(cola_notificaciones)
    for _ in range(cant):
        n = atencion(cola_notificaciones)
        print(f"   Hora: {n[0]} | App: {n[1]} | Mensaje: {n[2]}")
        arribo(cola_notificaciones, n)

    # --- Inciso b ---
    print("\nb) Notificaciones de Twitter con la palabra 'Python':")
    mostrar_twitter_python(cola_notificaciones)

    # --- Inciso c ---
    print("\nc) Notificaciones entre las 11:43 y las 15:57 (usando pila):")
    notificaciones_en_rango(cola_notificaciones)
