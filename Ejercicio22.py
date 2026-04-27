# Ejercicio 22

def usar_la_fuerza(mochila, indice=0, contador=0):

 if indice >= len(mochila):
   return False, contador

 objeto = mochila[indice]
 contador += 1

 print(f"Sacando objeto: {objeto}")

 if objeto == "sable de luz":
   return True, contador

 return usar_la_fuerza(mochila, indice + 1, contador)

encontrado, cantidad = usar_la_fuerza(mochila)

if encontrado:
  print(f"Se encontró el sable de luz sacando {cantidad} objetos.")
else:
  print(f"No se encontró el sable de luz. Se revisaron {cantidad} objetos.")
