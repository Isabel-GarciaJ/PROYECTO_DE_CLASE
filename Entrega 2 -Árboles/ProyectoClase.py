#Big tree
#find_attr y find_attrs: Busca uno o varios nodos por atributo.

#find_name y find_names: Busca uno o varios nodos por nombre.  

#Clase Nodo, capacidad(peso), nodos hijos, pedido(numero de pedido) y metodo para cambiar el pedido
class Nodo:
    def __init__(self, pedido):
        self.valor = pedido
        self.der = None
        self.izq = None

def obtener_sucesor(actual):
    actual = actual.der
    while actual is not None and actual.izq is not None:
        actual = actual.izq
    return actual

def eliminar_nodo(raiz, x):
    if raiz is None:
        return raiz

    if raiz.pedido > x:
        raiz.izq = eliminar_nodo(raiz.izq, x)
    elif raiz.pedido < x:
        raiz.der = eliminar_nodo(raiz.der, x)
    else:
        if raiz.izq is None:
            return raiz.der
        if raiz.der is None:
            return raiz.izq

        sucesor = obtener_sucesor(raiz)
        raiz.pedido = sucesor.pedido
        raiz.der = eliminar_nodo(raiz.der, sucesor.pedido)
        
    return raiz

def cambiar_pedido(self, nuevo_pedido):
        self.pedido = nuevo_pedido

def recorrido_inorden(raiz):
    if raiz is not None:
        recorrido_inorden(raiz.izq)
        print(raiz.pedido, end=" ")
        recorrido_inorden(raiz.der)

# Arbol binario,todos los nodos son pedidos, empleados fijos (repartidor). Altura 3
    #Metodo para peso de las rutas
    #Metodo para decidir que repatidores pueden realizar y que se escoja el de una capacidad más cercana
    #agregar nuevas rutas
    #Eliminar pedido ya recorrido
    #metodo para buscar nodo (numero pedido) con big tree find_name
    #Impripmir
class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self.insertar_nodo(self.raiz, valor)

    def insertar_nodo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izq is None:
                nodo.izq = Nodo(valor)
            else:
                self.insertar_nodo(nodo.izq, valor)
        else:
            if nodo.der is None:
                nodo.der = Nodo(valor)
            else:
                self.insertar_nodo(nodo.der, valor)

    def recorrido_inorden(self, nodo):
        if nodo:
            self.recorrido_inorden(nodo.izq)
            print(nodo.valor, end=' ')
            self.recorrido_inorden(nodo.der)

    def recorrido_preorden(self, nodo):
        if nodo:
            print(nodo.valor, end=' ')
            self.recorrido_preorden(nodo.izq)
            self.recorrido_preorden(nodo.der)

    def recorrido_postorden(self, nodo):
        if nodo:
            self.recorrido_postorden(nodo.izq)
            self.recorrido_postorden(nodo.der)
            print(nodo.valor, end=' ')



#Pedido (Si se agregan productos usar lectura de archivos),(numero de pedido), 
# peso (si se usan productos,metodo para calcular peso), (precio a cobrar no seeeeee)
    #imprimir
    #chequear pedido (Una vez pasa el repartidor se coloca peso en cero y pedido en none)

class Pedido:
	def __init__ (self, numpedido, peso, precio):  
		self.numpedido = numpedido
		self.peso = peso
		self.precio = precio

def imprimir(self):
        print("Pedido #", self.numpedido, " - Peso: ", self.peso, "kg - Precio: $", self.precio)

def chequear_entrega(self):
    print("Pedido #", self.numpedido, "entregado.")
    self.peso = 0
    self.numpedido = None
    self.precio = 0



#Repartidor: nombre, capacidad y vehiculo,(Lista con numero de pedidos)
class Repartidor:
	def __init__ (self, nombre, capacidad, vehiculo):
		self.nombre = nombre
		self.capacidad = capacidad
		self.vehiculo = vehiculo



#Demo: Rutas ya establecidas, metodo para agregar rutas