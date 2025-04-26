#Big tree
#find_attr y find_attrs: Busca uno o varios nodos por atributo.

#find_name y find_names: Busca uno o varios nodos por nombre.  

# Arbol binario,todos los nodos son pedidos, empleados fijos (repartidor). Altura 3
    #Metodo para peso de las rutas
    #Metodo para decidir que repatidores pueden realizar y que se escoja el de una capacidad más cercana
    #agregar nuevas rutas
    #Eliminar pedido ya recorrido
    #metodo para buscar nodo (numero pedido) con big tree find_name
    #Impripmir

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.der = None
        self.izq = None

# Note that it is not a generic inorder successor 
# function. It mainly works when the right child
# is not empty, which is  the case we need in BST
# delete.
def get_successor(curr):
    curr = curr.der
    while curr is not None and curr.izq is not None:
        curr = curr.izq
    return curr

# This function deletes a given key x from the
# given BST and returns the modified root of the 
# BST (if it is modified).
def del_node(root, x):
  
    # Base case
    if root is None:
        return root

    # If key to be searched is in a subtree
    if root.valor > x:
        root.izq = del_node(root.izq, x)
    elif root.valor < x:
        root.der = del_node(root.der, x)
        
    else:
        # If root matches with the given key

        # Cases when root has 0 children or 
        # only right child
        if root.izq is None:
            return root.der

        # When root has only left child
        if root.der is None:
            return root.izq

        # When both children are present
        succ = get_successor(root)
        root.valor = succ.valor
        root.der = del_node(root.der, succ.valor)
        
    return root

# Utility function to do inorder traversal
def inorder(root):
    if root is not None:
        inorder(root.izq)
        print(root.valor, end=" ")
        inorder(root.der)

# Driver code
if __name__ == "__main__":
    root = Nodo(10)
    root.izq = Nodo(5)
    root.der = Nodo(15)
    root.der.izq = Nodo(12)
    root.der.der = Nodo(18)
    x = 15

    root = del_node(root, x)
    inorder(root)
    print()

#Clase Nodo, capacidad(peso), nodos hijos, pedido(numero de pedido) y metodo para cambiar el pedido

#Pedido (Si se agregan productos usar lectura de archivos),(numero de pedido), 
# peso (si se usan productos,metodo para calcular peso), (precio a cobrar no seeeeee)
    #imprimir
    #chequear pedido (Una vez pasa el repartidor se coloca peso en cero y pedido en none)

class Pedido:
	def __init__ (self, numpedido, peso, precio):  
		self.numpedido = numpedido
		self.peso = peso
		self.precio = precio
	
#Repartidor: nombre, capacidad y vehiculo,(Lista con numero de pedidos)
class Repartidor:
	def __init__ (self, nombre, capacidad, vehiculo):
		self.nombre = nombre
		self.capacidad = capacidad
		self.vehiculo = vehiculo

#Demo: Rutas ya establecidas, metodo para agregar rutas