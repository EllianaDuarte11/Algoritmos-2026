import unicodedata

from queue_ import Queue
from tree import BinaryTree


def clave(nombre):
    """
    Clave de ordenamiento del árbol: nombre sin tildes y en minúsculas.
    Así 'Águila del Cáucaso' queda entre las A y no después de la Z (las tildes
    tienen un código mayor que las letras comunes), y las búsquedas no dependen
    de tildes ni de mayúsculas. El nombre original se guarda en other_values.
    """
    base = unicodedata.normalize('NFD', nombre)
    return ''.join(c for c in base if unicodedata.category(c) != 'Mn').lower()


class ArbolCriaturas(BinaryTree):
    """
    Árbol AVL de tree.py. Cada nodo: value = clave(nombre) y
    other_values = {'nombre', 'derrotado_por', 'descripcion', 'capturada'}
    """

    def cargar(self, nombre, derrotado_por=None):
        datos = {
            'nombre': nombre,
            'derrotado_por': derrotado_por,   # None = no fue derrotada
            'descripcion': '',
            'capturada': None,                # g. quién la capturó (None = nadie)
        }
        self.insert_node(clave(nombre), datos)

    # a. listado inorden de las criaturas y quién la derrotó
    def listar_inorden(self):
        def recorrer(root):
            if root is not None:
                recorrer(root.left)
                datos = root.other_values
                print(f"{datos['nombre']} -> derrotada por: {datos['derrotado_por'] or 'nadie'}")
                recorrer(root.right)
        recorrer(self.root)

    # b. cargar (o cambiar) la descripción de una criatura
    def cargar_descripcion(self, nombre, descripcion):
        nodo = self.search(clave(nombre))
        if nodo is not None:
            nodo.other_values['descripcion'] = descripcion
            return True
        return False

    # c. toda la información de una criatura
    def mostrar_info(self, nombre):
        nodo = self.search(clave(nombre))
        if nodo is None:
            print(f'{nombre} no está en el árbol')
        else:
            datos = nodo.other_values
            print(f"Criatura: {datos['nombre']}")
            print(f"Derrotada por: {datos['derrotado_por'] or 'nadie'}")
            print(f"Capturada por: {datos['capturada'] or 'nadie'}")
            print(f"Descripción: {datos['descripcion'] or '(sin descripción)'}")

    # d. ranking de héroes/dioses por cantidad de criaturas derrotadas (de mayor a menor)
    def ranking_vencedores(self):
        conteo = {}

        def recorrer(root):
            if root is not None:
                recorrer(root.left)
                vencedor = root.other_values['derrotado_por']
                if vencedor is not None:
                    conteo[vencedor] = conteo.get(vencedor, 0) + 1
                recorrer(root.right)
        recorrer(self.root)
        return sorted(conteo.items(), key=lambda par: (-par[1], par[0]))

    # e. criaturas derrotadas por un héroe/dios
    def listar_derrotadas_por(self, heroe):
        def recorrer(root):
            if root is not None:
                recorrer(root.left)
                if root.other_values['derrotado_por'] == heroe:
                    print(root.other_values['nombre'])
                recorrer(root.right)
        recorrer(self.root)

    # f. criaturas que no han sido derrotadas
    def listar_no_derrotadas(self):
        def recorrer(root):
            if root is not None:
                recorrer(root.left)
                if root.other_values['derrotado_por'] is None:
                    print(root.other_values['nombre'])
                recorrer(root.right)
        recorrer(self.root)

    # g y h. registrar quién capturó a la criatura
    def capturar(self, nombre, captor):
        nodo = self.search(clave(nombre))
        if nodo is not None:
            nodo.other_values['capturada'] = captor
            return True
        return False

    # i. búsqueda por coincidencia (sin importar tildes ni mayúsculas)
    def buscar_por_coincidencia(self, texto):
        buscado = clave(texto)

        def recorrer(root):
            if root is not None:
                recorrer(root.left)
                if buscado in root.value:
                    print(root.other_values['nombre'])
                recorrer(root.right)
        recorrer(self.root)

    # j. eliminar una criatura
    def eliminar(self, nombre):
        valor, _ = self.delete_node(clave(nombre))
        return valor is not None

    # k. registrar que un héroe/dios derrotó a la criatura
    def registrar_derrota(self, nombre, heroe):
        nodo = self.search(clave(nombre))
        if nodo is not None:
            nodo.other_values['derrotado_por'] = heroe
            return True
        return False

    # l. cambiar el nombre (es la clave del árbol: se elimina el nodo y se vuelve a insertar)
    def renombrar(self, nombre_actual, nombre_nuevo):
        valor, datos = self.delete_node(clave(nombre_actual))
        if valor is None:
            return False
        datos['nombre'] = nombre_nuevo
        self.insert_node(clave(nombre_nuevo), datos)
        return True

    # m. listado por nivel (by_level de tree.py imprime la clave, acá se imprime el nombre real)
    def listar_por_nivel(self):
        pendientes = Queue()
        if self.root is not None:
            pendientes.arrive(self.root)
        while pendientes.size() > 0:
            nodo = pendientes.attention()
            print(nodo.other_values['nombre'])
            if nodo.left is not None:
                pendientes.arrive(nodo.left)
            if nodo.right is not None:
                pendientes.arrive(nodo.right)

    # n. criaturas capturadas por un héroe/dios
    def listar_capturadas_por(self, heroe):
        def recorrer(root):
            if root is not None:
                recorrer(root.left)
                if root.other_values['capturada'] == heroe:
                    print(root.other_values['nombre'])
                recorrer(root.right)
        recorrer(self.root)


# (criatura, derrotado por)  ->  None = '-' en la tabla
CRIATURAS = [
    ('Ceto', None), ('Tifón', 'Zeus'), ('Equidna', 'Argos Panoptes'), ('Dino', None),
    ('Pefredo', None), ('Enio', None), ('Escila', None), ('Caribdis', None),
    ('Euríale', None), ('Esteno', None), ('Medusa', 'Perseo'), ('Ladón', 'Heracles'),
    ('Águila del Cáucaso', None), ('Quimera', 'Belerofonte'), ('Hidra de Lerna', 'Heracles'),
    ('León de Nemea', 'Heracles'), ('Esfinge', 'Edipo'), ('Dragón de la Cólquida', None),
    ('Cerbero', None), ('Cerda de Cromión', 'Teseo'), ('Ortro', 'Heracles'),
    ('Toro de Creta', 'Teseo'), ('Jabalí de Calidón', 'Atalanta'), ('Carcinos', None),
    ('Gerión', 'Heracles'), ('Cloto', None), ('Láquesis', None), ('Átropos', None),
    ('Minotauro de Creta', 'Teseo'), ('Harpías', None), ('Argos Panoptes', 'Hermes'),
    ('Aves del Estínfalo', None), ('Talos', 'Medea'), ('Sirenas', None), ('Pitón', 'Apolo'),
    ('Cierva de Cerinea', None), ('Basilisco', None), ('Jabalí de Erimanto', None),
]

DESCRIPCIONES = {
    'Ceto': 'Diosa marina, madre de monstruos del mar',
    'Tifón': 'Monstruo gigantesco que desafió a los dioses del Olimpo',
    'Equidna': 'Mitad mujer, mitad serpiente, madre de monstruos',
    'Dino': 'Una de las Greas, hermana de Pefredo y Enio',
    'Pefredo': 'Una de las Greas, comparte un ojo y un diente con sus hermanas',
    'Enio': 'Una de las Greas, ancianas desde su nacimiento',
    'Escila': 'Monstruo marino de seis cabezas que acechaba un estrecho',
    'Caribdis': 'Remolino monstruoso que tragaba barcos enteros',
    'Euríale': 'Una de las tres Gorgonas, hermana inmortal de Medusa',
    'Esteno': 'Una de las tres Gorgonas, hermana inmortal de Medusa',
    'Medusa': 'Gorgona de cabello de serpientes que petrificaba con la mirada',
    'Ladón': 'Dragón que custodiaba las manzanas doradas del jardín de las Hespérides',
    'Águila del Cáucaso': 'Águila que devoraba cada día el hígado de Prometeo',
    'Quimera': 'Monstruo con cabeza de león, cuerpo de cabra y cola de serpiente',
    'Hidra de Lerna': 'Serpiente acuática de múltiples cabezas que se regeneraban',
    'León de Nemea': 'León de piel invulnerable que aterrorizaba Nemea',
    'Esfinge': 'Monstruo alado que planteaba un enigma a los viajeros de Tebas',
    'Dragón de la Cólquida': 'Dragón que vigilaba el Vellocino de Oro',
    'Cerbero': 'Perro de tres cabezas guardián de la entrada al Hades',
    'Cerda de Cromión': 'Gigantesca cerda que devastaba los campos de Cromión',
    'Ortro': 'Perro de dos cabezas que cuidaba el ganado de Gerión',
    'Toro de Creta': 'Toro enloquecido que asolaba la isla de Creta',
    'Jabalí de Calidón': 'Jabalí enviado por Artemisa para castigar a Calidón',
    'Carcinos': 'Cangrejo gigante que ayudó a la Hidra contra Heracles',
    'Gerión': 'Gigante de tres cuerpos dueño de un rebaño de bueyes rojos',
    'Cloto': 'Una de las Moiras, hila el hilo de la vida',
    'Láquesis': 'Una de las Moiras, mide el hilo de la vida',
    'Átropos': 'Una de las Moiras, corta el hilo de la vida',
    'Minotauro de Creta': 'Criatura con cuerpo de hombre y cabeza de toro, encerrada en el laberinto',
    'Harpías': 'Criaturas aladas con rostro de mujer que robaban comida',
    'Argos Panoptes': 'Gigante de cien ojos, guardián incansable',
    'Aves del Estínfalo': 'Aves de picos y garras de bronce que se alimentaban de hombres',
    'Talos': 'Gigante de bronce que protegía la isla de Creta',
    'Sirenas': 'Seres que atraían a los marinos con su canto hacia la muerte',
    'Pitón': 'Serpiente gigante que custodiaba el oráculo de Delfos',
    'Cierva de Cerinea': 'Cierva de cuernos dorados consagrada a Artemisa',
    'Basilisco': 'Serpiente cuya mirada y aliento podían matar',
    'Jabalí de Erimanto': 'Enorme jabalí que habitaba el monte Erimanto',
}


if __name__ == '__main__':
    arbol = ArbolCriaturas()
    for nombre, vencedor in CRIATURAS:
        arbol.cargar(nombre, vencedor)

    print('--- a. Criaturas (inorden) y quién las derrotó ---')
    arbol.listar_inorden()

    for nombre, texto in DESCRIPCIONES.items():      # b.
        arbol.cargar_descripcion(nombre, texto)

    print('\n--- c. Información de Talos ---')
    arbol.mostrar_info('Talos')

    print('\n--- d. Los 3 que derrotaron más criaturas ---')
    ranking = arbol.ranking_vencedores()
    for heroe, cantidad in ranking[:3]:
        print(f'{heroe}: {cantidad}')
    if ranking[3][1] == ranking[2][1]:
        print(f'(el 3.er puesto está empatado: hay más héroes/dioses con {ranking[2][1]} criatura derrotada)')

    print('\n--- e. Derrotadas por Heracles ---')
    arbol.listar_derrotadas_por('Heracles')

    print('\n--- f. Criaturas no derrotadas ---')
    arbol.listar_no_derrotadas()

    print('\n--- h. Heracles captura a Cerbero, Toro de Creta, Cierva de Cerinea y Jabalí de Erimanto ---')
    for nombre in ['Cerbero', 'Toro de Creta', 'Cierva de Cerinea', 'Jabalí de Erimanto']:
        arbol.capturar(nombre, 'Heracles')
    arbol.mostrar_info('Cerbero')

    print('\n--- i. Búsqueda por coincidencia: "dra" ---')
    arbol.buscar_por_coincidencia('dra')
    print('(sin tildes)')
    arbol.buscar_por_coincidencia('aguila')

    print('\n--- j. Eliminar Basilisco y Sirenas ---')
    print('Basilisco eliminado:', arbol.eliminar('Basilisco'))
    print('Sirenas eliminadas:', arbol.eliminar('Sirenas'))

    print('\n--- k. Heracles derrotó a las Aves del Estínfalo ---')
    arbol.registrar_derrota('Aves del Estínfalo', 'Heracles')
    arbol.mostrar_info('Aves del Estínfalo')

    print('\n--- l. Ladón pasa a llamarse Dragón Ladón ---')
    arbol.renombrar('Ladón', 'Dragón Ladón')
    arbol.mostrar_info('Dragón Ladón')

    print('\n--- m. Listado por nivel ---')
    arbol.listar_por_nivel()

    print('\n--- n. Criaturas capturadas por Heracles ---')
    arbol.listar_capturadas_por('Heracles')
