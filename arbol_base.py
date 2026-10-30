import contextlib
import io

# tree.py ejecuta código de prueba al importarse (imprime un preorden).
# Se silencia ese texto para no modificar el archivo del profe.
with contextlib.redirect_stdout(io.StringIO()):
    from tree import BinaryTree


class ArbolBase(BinaryTree):
    """
    BinaryTree de tree.py con una única corrección: delete_node.
    En el original, cuando el nodo a eliminar tiene dos hijos, se copia la clave del
    reemplazo (root.value = aux.value) pero no sus datos (other_values), y los datos
    quedan mezclados. Acá se copian también.
    """

    def delete_node(self, value):
        def reemplazo(root):
            if root.right is None:
                return root.left, root
            root.right, aux = reemplazo(root.right)
            return root, aux

        def eliminar(root, value):
            x = None
            otros = None
            if root is not None:
                if value < root.value:
                    root.left, x, otros = eliminar(root.left, value)
                elif value > root.value:
                    root.right, x, otros = eliminar(root.right, value)
                else:
                    x = root.value
                    otros = root.other_values
                    if root.left is None:
                        return root.right, x, otros
                    elif root.right is None:
                        return root.left, x, otros
                    else:
                        root.left, aux = reemplazo(root.left)
                        root.value = aux.value
                        root.other_values = aux.other_values   # <- la línea que faltaba
                root = self.auto_balance(root)
                self.update_height(root)
            return root, x, otros

        self.root, x, otros = eliminar(self.root, value)
        return x, otros
