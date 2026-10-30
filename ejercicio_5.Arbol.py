from tree import BinaryTree


class ArbolMCU(BinaryTree):
    """
    Árbol AVL de tree.py. Cada nodo guarda el nombre (clave) y
    other_values = {'is_villain': bool}  ->  True = villano, False = héroe
    (es la misma convención que usan inorden_villain, postorden_hero, etc. de tree.py).
    """

    def cargar(self, nombre, es_villano):
        self.insert_node(nombre, {'is_villain': es_villano})

    # b. villanos ordenados alfabéticamente (inorden).
    def inorden_villain(self):
        def recorrer(root):
            if root is not None:
                recorrer(root.left)
                if root.other_values['is_villain']:
                    print(root.value)
                recorrer(root.right)
        recorrer(self.root)

    # c, d y f se resuelven con los métodos que ya están en tree.py:
    #   inorden_hero_star_with('C')  -> héroes que empiezan con C
    #   count_heroes()               -> cantidad de héroes
    #   postorden_hero()             -> héroes en orden descendente (derecha - raíz - izquierda)

    # e. búsqueda por proximidad: devuelve los nombres que contienen el texto
    def buscar_por_proximidad(self, texto):
        encontrados = []

        def recorrer(root):
            if root is not None:
                recorrer(root.left)
                if texto.lower() in root.value.lower():
                    encontrados.append(root.value)
                recorrer(root.right)
        recorrer(self.root)
        return encontrados

    # e. como el nombre es la clave del árbol, cambiarlo implica eliminar el nodo y volver a insertarlo
    def modificar_nombre(self, nombre_actual, nombre_nuevo):
        nombre, datos = self.delete_node(nombre_actual)
        if nombre is not None:
            self.insert_node(nombre_nuevo, datos)
            return True
        return False

    # g. bosque: un árbol con los héroes y otro con los villanos
    def generar_bosque(self):
        heroes = ArbolMCU()
        villanos = ArbolMCU()

        def recorrer(root):
            if root is not None:
                recorrer(root.left)
                destino = villanos if root.other_values['is_villain'] else heroes
                destino.insert_node(root.value, dict(root.other_values))
                recorrer(root.right)
        recorrer(self.root)
        return heroes, villanos

    # g.I
    def contar_nodos(self):
        def contar(root):
            if root is None:
                return 0
            return contar(root.left) + 1 + contar(root.right)
        return contar(self.root)

    # g.II
    def listar_alfabetico(self):
        def recorrer(root):
            if root is not None:
                recorrer(root.left)
                print(root.value)
                recorrer(root.right)
        recorrer(self.root)


PERSONAJES = [
    # héroes
    ('Iron Man', False), ('Captain America', False), ('Thor', False), ('Hulk', False),
    ('Black Widow', False), ('Hawkeye', False), ('Spider-Man', False), ('Black Panther', False),
    ('Ant-Man', False), ('Wasp', False), ('Captain Marvel', False), ('Scarlet Witch', False),
    ('Vision', False), ('Falcon', False), ('Winter Soldier', False), ('War Machine', False),
    ('Star-Lord', False), ('Gamora', False), ('Drax', False), ('Rocket Raccoon', False),
    ('Groot', False), ('Shang-Chi', False), ('Wong', False),
    ('Dr. Strange', False),          # <- mal cargado a propósito (punto e)
    # villanos
    ('Thanos', True), ('Loki', True), ('Ultron', True), ('Red Skull', True), ('Hela', True),
    ('Killmonger', True), ('Ronan', True), ('Ego', True), ('Vulture', True), ('Mysterio', True),
    ('Kang', True), ('Dormammu', True), ('Kaecilius', True), ('Yellowjacket', True),
    ('Whiplash', True), ('Obadiah Stane', True), ('Mandarin', True), ('Abomination', True),
    ('Ebony Maw', True), ('Zemo', True), ('Malekith', True), ('Crossbones', True),
]


if __name__ == '__main__':
    arbol = ArbolMCU()
    for nombre, es_villano in PERSONAJES:
        arbol.cargar(nombre, es_villano)

    print('--- b. Villanos ordenados alfabéticamente ---')
    arbol.inorden_villain()

    print('\n--- c. Superhéroes que empiezan con C ---')
    arbol.inorden_hero_star_with('C')

    print('\n--- d. Cantidad de superhéroes ---')
    print(arbol.count_heroes())

    print('\n--- e. Búsqueda por proximidad "strange" ---')
    for nombre in arbol.buscar_por_proximidad('strange'):
        print('encontrado:', nombre)
        arbol.modificar_nombre(nombre, 'Doctor Strange')
    print('después de corregir:', arbol.buscar_por_proximidad('strange'))

    print('\n--- f. Superhéroes en orden descendente ---')
    arbol.postorden_hero()

    print('\n--- g. Bosque ---')
    heroes, villanos = arbol.generar_bosque()
    print('Nodos del árbol de héroes:', heroes.contar_nodos())
    print('Nodos del árbol de villanos:', villanos.contar_nodos())
    print('\nHéroes (A-Z):')
    heroes.listar_alfabetico()
    print('\nVillanos (A-Z):')
    villanos.listar_alfabetico()
