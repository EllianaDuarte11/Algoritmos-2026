#Ejercicio20
pila = []

def push(movimiento):
    pila.append(movimiento)

def pop():
    if not pila_vacia():
        return pila.pop()
    else:
        print("La pila está vacía")

def pila_vacia():
    return len(pila) == 0

# --- DIRECCIONES VÁLIDAS ---
direcciones = ["norte", "sur", "este", "oeste",
               "noreste", "noroeste", "sureste", "suroeste"]

print("=== REGISTRO DE MOVIMIENTOS DEL ROBOT ===")

while True:
    print("\nDirecciones: norte, sur, este, oeste, noreste, noroeste, sureste, suroeste")
    direccion = input("Ingrese dirección (o 'fin' para terminar): ").lower()

    if direccion == "fin":
        break

    if direccion not in direcciones:
        print("Dirección no válida, intente de nuevo")
        continue

    pasos = int(input("Ingrese cantidad de pasos: "))

    movimiento = (direccion, pasos)
    push(movimiento)
    print(f"Movimiento registrado: {pasos} pasos hacia el {direccion}")

# --- MOSTRAR MOVIMIENTOS REGISTRADOS ---
print("\n=== MOVIMIENTOS REALIZADOS ===")
for i, mov in enumerate(pila):
    print(f"{i+1}. {mov[1]} pasos hacia el {mov[0]}")

print("\n=== SECUENCIA PARA VOLVER AL ORIGEN ===")

# Direcciones opuestas
opuestas = {
    "norte": "sur",
    "sur": "norte",
    "este": "oeste",
    "oeste": "este",
    "noreste": "suroeste",
    "suroeste": "noreste",
    "noroeste": "sureste",
    "sureste": "noroeste"
}

paso_num = 1
while not pila_vacia():
    mov = pop()
    direccion_vuelta = opuestas[mov[0]]
    print(f"{paso_num}. {mov[1]} pasos hacia el {direccion_vuelta}")
    paso_num += 1

print("\n¡El robot volvió a su lugar de partida!")
